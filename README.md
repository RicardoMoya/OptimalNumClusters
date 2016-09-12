# Selección óptima de Clusters

Uno de los problemas que nos encontramos a la hora de aplicar alguno de los 
métodos de Clustering (K-means o EM) es la elección del número de Clusters. No 
existe un criterio objetivo ni ampliamente válido para la elección de un número
óptimo de Clusters; pero tenemos que tener en cuenta, que una mala elección de 
los mismos puede dar lugar a realizar agrupaciones de datos muy heterogéneos 
(pocos Clusters); o datos, que siendo muy similares unos a otros los agrupemos 
en Clusters diferentes (muchos Clusters).

Para saber más sobre la selección óptima del número de Clusters ir al siguiente
tutorial:

http://jarroba.com/seleccion-del-numero-optimo-clusters/


## Prerrequisitos

El código que se encuentra en este repositorio hace uso de las librerías de 
numpy, matplotlib y scipy. Para descargar e instalar (o actualizar a la última 
versión con la opción -U) estas librerías con el sistema de gestión de paquetes 
pip, se deben ejecutar los siguiente comandos:

```ssh
$ pip install -U numpy
$ pip install -U matplotlib
$ pip install -U scipy
```

## Elbow Method

Resultados:
![alt jarroba](http://jarroba.com/wp-content/uploads/2016/09/Elbow_ds1_2.png)
![alt jarroba](http://jarroba.com/wp-content/uploads/2016/09/Elbow_ds2_2.png)
![alt jarroba](http://jarroba.com/wp-content/uploads/2016/09/Elbow_ds3_2.png

## Dendogram

Resultados:
![alt jarroba](http://jarroba.com/wp-content/uploads/2016/09/Dendogram_ds1.png)
![alt jarroba](http://jarroba.com/wp-content/uploads/2016/09/Dendogram_ds2.png)
![alt jarroba](http://jarroba.com/wp-content/uploads/2016/09/Dendogram_ds3.png)

## Gap

Resultados:
![alt jarroba](http://jarroba.com/wp-content/uploads/2016/09/Gap_ds1.png)
![alt jarroba](http://jarroba.com/wp-content/uploads/2016/09/Gap_ds2.png)
![alt jarroba](http://jarroba.com/wp-content/uploads/2016/09/GAP_ds3.png)


Para más detalles del proyecto vista la web de jarroba.com:

![alt jarroba](http://jarroba.com/wp-content/themes/jarrobav6/static/img/logojarroba.png)
