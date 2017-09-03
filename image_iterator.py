from PIL import Image
import random


# Funcion de muestra que debera ser reemplazada por la funcion que ustedes implementen.
# Lo que hace esta funcion dummy es elegir con 50% de probabilidad si poner todo negro
# o no la region que le pasan.
def dummy_function(region):
    if random.random() < 0.5:
    	return Image.eval(region, lambda x: 1)
    return region


# Funcion auxiliar que los participantes pueden usar como ayuda
# file_name: nombre de la imagen original
# step_size: tamanio en pixels que tiene la seccion que se va iterando en la imagen
# function_to_apply: funcion que los participantes tienen que implementar, esta funcion
# recibe una region de tamanio step_size x step_size de tipo Image y tiene que devolver
# otra instancia de tipo Imgage
def apply_to_image(file_name, step_size, function_to_apply):
    HS = step_size
    WS = step_size
    

    im = Image.open(file_name)
    ancho, alto = im.size
    for h in range(0, alto, HS):
        for w in range (0, ancho, WS):
            box = (w, h, w+WS, h+HS)
            region = im.crop(box)
            region = function_to_apply(region)
            region = region.resize((WS, HS), Image.NEAREST)
            im.paste(region, box)

    return im


FOTO_ORIGINAL = "imagen.png"
TAMANIO_EN_PIXELS_SUB_IMAGENES = 10
FUNCION_A_IMPLEMENTAR = dummy_function

apply_to_image(FOTO_ORIGINAL, TAMANIO_EN_PIXELS_SUB_IMAGENES, FUNCION_A_IMPLEMENTAR).save("out.bmp")
