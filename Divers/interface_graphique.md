
# CHOIX D'INTERFACE GRAPHIQUE**


## Pygame

AVANTAGES:
- Libre et Open Source.
- Basé sur la bibliothèque SDL, offrant des fonctionnalités de mathématiques vectorielles, détection de collision, gestion de sprite 2D, manipulation de matrices de pixels.
- Communauté active.
- Multiplateforme (PC, smartphones, etc.).
- Adapté à la 2D, avec la possibilité de faire de la 3D.
- Membres de l'équipe déjà familiers avec Pygame.

INCONVÉNIENTS:
- Performances limitées, notamment pour la 3D.
- Manque d'outils de développement avancés prêts à l'emploi.

---

## Kivy

AVANTAGES:
- Libre et Open Source.
- Sous licence MIT.
- Déploiement possible sur Windows, Mac, Linux, et Raspberry Pi.
- Grande variété de widgets personnalisables.
- Combinaison possible avec d'autres bibliothèques Python.

INCONVÉNIENTS:
- Optimisé pour les applications mobiles.
- Courbe d'apprentissage difficile.
- Performances limitées.
- Applications Kivy peuvent avoir une taille plus importante.

---

## Tkinter

AVANTAGES:
- Aucun besoin d'installer des packages, l'importation via une commande suffit.
- Multiplateforme.
- Processus de liaison.
- Fonctionne avec des bibliothèques scientifiques (NumPy, Pandas, Matplotlib, etc.).
- Léger et facile d'utilisation.
- Quantité raisonnable de widgets.
- Documentation complète.
- Communauté active.

INCONVÉNIENTS:
- Vitesse d'exécution.
- Limitation graphique.
- Widgets moins esthétiques.
- Personnalisation limitée.
- Pas de possibilité de faire de la 3D.

---

## PyQt

AVANTAGES:
- Compatible avec Linux, Windows, Mac, et Android.
- Contient environ 440 classes et 6000 fonctions et méthodes.
- Logiciel libre et Open Source.
- Prise en charge 2D et 3D.
- QT Designer simplifie la création d'interfaces graphiques.
- Performances élevées.
- Documentation complète.

INCONVÉNIENTS:
- Difficile à prendre en main.
- Taille de l'application.
- Parfois payant.
- Aspect visuel des widgets peut être amélioré.

---

## PyForms

AVANTAGES:
- Open Source.
- Définition facile d'interfaces.
- Apprentissage facile.
- Code organisé en modules.
- Conception axée sur la simplicité pour un développement rapide.
- Widgets interactifs prêts à l'emploi.
- Extension de widgets.
- Grande documentation.

INCONVÉNIENTS:
- Uniquement disponible pour Python 3.
- Petite communauté.
- Limitations de certaines fonctionnalités.
- Possibilités de personnalisation plus limitées par rapport à d'autres frameworks.

---

## Pyglet

AVANTAGES:
- Prise en charge de la 3D grâce à OpenGL.
- Facile d'utilisation.
- Indépendant de bibliothèques externes.
- Multithreading intégré.
- Open Source.

INCONVÉNIENTS:
- Documentation moins complète.
- Manque de fonctionnalités graphiques avancées.
- Taille de la communauté.
- Documentation moins étendue.
- Support 3D limité.

---

# Conclusion:

Après réflexion, nous avons hésité entre trois interfaces graphiques : Pygame, Kivy, et Tkinter. En raison des limitations de performance de Kivy, surtout pour des applications non mobiles, et de sa possible lourdeur, nous avons écarté cette option. Le choix s'est ensuite porté entre Pygame et Tkinter.

Bien que Tkinter soit facile à utiliser, multiplateforme et ne nécessite pas l'installation de packages, ses limitations en termes de vitesse d'exécution et d'absence de support 3D ont conduit à notre préférence pour Pygame. De plus, certains membres de notre équipe ont déjà des connaissances préalables en Pygame, facilitant ainsi l'apprentissage pour ceux qui ne sont pas familiers avec cette interface graphique.

En conclusion, nous avons choisi Pygame pour la réalisation de la simulation de notre projet de robotique.