import images
import math

def vignetta(img_in, radius: int, strenght: float):
    img = images.load(img_in)

    x_center = len(img)//2
    y_center = len(img[0])//2

    for y in range(len(img)):
        for x in range(len(img[0])):

            distance_from_center = (math.sqrt((x_center - x)**2 + (y_center - y)**2))/radius

            r, g, b = img[y][x]

            g = int(g * (1 - distance_from_center * strenght))
            r = int(r * (1 - distance_from_center * strenght))
            b = int(b * (1 - distance_from_center * strenght))

            r = max(0, r)
            g = max(0, g)
            b = max(0, b)

            img[y][x] = (r, g, b)

    images.save(img, "output.png")


vignetta("img1.png", 120, 0.4)