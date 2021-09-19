#!/bin/python3

from PyZenity import ErrorMessage, InfoMessage
from PyZenity import GetFilename

def main():
    archivo = None
    lineas = None
    try:
        archivo = GetFilename(multiple=True,sep='|')
    except TypeError as ex:
        ErrorMessage("Ha ocurrido una excepcion al obtener el archivo: "+str(ex))
    
    
    if archivo != None:
        try:
            InfoMessage("seleccion: "+archivo)
        except Exception as ex:
            ErrorMessage("Ha ocurrido un error al tratar de mostrar la información: "+str(ex))
    

if __name__ == '__main__':
  main()

