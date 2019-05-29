# Kinetic Energy V2 con animacion

## Clase ReadFile.py
### Métodos:
Leer archivo, donde recibe todas las columnas del archivo como importación, con auxilio de la biblioteca pandas el archivo csv y devolver los valores.

## Clase Skeleton.py
### Métodos:
Get skeleton joints: se obtienen los datos de articulación, a través del método de la clase anterior

Geet Time: con ayuda de la biblioteca datetime se obtienen los datos necesarios referente a tiempo

Get Mass: de 0 a 15 en una lista si reciben los valores de posiciones para devolver el valor de masa

Get kinetic energy: método responsable por datos referentes a la energía cinetica generada para obtener datos de distacia y velocidad

Get calories: devuelve valores de calorías basados en los datos disponibles en https://www.zonadiet.com/nutricion/energia.htm

## Clase animation.py
### Métodos:
Animate: se obtiene el archivo con los datos y las instancias en una lista, repasando para cada variable la posición de acuerdo con la parte del cuerpo que hace el movimiento, lo mismo ocurre con los huesos, para entonces generar la animación y presentar los datos finales de energía cinética: Joules y Energía calorica

## Clase FinalProyect.py
Clase de ejecución del proyecto, compuesta por un array, la importación del archivo, y la clase responsable de la animación con todos sus métodos