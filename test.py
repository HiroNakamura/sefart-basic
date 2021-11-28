#!/bin/python3

from PyZenity import ErrorMessage, InfoMessage
from tkinter.filedialog import askopenfilename
from tkinter import *

def main():
    archivo = None
    try:
        Tk().withdraw()
        archivo = askopenfilename()
    except TypeError as ex:
        ErrorMessage("Ha ocurrido una excepcion al obtener el archivo: "+str(ex))
    
    if archivo != None:
        try:
            InfoMessage("Seleccion: "+str(archivo))
        except Exception as ex:
            ErrorMessage("Ha ocurrido un error al tratar de mostrar la información: "+str(ex))
    

if __name__ == '__main__':
  main()

