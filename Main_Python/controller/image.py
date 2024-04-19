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


def get_masks_color(frame):
    """
    Image -> List * int
    Permet de reccuperer les masks de l'image apres applications de la selection des couleurs ainsi que le nombre de masks non vides
    """
    masks = []

    # On transforme l'image en hvs
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Le nombre de masks non vides
    number = 0

    # On boucle sur les quatre couleurs
    for i in range(4):

        # On reccuper les conditions de la couleur i
        _, hsv_lower, hsv_upper = color_profiles(i)

        # On selectionne les pixels qui verifie les conditions
        mask = cv2.inRange(hsv, hsv_lower, hsv_upper)

        # On netoie un peu le mask
        mask = cv2.erode(mask, None, iterations=4)
        mask = cv2.dilate(mask, None, iterations=4)

        # On chercher toutes les formes detecter
        elements, _ = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Si on a trouver au moins element, donc le mask n'est pas vide on increment le nombre
        if len(elements) > 0:
            number += 1

        # On ajoute le mask obtenu
        masks.append(mask)

    return masks, number
