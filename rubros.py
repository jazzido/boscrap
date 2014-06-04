import sys
import os
import re
from datetime import datetime
import urlparse
import json
from multiprocessing import Pool

from bs4 import BeautifulSoup
import requests
import xmltodict

XML_URL_TMPL = "http://www.boletinoficial.gov.ar/Content/XML/Avisos/02/%s/%s/%s/%s.xml"
AVISO_HREF_RE = re.compile('^/Avisos')

def get_aviso(qs):
        print >>sys.stderr, "getting aviso: %s" % (qs['idAviso'][0])
        f = qs['f'][0]
        fecha = "%s-%s-%s" % (f[0:4], f[4:6], f[6:8])
        r = requests.get(XML_URL_TMPL % (f[0:4], f[4:6], f[6:8], qs['idAviso'][0]))
        try:
                rv = xmltodict.parse(r.text[3:].encode('latin-1').decode('utf-8'))['Aviso']
                rv['fecha'] = fecha
                rv['avisoId'] = qs['idAviso'][0]
                return rv
        except Exception as e:
                print >>sys.stderr, "Error in get: %s" % e
                return None


def main(fname):
        POOL = Pool(processes=4)
        soup = BeautifulSoup(open(fname).read())
        for r in soup.find('table', {'class':'TablaResultadoPortadaSegunda'}) \
                     .findAll('div', {'class': 'HeaderRubro'}):
                rubro = r.text.strip()
                avisos_qss = [urlparse.parse_qs(urlparse.urlparse(aviso['href']).query) for aviso in r.findParent('tr') \
                              .findNextSibling('tr') \
                              .findNextSibling('tr') \
                              .findAll('a', {'href': AVISO_HREF_RE})]

                results = POOL.map(get_aviso, avisos_qss)
                for result in results:
                        if result is None:
                                continue
                        with open(os.path.join(os.path.dirname(fname), result['avisoId'] + '.json'), 'w') as out:
                                json.dump(result, out)

if __name__ == '__main__':
        main(sys.argv[1])
