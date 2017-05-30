##!/usr/bin/python3
# -*- coding: utf-8 -*-

class Pelicula:

    def __init__(self):
        self.server = 'www.unserver.com'

    def buscar(self, nombre):
        """
        Busca peliculas por nombre.

        return:
            lista de archivos
        """
        return ['Duro de Matar 1', 'Duro de Matar 2']

    def descargar (self, lista_archivos):
        """
        Recibe una lista peliculas para descargar.

        return:
            lista de archivos descargado satifactoriamente.
        """
        return ['Duro de Matar 1 descargado Ok', 'Duro de Matar 2 descargado Ok']
