import images

# disegna una ragnatela
def draw_lines(image):
    midx = len(image)//2
    midy = len(image[0])//2

    for x in range(len(image)):
        image[midy][x] = (255, 255, 255)
    for y in range(len(image[0])):
        image[y][midx] = (255, 255, 255)

    for y in range(len(image)):
        for x in range(len(image[0])):
            if y == x:
                image[y][x] = (255, 255, 255)
            if y == len(image) - 1 - x:
                image[y][x] = (255, 255, 255)

def draw_squares(xs, ys, lenght, image):
    for x in range(xs, xs + lenght):
        image[ys][x] = (255, 255, 255)
        image[ys + lenght -1][x] = (255, 255, 255)
    for y in range(ys, ys + lenght):
        image[y][xs] = (255, 255, 255)
        image[y][xs + lenght - 1] = (255, 255, 255)


def disegna_ragnatela(dimention, passo):
    img = [[(0, 0, 0) for _ in range(dimention)] for _ in range(dimention)]

    lunghezza = dimention
    for x in range(0, dimention//2, passo):
        draw_squares(x, x, lunghezza - x, img)
        lunghezza -= passo

    draw_lines(img)

    images.save(img, "output.png")

disegna_ragnatela(51, 4)