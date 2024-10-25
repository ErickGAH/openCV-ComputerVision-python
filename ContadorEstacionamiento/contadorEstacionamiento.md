# <font style="color:rgb(50,120,229)"> Contador de lugares de estacionamiento </font>

En este proyecto vas a utilizar las técnicas de procesamiento de imágenes binarias para contar los lugares de estacionamiento ocupados y libres en un estacionamiento.

El funcionamiento del sistema es el siguiente:

1. El archivo `main.py` cuenta con algunas cajas de estacionamiento guardadas, puedes utilizar estas cajas para probar tu programa.
2. Debes de procesar cada caja de manera individual para determinar si está ocupada o no.
3. Si el lugar de estacionamiento está ocupado, debes de dibujar un rectángulo de color rojo alrededor de la caja.
4. Si el lugar de estacionamiento está libre, debes de dibujar un rectángulo de color verde alrededor de la caja.
5. En la parte superior de la imagen debes de mostrar el número de lugares de estacionamiento ocupados y libres.
6. El video de ejemplo se encuentra en la carpeta `data`.

Te dejo un par de imágenes de ejemplo para que te des una idea de como obtener los resultados:

<center>
    <figure>
        <img src="./output.png" width="400"/>
        <figcaption> Resultados procesamiento </figcaption>
    </figure>
</center>

<center>
    <figure>
        <img src="./output2.png" width="400"/>
        <figcaption> Resultado Final </figcaption>
    </figure>
</center>

## <font style="color:rgb(50,120,229)"> Funciones útiles </font>

- Contar pixeles blancos en una imagen binaria:

    ```python
    num_pixeles_blancos = cv2.countNonZero(imagen_binaria)
    ```

- Convertir una imagen a escala de grises:

    ```python
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    ```

## <font style="color:rgb(50,120,229)"> Bonus </font>

Si quieres un reto extra, puedes intentar agregar al sistema la capacidad de seleccionar las cajas de estacionamiento manualmente dibujando un rectángulo alrededor de cada lugar de estacionamiento.