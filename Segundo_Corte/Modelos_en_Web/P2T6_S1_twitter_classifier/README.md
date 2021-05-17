# Publicar un modelo IA en un Cloud (PythonAnyWhere)

## Configurar database SQLite

Primero se va a crear una base de datos en SQLite llamado ```tweets.sqlite``` dentro del directorio de ```P2T6_S1_twitter_classifier``` y almacenara 2 oraciones de prueba, acompañados del sentimiento que representa.

Es importante recordar cuales son los valores asignados a dichos sentimientos:

|Sentimiento|Valor|
|-----------|-----|
|Positivo|1|
|Negativo|2|
|Sin sentimientos|-1|
|Neutro|0|

Para crear dicha base de datos, usamos un script ubicado y llamado ```config/make_database_sqlite.py```.

## Archivos serializados

El modelo usado para hacer el análisis de sentimientos fue elaborado en Colab, [Procesamiento de Lenguaje Natural | Análisis de Sentimientos con Twitter (es)](https://github.com/carlos-paezf/Deep_Learning/blob/master/Segundo_Corte/P2T3_PLN.ipynb). Dichos serializables pasaran a ser parte de nuestro proyecto de Flask dentro del directorio de ```pkl_objects```

## El archivo vectorizer.py

Este archivo nos permite convertir las palabras o cualquier texto en un vector, donde cada elemento es una palabra o un símbolo gramatical, para luego reemplazarlas, analizarlas o demás, dependiendo el caso, como por ejemplo eliminar los emoticones o símbolos totalmente innecesario que pueden solo entorpercer el análisis de nuestro algoritmo.


## Comprender del archivo flask_app.py

Lo primero es llamar las librerías que se van a usar, de parte de Flask, tenemos Flask, render_template y request; para los formularios se hace uso wtforms, para el manejo de directorios y archivos tenenmos a pickle, la cual va de la mano con os para acceder al sistema operativo, y por ultimo tenemos a numpy para el manejo especializado de vectores o arreglos. Teniendo en cuenta que ya tenemos nuestro archivo ```vectorizer.py```, vamos a hacer uso de de la variable ```vect```, es cual crea un objeto de *HashingVectorizer*.

Luego vamos a deserializar el clasificador de regresión logística, es decir, el archivo ```classifier.pkl```. Su funcionalidad se explicó brevemente en la sección anterior.

La función *classify(document)* permite que se le ingrese un texto, y posteriormente retorne una etiqueta de clase según el sentimiento que se predice. La función de *train(document)* permite actualizar el clasificador con las nuevas entradas dependiendo de si la etiqueta dada fue correcta o no. 

La función *sql_entry(path, document, y)*, se usa para guardas las entradas que cargan los usuarios desde la página web. La función *sqlite_select(path)*, nos permite visualizar los tweets que se han clasificado y han permitido reentrenar el modelo de IA. 

Existe una clase llamada *ReviewForm* que instancia un TextAreaField para renderizar en el archivo ```reviewform.html```, el cual es la página de inicio de nuestra aplicación. Dicho archivo se renderiza por medio de la función *index()*. La función *sqlite_report()* permite consultar la base de datos de sqlite y mostrar la información en pantalla. 

La función *results()*, toma el contenido del formulario y lo pasa al clasificador para predicir el sentimiento y despues mostrarlo en ```results.html```. La función *feedback()*, toma la apreciación correto o incorrecto, y vuelve a transformar el sentimiento predicho, y vuelve a entrenar. 

## teewtform.html

Se puede considerar como la página index de nuestra aplicación. Es importante que el directorio que contenga los archivos html, se llame ```templates```. Dentro de esta plantilla, importamos a ```_formhelpers.html```, el cual se usa para renderizar el TextAreaField, donde el usuario proporcionara la crítica. Cuando se da click a *Evaluar tweet* nos redirige a la pagina de ```result.html```

## result.html

En esta plantilla tenemos 2 secciones, la primera nos muestra el resultado que se obtiene de tweet según lo clasificado por el modelo de IA. Y la segunda parte representa la opción de clasificar si el modelo de IA hizo bien o no su trabajo, y si lo último es el caso, entonces el usuario puede reentrenar el modelo para apoyo del creador. 