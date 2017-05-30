# -*- coding: utf-8 -*-


class Archivo:

    def __init__(self, archivo):
        self.archivo = archivo

    def buscar(self, nombre):
        """
        Busca archivospor nombre con la fecha de creacion desde fecha_inicio

        return:
            lista de archivos
        """
        return self.archivo.buscar(nombre)

    def descargar (self, lista_archivos):
        """
        Recibe una lista archivos para descargar.

        return:
            lista de archivos descargado satifactoriamente.
        """
        return self.archivo.descargar(lista_archivos)


"""
Use
from archivo import Archivo()
from pelicula import Pelicula()

pelicula = Pelicula()
archivo = Archivo(pelicula)
y usar  archivo para llamar
"""
