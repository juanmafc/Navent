import Image

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
    return ((r/cantidad), (g/cantidad), (b/cantidad))



imagen = Image.open('test.png').convert('RGB')
ancho, alto = imagen.size
r, g, b = calcularPromedio((0,0), ancho, alto, imagen)

archivoPromedios = open("promedios.txt", "w")
archivoPromedios.write("archivoname " + str(r) + " " + str(g) + " " + str(b) + "\n")
archivoPromedios.close()
