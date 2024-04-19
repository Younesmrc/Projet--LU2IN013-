import cv2
def color_profiles(n):
    """  Fonction qui retourne les condition des couleurs """
    if n == 0:
        name = "Bleu"
        hsv_lower = (95, 100, 20)
        hsv_upper = (115, 255, 255)
        return (name, hsv_lower, hsv_upper)

    if n == 1:
        name = "Rouge"
        hsv_lower = (0, 100, 50)
        hsv_upper = (10, 255, 255)
        return (name, hsv_lower, hsv_upper)

    if n == 2:
        name = "Vert"
        hsv_lower = (50, 50, 20)
        hsv_upper = (100, 255, 255)
        return (name, hsv_lower, hsv_upper)

    if n == 3:
        name = "Jaune"
        hsv_lower = (10, 100, 50)
        hsv_upper = (50, 255, 255)
        return (name, hsv_lower, hsv_upper)
