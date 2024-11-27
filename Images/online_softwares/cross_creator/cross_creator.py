import images

#definisci una funzione in grado di costruire delle croci all'interno del tuo testo
#in input ti verranno fornite delle liste con all'interno delle lista che contengono
#la coordinata di centro della croce e il suo "raggio"


#funzione che disegna una croce
def cross_creator(x_center, y_center, lenght, image):
    for x in range(x_center - lenght, x_center + lenght + 1):
        if 0 <= x <= 300:
            image[y_center][x] = (255, 255, 255)
    for y in range(y_center - lenght, y_center + lenght + 1):
        if 0 <= y <= 300:
            image[y][x_center] = (255, 255, 255)

def ex1(croci, image):
    for croce in croci:
        if 0 <= croce[0] < 300 and 0 <= croce[1] < 300:
            cross_creator(croce[0], croce[1], croce[2], image)

    images.save(image, "prova.png")


croci = [
    [22, 23, 5], [200, 129, 8], [10, 10, 15], [50, 50, 3], [120, 150, 6],
    [200, 250, 4], [75, 100, 10], [300, 20, 7], [250, 200, 5], [60, 70, 4],
    [180, 120, 5], [130, 180, 8], [90, 40, 12], [210, 80, 6], [15, 250, 10],
    [140, 90, 3], [60, 250, 7], [220, 150, 9], [180, 200, 7], [30, 100, 4],

    # Aggiungo croci che si toccano
    [100, 60, 5], [120, 60, 5],  # Croci che si toccano orizzontalmente
    [50, 150, 6], [50, 156, 6],  # Croci che si toccano verticalmente
    [200, 100, 4], [204, 100, 4],  # Croci che si toccano orizzontalmente
    [250, 150, 6], [250, 156, 6]  # Croci che si toccano verticalmente
]

img = [[(0,0,0) for _ in range(300)] for _ in range(300)]

ex1(croci, img)