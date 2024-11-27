import images
import png
import io



# %% PER CASA: Dati i rettangoli definiti nella lista list_rect
# calcolarsi il rettangolo R di area minima che li racchiude tutti
# e disegnare R con colore (255,255,255) usando la funzione sopra fill_rect.
# Poi successivamente disegnare i rettangoli nella list_rect sempre usando
# fill_rect
# I rettangoli sono in formato
# pixel top left= (x1,y1) e bottom right (x2,y2) e
# c e' il colore come tupla rgb
# rettangolo (1,1,20,19,(255, 0, 0)) indica il rettangolo che parte dal punto
# in alto a sx (1,1) e termina a (20,19) compreso di colore rosso ossia
# (255, 0, 0).
# rettangolo = (x1,y1,x2,y2,c)
# provate a disegnare nell ordine suddetto in un un' immagine
# tutte nera con 300 colonne e 300 righe.
list_rect = [(210, 210, 210, 210 ,(255, 0, 0)),
             (50, 100, 100, 200, (255, 255, 0)),
             (220, 50, 250, 99, (255, 0, 255)),
             (150, 80, 150, 190, (0, 128, 0))
             ]


#mi creo una funzione in grado di disegnare un quadrilatero a partire dalle sue coordinate in alto a sinistra e in basso a destra
def draw_rectangle(xl, yl, xr, yr, color: tuple):
    for row in range(yl, yr + 1):
        for column in range(xl, xr + 1):
            img[row][column] = color

#creo un'immagine, un colorgrade per i colori da usare e imposto il rettangolo che copre gli altri
img = [[(0, 0, 0) for _ in range(300)] for _ in range(300)]
colorgrade = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (123, 0, 255)]
rect_filler = [300, 300, 0, 0]

#mi calcolo gli spigoli maggiori del quadrilatero esterno agli altri
for rect in list_rect:
    rect_filler[0] = min(rect_filler[0], rect[0])
    rect_filler[1] = min(rect_filler[1], rect[1])
    rect_filler[2] = max(rect_filler[2], rect[2])
    rect_filler[3] = max(rect_filler[3], rect[3])

#mi disegno il quadrilatero piu' esterno
draw_rectangle(rect_filler[1], rect_filler[0], rect_filler[3], rect_filler[2], (255, 255, 255))

#mi disegno i 4 quadrilateri rimanenti
for index, rect in enumerate(list_rect):
    draw_rectangle(rect[1], rect[0], rect[3], rect[2], colorgrade[index])

images.save(img, "test.png")



# %% PER CASA: cambiare il codice di prima in maniera che crei
# una classe per i rettangoli e per i colori e usi oggetti nella sua esecuzione.




# %% PER CASA: Per i piu coraggiosi ed esperti. scrivere la funzione
#di prima che disegna (senza classi va bene) SENZA cicli ma solo usando
# map, zip, lambda etc

#creo un'immagine, un colorgrade per i colori da usare e imposto il rettangolo che copre gli altri
img = [[(0, 0, 0) for _ in range(300)] for _ in range(300)]
colorgrade = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (123, 0, 255)]
rect_filler = [300, 300, 0, 0]

# Trovo i confini del quadrilatero esterno
for rect in list_rect:
    rect_filler[0] = min(rect_filler[0], rect[0])
    rect_filler[1] = min(rect_filler[1], rect[1])
    rect_filler[2] = max(rect_filler[2], rect[2])
    rect_filler[3] = max(rect_filler[3], rect[3])

# Disegno il quadrilatero esterno
draw_rectangle(rect_filler[1], rect_filler[0], rect_filler[3], rect_filler[2], (255, 255, 255))

# Usa map con una lambda per disegnare i rettangoli con i colori corrispondenti
list(map(lambda index_rect: draw_rectangle(index_rect[1][1], index_rect[1][0], index_rect[1][3], index_rect[1][2], colorgrade[index_rect[0]]), enumerate(list_rect)))

# Salvo l'immagine
images.save(img, "test.png")
