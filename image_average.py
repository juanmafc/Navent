import Image
import os
import sys

def calcularPromedio((x0,y0), ancho, alto, imagen):
    r, g, b = 0, 0, 0
    cantidad = 0
    anchoImagen, altoImagen = imagen.size
    for x in range(x0, x0+ancho):
        for y in range(y0, y0+alto):
            if ( (x < anchoImagen) and (y < altoImagen) ):
                pixelR, pixelG, pixelB = imagen.getpixel((x,y))
                r += pixelR
                g += pixelG
                b += pixelB
                cantidad += 1
    return [(r/cantidad), (g/cantidad), (b/cantidad)]


def procesarPromedioDeImagen(imagen):
    ancho, alto = imagen.size
    promedios = []

    stepHorizontal = ancho/int(sys.argv[1])
    stepVertical = alto/int(sys.argv[2])
    for offsetHorizontal in range(0, ancho - 1, stepHorizontal):
        for offsetVertical in range(0, alto - 1, stepVertical):
            coloresPromedios = calcularPromedio( (offsetHorizontal,offsetVertical), stepHorizontal, stepVertical, imagen)
            for color in coloresPromedios:
                promedios.append(color)
    return  promedios


archivoPromedios = open("promedios.txt", "w")
for archivoImagen in os.listdir('./images'):
    promedios = procesarPromedioDeImagen(  Image.open("images/" + archivoImagen).convert('RGB'))
    archivoPromedios.write(archivoImagen)
    for promedio in promedios:
        archivoPromedios.write( " " + str(promedio) )
    archivoPromedios.write("\n")
archivoPromedios.close()
