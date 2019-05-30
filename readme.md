# Kinetic Energy V2 con animacion

## Clase ReadFile.py
### Métodos:
read, recibe como parametro un archivo csv, el cual con ayuda de la librería pandas, procesa las columnas deseeadas y el metodo regresa los valores en forma de lista.

## Clase Skeleton.py
### Métodos:
Get skeleton joints: se obtienen los datos de articulación, a través del método de la clase anterior

Get Time: con ayuda de la librería datetime se obtienen los datos necesarios referente a tiempo

Get Mass: de 0 a 15 en una lista se obtienen valores de masa calculados previemente por joint dependiendo la edad del pasciente en el csv e ejemplo.

Get kinetic energy: método responsable por datos referentes a la energía cinetica generada para obtener datos de distacia y velocidad

Get calories: devuelve valores de calorías basados en los datos disponibles en https://www.zonadiet.com/nutricion/energia.htm en cojunto a la referenccia de energía cinética calculada anteriormente.

## Clase animation.py
### Métodos:
Animate: se obtiene el archivo con los datos y las instancias en una lista, repasando para cada variable la posición de acuerdo con la parte del cuerpo que hace el movimiento, lo mismo ocurre con los huesos, para entonces generar la animación y presentar los datos finales de energía cinética: Joules y Energía calorica

## Clase FinalProyect.py
Clase de ejecución del proyecto, compuesta por un array, la importación del archivo, y la clase responsable de la animación con todos sus métodos