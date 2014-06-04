import sys
import os
import re
from datetime import datetime, timedelta
import urlparse
import json
from multiprocessing import Pool
from contextlib import contextmanager

from bs4 import BeautifulSoup
import requests
import xmltodict
import unicodecsv

LISTING_URL_TMPL = "http://www.boletinoficial.gov.ar/SegundaSeccion/ListarPortadas.castle?idRubro=2&fecha=%s"
XML_URL_TMPL = "http://www.boletinoficial.gov.ar/Content/XML/Avisos/02/%s/%s/%s/%s.xml"
AVISO_HREF_RE = re.compile('^/Avisos')
PARALLEL_DOWNLOADS = 4

start_date = datetime(2009,5,4)
end_date   = datetime.now()

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        d = start_date + timedelta(n)
        if d.weekday() != 0 and d.weekday() != 6: # saltear sabados y domingos
            yield d

def get_aviso(qs):
    print >>sys.stderr, "getting aviso: %s" % (qs['idAviso'][0])
    f = qs['f'][0]
    fecha = "%s-%s-%s" % (f[0:4], f[4:6], f[6:8])
    url = XML_URL_TMPL % (f[0:4], f[4:6], f[6:8], qs['idAviso'][0])
    r = requests.get(url)
    try:
        rv = xmltodict.parse(r.text[3:].encode('latin-1').decode('utf-8'))['Aviso']
        rv['Fecha'] = fecha
        rv['AvisoId'] = qs['idAviso'][0]
        return rv
    except Exception as e:
        print >>sys.stderr, "Error getting aviso: %s" % url
        return None


def get_avisos_from_listado(page):
    POOL = Pool(processes=PARALLEL_DOWNLOADS)
    soup = BeautifulSoup(page)

    for r in soup.findAll('div', {'class': 'HeaderRubro'}):
        rubro = r.text.strip()
        print >>sys.stderr, "Rubro: %s" % rubro
        avisos_qss = [urlparse.parse_qs(urlparse.urlparse(aviso['href']).query) for aviso in r.findParent('tr') \
                  .findNextSibling('tr') \
                  .findNextSibling('tr') \
                  .findAll('a', {'href': AVISO_HREF_RE})]

        for aviso in POOL.map(get_aviso, avisos_qss):
            if aviso is None:
                continue
            aviso['Rubro'] = rubro
            yield aviso

def get_listado_for_date(date):
    url = LISTING_URL_TMPL % date.strftime('%d/%m/%Y')
    print >>sys.stderr, "getting listado for date %s (%s)" % (date.strftime('%Y-%m-%d'), url)
    r = requests.get(url)
    body = r.text
    if 'No se encontraron registros' in body:
        print >>sys.stderr, "No items on date %s" % date.strftime('%d/%m/%Y')
        return
    for aviso in get_avisos_from_listado(body):
        yield aviso

@contextmanager
def output_csv(out):
    writer = unicodecsv.DictWriter(out,
                                   ['Fecha',
                                    'AvisoId',
                                    'Titulo',
                                    'Texto',
                                    'Empieza-Vence',
                                    'NumeroPagDesde',
                                    'NumeroPagHasta',
                                    'Rubro'],
                                   extrasaction='ignore')

    writer.writeheader()

    yield writer



if __name__ == '__main__':

    date = None
    try:
        date = datetime.strptime(sys.argv[1], '%Y-%m-%d')
    except:
        print >>sys.stderr, "Usage: %s YYYY-mm-dd" % sys.argv[0]
        sys.exit(1)

    with output_csv(sys.stdout) as out:
        for aviso in get_listado_for_date(date):
            out.writerow(aviso)
