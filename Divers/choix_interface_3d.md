## Choix d'interface 3D :

### Introduction

Pour progresser dans notre projet, nous avons besoin d'une interface graphique 3D pour simuler la caméra du robot. Cela permettra une représentation visuelle immersive de l'environnement, facilitant le suivi d'une balise. En utilisant cette interface, nous pouvons améliorer la précision et la fiabilité du système de navigation. Nous devons évaluer plusieurs interfaces graphiques pour choisir celle qui convient le mieux à nos besoins.

### Liste des interfaces 3D

- Panda3D
- VTK (Visualization Toolkit)
- Pyglet
- VisPy
- Kivy
- Ursina

### Avantages et inconvénients

### Panda3D :

<u>Avantages : </u>
- Puissant et flexible.
- Supporte Python et C++.
- Bonne documentation.
- Communauté active.
- Performances optimisées.

<u>Inconvénients : </u>
- Courbe d'apprentissage prononcée.
- Moins populaire que d'autres moteurs.
- Configuration initiale complexe.
- Documentation parfois obsolète.
- Moins de ressources en ligne que d'autres moteurs.

### VTK (Visualization Toolkit) :
<u>Avantages : </u>
- Large gamme de fonctionnalités.
- Performance optimisée.
- Documentation complète.

<u>Inconvénients : </u>
- Courbe d'apprentissage abrupte.
- Moins adapté aux applications non scientifiques.
- Moins de ressources en ligne.

#### VisPy :

<u>Avantages :</u>

- Accélération matérielle GPU pour un rendu rapide.
- Interface simple à utiliser avec Python.
- Communauté active.

<u>Inconvénients :</u>

- Documentation parfois insuffisante.
- Moins adapté à la modélisation 3D avancée.
- Possibilité de problèmes de performances.

#### Kivy :

<u>Avantages :</u>

- Multiplateforme.
- Langage Python facile à apprendre.
- Grande bibliothèque standard.
- Communauté active.

<u>Inconvénients :</u>

- Performances moins bonnes pour les applications graphiques intensives.
- Courbe d'apprentissage prononcée.
- Moins adapté à la personnalisation approfondie.
- Possibilité de limitations dans le style des widgets.
- Documentation parfois limitée.
- Se base sur OpenGL

#### Ursina :

<u>Avantages :</u>

- Simple à apprendre et à utiliser.
- Bon pour le prototypage rapide.
- Facile à créer des objets 3D et à les animer.
- Supporte la création d'interfaces utilisateur graphiques.
- Communauté active.

<u>Inconvénients :</u>

- Moins adapté aux applications professionnelles.
- Moins de fonctionnalités que des moteurs de jeu plus complets.
- Courbe d'apprentissage prononcée.
- Moins performant pour des jeux graphiquement intensifs.
- Moins de ressources disponibles.
- Incompatible avec Linux

### Choix + Conclusion :

En vue des avantages et inconvénients de chaque interface graphique pour la 3D, nous hésitons entre Panda3D et Ursina. Cependant, le fait qu'Ursina ne soit pas compatible avec Linux nous oriente plutôt vers Panda3D.

### Sources :

https://www.unite.ai/fr/10-meilleures-biblioth%C3%A8ques-Python-pour-l%27interface-graphique/

https://www.createursdemondes.fr/moteurs-de-jeux/apprendre-python-en-jouant-cest-facile-avec-panda3d/

https://www.kitware.fr/formation-exploration-de-donnees-avec-vtk/

https://pythonawesome.com/vispy-interactive-scientific-visualization-in-python/

https://blog.desdelinux.net/fr/framework-kivy-pour-python/

https://www.ursinaengine.org/

https://chat.openai.com/