import images

def disegna_parabola(n):
    """
    Disegna la parabola y = x^2 su un'immagine n x n, centrata nel punto (n//2, n//2).

    :param n: La dimensione dell'immagine quadrata.
    """

    img = [[(0, 0, 0) for _ in range(n)] for _ in range(n)]

    cx = cy = n // 2

    for x in range(-cx, cx + 1):
        y = x**2
        if 0 < cy - y < n:
            img[cy - y][cx - x] = (255, 255, 255)

    images.save(img, "output.png")

disegna_parabola(300)