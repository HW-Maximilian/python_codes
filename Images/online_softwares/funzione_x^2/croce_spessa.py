import images

def disegna_funzione(n):
    """
    Disegna la parabola y = x^2 su un'immagine n x n, centrata nel punto (n//2, n//2).

    :param n: La dimensione dell'immagine quadrata.
    """

    img = [[(0, 0, 0) for _ in range(n)] for _ in range(n)]

    cx = cy = n // 2

    for x in range(-cx, cx + 1):
        y = x + 20
        y2 = x - 20

        for value in range(y2, y + 1):
            if 0 < cy - value < n and 0 < cx - x < n:
                img[cy - value][cx - x] = (255, 255, 255)

        for value in range(y2, y + 1):
            if 0 < cy - value < n and 0 < cx - x < n:
                img[cy - value][x - cx] = (255, 255, 255)


    images.save(img, "output.png")

disegna_funzione(300)