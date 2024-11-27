import images
import math

# creare una funzione ricevente in input una immagine con all'interno un cerchio, in grado di trovare le coordinate del centro e il suo raggio:
# ritornare una tupla, con le coord e il raggio -> [(y, x), r]

def find_center(ys, xs, image):
    # Trova il centro orizzontale
    x_left = xs
    while image[ys][x_left] == (255, 255, 255) and x_left > 0:
        x_left -= 1
    x_right = xs
    while image[ys][x_right] == (255, 255, 255) and x_right < len(image[0]) - 1:
        x_right += 1
    c_x = (x_left + x_right) // 2

    # Trova il centro verticale
    y_top = ys
    while image[y_top][xs] == (255, 255, 255) and y_top > 0:
        y_top -= 1
    y_bottom = ys
    while image[y_bottom][xs] == (255, 255, 255) and y_bottom < len(image) - 1:
        y_bottom += 1
    c_y = (y_top + y_bottom) // 2

    return c_y, c_x


def find_radius(yc, xc, image):
    radius = 0
    # Controlla la distanza fino al bordo in tutte le direzioni
    while image[yc][xc] == (255, 255, 255):
       yc += 1
       radius += 1
    return radius - 1



def delete_circle(xc, yc, radius, image):
    for y in range(len(image)):
         for x in range(len(image[0])):
            distance = math.sqrt((x - xc) ** 2 + (y - yc) ** 2)
            if distance <= radius:
                image[y][x] = (0, 0, 0)



def find_circle(in_img):
    # cicliamo sull'immagine e appena troviamo un pixel
    # a partire da quel pixel, spostarsi verso destra per trovare la larghezza e poi il punto medio della larghezza
    # ora fare lo stesso sull'asse verticale per trovare il punto medio della larghezza
    # abbiamo cosi' trovato il punto centrale del cerchio e possiamo salvarci le sue coordinate
    # a questo punto spostarci verso una posizione qualunque per trovare il pixel piu' lontano appartenente al cerchio e con un contatore tenere traccia del raggio
    # ritornare il tutto

    img = images.load(in_img)

    coord = []

    for y in range(len(img)):
        for x in range(len(img[0])):
            if img[y][x] == (255, 255, 255):
                y_center, x_center = find_center(y, x, img)
                coord.append((y_center, x_center))

                r = find_radius(y_center, x_center, img)
                delete_circle(y_center, x_center, r, img)
                coord.append(r)
    return coord

print(find_circle("test1.png"))
