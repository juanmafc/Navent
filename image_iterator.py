from PIL import Image
import random
import image_average
import math
import os




diccionarioPromedios = {}

def calcularDistancia(color1, color2):
    return math.sqrt( (color1[0] - color2[0])**2 + (color1[1] - color2[1])**2 + (color1[2] - color2[2])**2 )

def encontrarImagenMasCercana(promedio):
    distanciaMinima = -1
    imagenMasCercana = ""

    for nombreImagen, promedioImagen in diccionarioPromedios.iteritems():
        distancia = calcularDistancia(promedioImagen, promedio)
        if ( (distancia < distanciaMinima) or ( distanciaMinima == -1 ) ):
            distanciaMinima = distancia
            imagenMasCercana = nombreImagen
    return Image.open("images/" + imagenMasCercana)

# Funcion de muestra que debera ser reemplazada por la funcion que ustedes implementen.
# Lo que hace esta funcion dummy es elegir con 50% de probabilidad si poner todo negro
# o no la region que le pasan.
def dummy_function(region):
    ancho, alto = region.size
    promedioRegion = image_average.calcularPromedio((0,0), ancho, alto, region)
    return encontrarImagenMasCercana(promedioRegion)


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
            '''
            anchoImagen, altoImagen = region.size
            areaInicial = anchoImagen * altoImagen
            nuevoAncho = HS*anchoImagen/altoImagen
            nuevaAltura = WS*altoImagen/anchoImagen
            nuevaArea1 = HS * nuevoAncho
            nuevaArea2 = WS * nuevaAltura
            if ( (nuevaArea1) > (nuevaArea2) ):
                altoImagen = HS
                anchoImagen = nuevoAncho
            else:
                anchoImagen = WS
                altoImagen = nuevaAltura
            '''
            region = region.resize((WS, HS), Image.ANTIALIAS)
            #region = region.resize((anchoImagen, altoImagen), Image.ANTIALIAS)
            im.paste(region, box)
            #im.paste(region, (w,h))

    return im


archivoPromedios = open("promedios.txt", "r")
for linea in archivoPromedios:
    nombreImagen, r, g, b = linea.split(" ")
    diccionarioPromedios[nombreImagen] = [ int(r), int(g), int(b) ]
    #print diccionarioPromedios


logo = 0
for archivoLogo in os.listdir('./logos'):
    apply_to_image("logos/" + archivoLogo, 16, dummy_function).save( "logo" + str(logo) + ".bmp")
    logo += 1
