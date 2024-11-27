# Ignorare le righe fino alla 31
from typing import Any, Callable, List, Tuple, Dict, Union
import sys
from unittest import result
import images
import math


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Esegue un test e controlla il risultato


def check_test(func: Callable, expected: Any, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        expected_str = repr(expected)
        test_outcome = "succeeded" if (result == expected) else "failed"
        color = bcolors.OKGREEN if (result == expected) else bcolors.FAIL
        print(f'{color}Test on {func_str} on input {args_str} {test_outcome}. Output: {result_str} Expected: {expected_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERROR: {func_str}({args_str}) => {error_str}')


# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola l'immagine corrispondente in scala di grigi.
# Per fare ciò, se R è il canale del rosso, G del verde, e B del blu, rimpiazzare ogni canale
# con il valore 0.2126*R + 0.7152*G + 0.0722*B.
# Attenzione: Il valore di ciascun canale deve essere un intero.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
def img_grayscale(img_in: str, img_out: str):
    img=images.load(img_in)
    img=[[[int(0.2126*R) + int(0.7152*G) + int(0.0722*B)]*3 for (R, G, B) in row] for row in img]
    images.save(img, img_out)


# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# ruota l'immagine (tenendo fisso il centro) di un certo numero di gradi centigradi
# specificato come parametro (theta).
# Per fare ciò, utilizzare la seguente formula:
#   - Se ruotiamo l'immagine di un angolo theta, il pixel che si trova alle coordinate (x, y),
#     nell'immagine ruotata si troverà alle coordinate (x*cos(theta) + y*sin(theta), -x*sin(theta) + y*cos(theta))
# Attenzione: controllare la documentazione per vedere cosa richiedono in input le funzioni
# math.sin e math.cos
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione (non vengono effettuati test automatici)
def img_rotate(img_in: str, theta: float, img_out: str):
    theta*=math.pi/180
    img=images.load(img_in)
    to_return = [[(0, 0, 0) for _ in range(len(img[0]))] for _ in range(len(img))]
    mid_x= len(img[0])//2
    mid_y= len(img)//2

    def to_xy(i, j):
        return i-mid_x, mid_y-j
    def to_ij(x, y):
        return x+mid_x, mid_y-y
    def rotate_xy(x, y):
        return int(x*math.cos(theta) + y*math.sin(theta)), int(-x*math.sin(theta) + y*math.cos(theta))
    for i in range(len(img)):
        for j in range(len(img[0])):
            x, y=to_xy(i, j)
            x1, y1 = rotate_xy(x, y)
            i1, j1 = to_ij(x1, y1)
            if 0<=i1<len(to_return) and 0<=j1<len(to_return[0]):
                to_return[i][j]=img[i1][j1]
    images.save(to_return, img_out)



# Definire una funzione che disegna un cerchio centrato in (x,y) e di raggio r,
# su una immagine presa in input e la ri-scrive in output.
# Per disegnare il cerchio, testiamo se un punto è all'interno del cerchio o no,
# guardando se la distanza dal center è <= raggio. Nel caso settiamo il colore c.
# Il centro di ogni pixel è translato di 0.5 rispetto agli indici dei pixels.
def img_circle(img_in: str, x: float, y: float, r: float, c: Tuple, img_out: str):
    img = images.load(img_in)
    for i in range(len(img)):
        for j in range(len(img[0])):
            d=math.sqrt(((i+.5)-x)**2+((j+.5)-y)**2)
            if d<=r:
                img[i][j]=c
    images.save(img, img_out)




# Definire una funzione che applica aggiunstamenti di colore ad una immagine.
# In particolare, applichiamo nel'ordine: (a) tinta, (b) contrasto, (c) saturazione.
# Per farlo, priam riportiamo i colori in [0,1] float, poi applichiamo gli updates,
# e poi torniamo in [0,255] intero.
# (a) tinta: pixel *= t
# (b) contrasto: pixel = (pixel - 0.5) * c + 0.5
# (c) saturazione: pixel = (pixel - gray(pixel)) * s + gray(pixel)
def img_colorgrade(img_in: str, t: tuple, c: float, s: float, img_out: str):
    img=images.load(img_in)
    def gray(R, G, B):
        return 0.2126*R + 0.7152*G + 0.0722*B

    for i in range(len(img)):
        for j in range(len(img[0])):
            img[i][j]= [(k/255*t[n]-.5)*c+.5 for n, k in enumerate(img[i][j])]
            g= gray(*img[i][j])
            img[i][j] = [max(0, min((255, int(((k - g) * s + g) * 255)))) for k in img[i][j]]
    images.save(img, img_out)

# Definire una funzione che crea un mosaico sui pixel di una immagine. Il mosaico
# ha celle di larghezza n. Per questo esercizio usiamo un colore del quadratino e
# non ci preoccupiamo di fare la media. Inoltre disegniamo anche delle linee nere
# intorno a ogni cella del mosaico.
def img_mosaic(img_in: str, n: int, img_out: str):
    img=images.load(img_in)
    to_return = [[None for _ in range(len(img[0]))] for _ in range(len(img))]
    for i in range(len(img)):
        for j in range(len(img[0])):
            to_return[i][j]= (0, 0, 0) if ((i%n==0) or (j%n==0)) else img[i//n*n][j//n*n]
    images.save(to_return, img_out)

# Test funzioni
img_grayscale("img1.png", "img1_grayscale_ms.png")
for angle in [-30, 15, 30, 45, 480, -500]:
    img_rotate("img1.png", angle, "img1_rotated_" + str(angle) + "_ms.png")
img_circle("img1.png", 150, 150, 50, (255, 255, 0), "img1_circle_ms.png")
img_colorgrade("img1.png", (0.95, 1.0, 0.95), 1, 1, "img_colorgrade1_ms.png")
img_colorgrade("img1.png", (1.0, 1.0, 1.0), 2, 1, "img_colorgrade2_ms.png")
img_colorgrade("img1.png", (1.0, 1.0, 1.0), 1, 2, "img_colorgrade3_ms.png")
img_colorgrade("img1.png", (0.9, 1.0, 0.9), 2, 0.7, "img_colorgrade4_ms.png")
img_mosaic("img1.png", 16, "img_mosaic_ms.png")
