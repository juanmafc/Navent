import Image
import os

def calcularPromedio((x0,y0), ancho, alto, imagen):
    r, g, b = 0, 0, 0
    cantidad = 0
    for x in range(x0, x0+ancho):
        for y in range(y0, y0+alto):
            pixelR, pixelG, pixelB = imagen.getpixel((x,y))
            r += pixelR
            g += pixelG
            b += pixelB
            cantidad += 1
    return [(r/cantidad), (g/cantidad), (b/cantidad)]


def procesarPromedioDeImagen(imagen):
    ancho, alto = imagen.size
    promedios = []

    stepHorizontal = ancho/2
    stepVertical = alto/2
    for offsetHorizontal in range(0, ancho - 1, stepHorizontal):
        for offsetVertical in range(0, alto - 1, stepVertical):
            promedios.append(calcularPromedio( (offsetHorizontal,offsetVertical), stepHorizontal, stepVertical, imagen))
    return  promedios


archivoPromedios = open("promedios4D.txt", "w")
for archivoImagen in os.listdir('./images'):
    promedios = procesarPromedioDeImagen(  Image.open("images/" + archivoImagen).convert('RGB'))
    archivoPromedios.write(archivoImagen)
    for promedio in promedios:
        archivoPromedios.write(" " + str(promedio[0]) + " " + str(promedio[1]) + " " + str(promedio[2]))
    archivoPromedios.write("\n")
archivoPromedios.close()
