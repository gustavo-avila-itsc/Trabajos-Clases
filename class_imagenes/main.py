##!/usr/bin/python3
# -*- coding: utf-8 -*-

from archivo import Archivo
from pelicula import Pelicula
from imagen import Imagen 

pelicula = Pelicula()
imagen= Imagen()
archivo = Archivo(pelicula)
archivo2=Archivo(imagen)

descarados=[]
encontrados2 = []

encontrados = archivo.buscar('Duro de matar')
descargados2= archivo2.buscar('hola')

print (archivo.descargar(encontrados),archivo2.descargar(encontrados2) )

