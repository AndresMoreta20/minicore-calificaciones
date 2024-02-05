
# Sistema de Cálculo de Calificaciones

Este proyecto es un mini-sistema MVC (Modelo-Vista-Controlador) desarrollado con Django, diseñado para calcular calificaciones por fechas y determinar la calificación necesaria que un estudiante necesita obtener en el último parcial para pasar el semestre con una nota mínima de 6. Es útil para educadores y estudiantes que buscan monitorear y proyectar el rendimiento académico a lo largo del semestre.

## Comenzando

Sigue estas instrucciones para obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### Prerrequisitos

Necesitarás Python y Django instalados en tu entorno. Asegúrate de tener las siguientes versiones o superiores:

```
Python 3.8
Django 3.2
```

### Instalación

Clona el repositorio a tu máquina local:

```
git clone https://tu-repositorio-aqui.git
```

Instala las dependencias necesarias:

```
pip install -r requirements.txt
```

Realiza las migraciones necesarias para preparar tu base de datos:

```
python manage.py migrate
```

Inicia el servidor de desarrollo:

```
python manage.py runserver
```

Ahora puedes acceder a la aplicación en `http://localhost:8000`.

## Ejecutando las pruebas

Para ejecutar las pruebas automatizadas y asegurar que todo funciona correctamente:

```
python manage.py test
```

### Desglose en pruebas end to end

Las pruebas end to end aseguran que el flujo de cálculo de calificaciones y proyección de notas funcione de principio a fin.

```
python manage.py test app.tests.EndToEndTests
```

### Y pruebas de estilo de codificación

Utiliza herramientas como flake8 para mantener la calidad y consistencia del código:

```
flake8
```

## Despliegue

Para desplegar este proyecto en un entorno de producción, sigue las instrucciones específicas de tu proveedor de hosting sobre la implementación de aplicaciones Django.

## Construido con

* [Django](https://www.djangoproject.com/) - El framework web usado para implementar el patrón MVC.

## Contribuyendo

Si deseas contribuir a este proyecto, por favor envía un pull request con tus mejoras, siguiendo las buenas prácticas de desarrollo y documentación de código.

## Versionado

Utilizamos [SemVer](http://semver.org/) para el versionado. Para las versiones disponibles, visita los [tags de este repositorio](https://tu-repositorio-aqui/tags).

## Autores

* **Tu Nombre** - *Desarrollo inicial* - [TuUsuario](https://github.com/TuUsuario)

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - mira el archivo [LICENSE.md](LICENSE.md) para más detalles.

## Agradecimientos

* A todos los que contribuyeron al proyecto.
* Inspiración.
* Cualquiera que haya dedicado tiempo a ayudar con el desarrollo y las pruebas.
