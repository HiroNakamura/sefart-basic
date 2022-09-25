# Sefart-basic

> Ésta es una copia del repositorio de Sefart.net 

Se hará un cambio usando PyZenity.

Para más información [sefart.net](https://sefart.net/metodologia/)

Este es el código más simple en este asunto para ahorrar el esfuerzo inicial.
El código está en Python con algún estilo de programación funcional.
Para comenzar a trabajar con el código encriptado en la Torá, necesitamos tres (3) cosas:

- **Genesis.txt:** un libro para trabajar.
  Nosotros podemos encontrar más libros en [tanach.us](https://tanach.us/Server.txt?Genesis*&content=Consonants)

- **mispar.py:** es una tabla de conversión numérica.
Trabajaremos con los valores de 22 letras Mispar-Hechrachi.
Son variantes como los valores de Mispar-Gadol, entre otros[1].

- **gematria.py:** es el script de procesamiento.

Para usar:
- Descargar ambos archivos *.py*
- En segundo lugar, descargue un libro de la URL sugerida anteriormente.
- Moverlos todos a la misma carpeta.
- Dentro del folder ejecuta:
  `python3 gematria.py Genesis.txt`

Puedes comprobar tus resultados con:

![gematrix.org](https://raw.githubusercontent.com/giancarlocp/sefart-basic/master/img/gematrix.org.png)

El procesamiento del resultado de las primeras líneas  Genesis.txt es:

![result](https://raw.githubusercontent.com/giancarlocp/sefart-basic/master/img/result-example.png)

Para obtener el código binario espejo, sugerimos insertar las siguientes líneas después
nosotros obtenemos `gem` en [gematria.py](https://github.com/giancarlocp/sefart-basic/blob/master/gematria.py#L23):
```python
binary = format(gem,'012b')
mirror = binary[::-1]
```

No guardamos la información procesada en ningún formato.
La intención es dar un código / conocimiento básico con el que empezar a trabajar.

Enlace:

[1] https://en.wikipedia.org/wiki/Gematria
[2] http://brianramos.com
[3] https://github.com/rlebron88/PyZenity
[4] https://pypi.org/project/python-zenity/
[5] http://brianramos.com/software/PyZenity/docs/
[6] https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python