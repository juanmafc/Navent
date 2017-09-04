from PIL import Image
import random
import image_average
import math
import os
import sys



diccionarioPromedios = {}


def calcularDistancia(color1, color2):
    return math.sqrt( (color1[0] - color2[0])**2 + (color1[1] - color2[1])**2 + (color1[2] - color2[2])**2 )

def encontrarImagenMasCercana(promedios):
    distanciaMinima = -1
    imagenMasCercana = ""


    for nombreImagen, promediosImagen in diccionarioPromedios.iteritems():
        distancia = 0
        for i in range(0, len(promedios)/3-1):
            offsetPromedio = i * 3
            promedio = [ promedios[offsetPromedio], promedios[offsetPromedio+1], promedios[offsetPromedio+2] ]
            promedioImagen = [ promediosImagen[offsetPromedio], promediosImagen[offsetPromedio+1], promediosImagen[offsetPromedio+2] ]
            distancia += calcularDistancia(promedioImagen, promedio)

        distancia = distancia / (len(promedios)/3)
        if ( (distancia < distanciaMinima) or ( distanciaMinima == -1 ) ):
            distanciaMinima = distancia
            imagenMasCercana = nombreImagen

    return Image.open("images/" + imagenMasCercana)

# Funcion de muestra que debera ser reemplazada por la funcion que ustedes implementen.
# Lo que hace esta funcion dummy es elegir con 50% de probabilidad si poner todo negro
# o no la region que le pasan.
def dummy_function(region):
    ancho, alto = region.size
    promediosRegion = image_average.procesarPromedioDeImagen(region)
    promedios = []
    for colorPromedio in promediosRegion:
        promedios.append(colorPromedio[0])
        promedios.append(colorPromedio[1])
        promedios.append(colorPromedio[2])
    return encontrarImagenMasCercana(promedios)


# Funcion auxiliar que los participantes pueden usar como ayuda
# file_name: nombre de la imagen original
# step_size: tamanio en pixels que tiene la seccion que se va iterando en la imagen
# function_to_apply: funcion que los participantes tienen que implementar, esta funcion
# recibe una region de tamanio step_size x step_size de tipo Image y tiene que devolver
# otra instancia de tipo Imgage
def apply_to_image(file_name, step_size, function_to_apply):
    HS = step_size
    WS = step_size

    im = Image.open(file_name).convert('RGB')
    ancho, alto = im.size
    for h in range(0, alto, HS):
        for w in range (0, ancho, WS):
            box = (w, h, w+WS, h+HS)
            region = im.crop(box)
            region = function_to_apply(region)
            region = region.resize((WS, HS), Image.ANTIALIAS)
            im.paste(region, box)
    return im





archivoPromedios = open("promedios.txt", "r")
for linea in archivoPromedios:
    datosPromedio = linea.split(" ")
    nombreImagen = datosPromedio[0]
    diccionarioPromedios[nombreImagen] = []
    for i in range(1, len(datosPromedio)-1,3):
        r = datosPromedio[i]
        g = datosPromedio[i+1]
        b = datosPromedio[i+2]
        diccionarioPromedios[nombreImagen].append(int(r))
        diccionarioPromedios[nombreImagen].append(int(g))
        diccionarioPromedios[nombreImagen].append(int(b))


logo = 0
for archivoLogo in os.listdir('./logos'):
    apply_to_image("logos/" + archivoLogo, int(sys.argv[3]), dummy_function).save( "logo" + str(logo) + ".bmp")
    logo += 1
