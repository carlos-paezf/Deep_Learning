# Guía rapida

Esta el la primera aplicación que creo con Flask, por lo tanto agrego los comandos que use para ejecutarlos desde un pc con Windows 10.

## Instalación de Flask

Abrí una terminal de comandos en modo administrador e ingresé el comando:
```
pip install Flask
```

## Ejecutar el proyecto

Primero se debe extraer el proyecto con este comando:
```
set FLASK_APP=flask_app.py
```

Y luego para desplegarlo escribí:
```
python -m flask_app run
```

Para hacer el despliegue en pythonanywhere.com, es importante que el archivo principal se llame flask_app.py, de lo contrario se generan errores.
