# Publicar un modelo en Cloud

Cuando hemos serializado un modelo de IA, queremos mostrarlo y que otras personas tambien hagan uso de él. Pero primero debemos escoger en cual plataforma lanzarlo. En este caso, hacemos uso de Heroku o de PythonAnywhere.

## Lanzamiento en PythonAnywhere

Lo primero es crear una cuenta en dicha plataforma, posteriormente, dentro del *Dashboard*, ingresar a la sección de *Web apps*, allí le damos a *Add a new web app* y escogemos como Framework de Python Web a *Flask*, ya que será el que vamos utilizar para aprender a desplegar los modelos. Luego seleccionamos *Python 3.7* y con esto podremos subir nuestro proyecto.

Ahora bien, allí dentro vamos a la sección de *Code* y en el item de *Working directory* optamos por *Go to directory*.

Dentro de esta pestaña, en el menú de directorios, ingresamos al directorio llamado *mysite/*, y en el menú de Files, añadimos nuestro archivo *flask_app.py*, si tenemos directorios para nuestro proyecto, los creamos desde el menú de *Directories* y añadimos los archivos allí.

De regreso al menú de *Web apps*, pulsamos al boton de *Reload <nombre-user>.pythonanywhere.com* y podremos ingresar a dicha url para ver nuestros archivos.
