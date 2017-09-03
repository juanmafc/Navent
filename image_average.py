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


def procesarPromedioDeImagen(archivoImagen):
    imagen = Image.open(archivoImagen).convert('RGB')
    ancho, alto = imagen.size
    return calcularPromedio((0,0), ancho, alto, imagen)


archivoPromedios = open("promedios.txt", "w")
for archivoImagen in os.listdir('./images'):
    promedio = procesarPromedioDeImagen("images/" + archivoImagen)
    archivoPromedios.write(archivoImagen + " " + str(promedio[0]) + " " + str(promedio[1]) + " " + str(promedio[2]) + "\n")
archivoPromedios.close()
