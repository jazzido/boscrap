BOSCRAP!!!1
===========

Scraper de la segunda sección del [Boletín Oficial de la República Argentina](http://www.boletinoficial.gov.ar).

Emite resultados en formato CSV.




## Ejemplo

```
$ python boscrap.py 2013-10-07 > bo.csv
$ head -n 5 bo.csv
Fecha,AvisoId,Titulo,Texto,Empieza-Vence,NumeroPagDesde,NumeroPagHasta,Rubro
2013-10-07,4485883,AGROPELL,"Escritura Rectificatoria Nº 283 del 3/10/2013, Reg. 209, Escr. Juan Manuel Reynal O’Connor: Ante observación de IGJ: se modifica el artículo cuarto del estatuto social correspondiente al objeto social quedando redactado de la siguiente manera: La sociedad tiene por objeto dedicarse por cuenta propia y/o asociada a terceros a las siguientes actividades: a) operaciones agrícologanaderas: comprendiendo toda clase de actividad agropecuaria, explotación de campos, cría y engorde de pollos, cría y engorde de ganado menor y mayor, fruticultura, huertos de todo tipo, forestación, avicultura en todas sus etapas y tambo, pudiendo extender hasta las etapas comerciales e industriales de los productos derivados de esa explotación, incluyendo en esto la conservación, fraccionamiento, envasado y exportación de los mismos; b) comercialización y compraventa, incluyendo importación y exportación, de frutos del país; c) comercialización y compraventa, incluyendo importación y exportación, por cuenta propia y/o de terceros, de todos aquellos productos derivados directa o indirectamente de las actividades de producción detalladas en a). Para el cumplimiento de su objeto, la sociedad tendrá plena capacidad jurídica para realizar todo tipo de actos, contratos y operaciones que se relaciones directa o indirectamente con aquel. Autorizado según instrumento público Esc. Nº 266 de fecha 23/09/2013 Reg. Nº 209. Vanesa Elisabeth Kukva Tº: 112 Fº: 660 C.P.A.C.F.",e. 07/10/2013 Nº 79894/13 v. 07/10/2013,1,1,Sociedades Anonimas
2013-10-07,4484960,AYRE LIBRE,"1) 26/9/13. 2) Gustavo A. Muia, argentino, 30/10/80, casado, empresario, 28.283.934, Pumacahua 311, piso 6º A, CABA; Walter C. Muia, argentino, 22/6/74, casado, Lic. en Publicidad, 23.815.851, Av. Alvear 1564, Banfield, Pcia. Bs. As; Diego A. Muia, argentino, 3/7/77, casado, empresario, 25.969.571, Rodríguez Peña 599, Banfield, Pcia. Bs. As.; Andrea S. Muia, argentina, 24/5/79, soltera, abogada, 27.343.052, Juan Bautista Alberdi 2449, 3º F, CABA; Diana P. Muia, argentina, 13/483, soltera, Lic. en Diseño textil e Indumentaria, 30.236.270, Av. Alvear 1564, Banfield, Pcia. Bs. As.; y Paula N. Muia, argentina, 8/1077, casada, empresaria, 26.230.192, José María Moreno 479, Lanus, Pcia. Bs. As.
3) Curapaligue Nº 63, piso 5º, oficina B, C.A.B.A.; 4) a) Diseño, comercialización, industrialización y fabricación de calzados y de ar-tículos de cuero, textiles y otros de vestimenta o indumentaria masculina o femenina y de niños, en general; y b) la compra, venta, importación y exportación de bienes, mercaderías y materias primas relacionadas con su objeto social. 5) 99 años. 6) se prescinde de sindicatura. 7) $ 120.000. 8) Presidente: Andrea S. Muia.- Vicepresidente: Diana P. Muia. Director Suplente: Diego A. Muia. Constituyen domicilio en la sede social. 9) Presidente - 3 Ejercicios. 10) 30/9. Autorizado según instrumento público Esc. Nº 110 de fecha 26/09/2013 Reg. Nº 1941 María Florencia Zungri  Tº: 106 Fº: 284 C.P.A.C.F.",e. 07/10/2013 Nº 78971/13 v. 07/10/2013,1,1,Sociedades Anonimas
2013-10-07,4485648,BLUE OCEAN EXPERT,"Complementaria del T.I. 72717/13 del 16/9/2013, se rectifica la fecha de cierre del ejercicio, siendo la correcta 31/3/2013. Autorizado según instrumento público Esc. Nº 149 de fecha 12/09/2013 Reg. Nº 834. Susana del Valle del Blanco de Enriquez Matrícula: 3342 C.E.C.B.A.",e. 07/10/2013 Nº 79659/13 v. 07/10/2013,1,1,Sociedades Anonimas
```

## Licencia

Dominio público (http://unlicense.org)
