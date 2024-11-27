import images
import math

def calcola_pixel_ovale(centro, semiassi, image_dimention):
    """
    Calcola i pixel da colorare per disegnare un ovale.

    :param centro: Tupla (cx, cy) con le coordinate del centro dell'ovale.
    :param semiassi: Tupla (a, b) con la lunghezza dei semiassi (orizzontale, verticale).
    :param image_dimention: Intero che determina la dimensione n*n dell'immagine
    :return: Una lista di tuple (x, y) con le coordinate dei pixel da colorare.
    """

    img = [[(0, 0, 0) for _ in range(image_dimention)] for _ in range(image_dimention)]

    for y in range(len(img)):
        for x in range(len(img[0])):
            formula_ovale = (((x - centro[0])**2) / ((semiassi[0]**2)) + ((y - centro[1])**2) / (semiassi[1]**2))
            if formula_ovale <= 1:
                img[y][x] = (255, 255, 255)

    images.save(img, "output.png")

# Parametri del test
centro = (1000, 1000)  # Centro dell'ovale
semiassi = (343, 200)  # Semiassi: 3 orizzontali, 2 verticali

# Calcola i pixel da colorare
calcola_pixel_ovale(centro, semiassi, 2000)