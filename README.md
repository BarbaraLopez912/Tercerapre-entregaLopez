# VolcanesChile

Una aplicación Django que proporciona datos sobre volcanes en Chile, incluyendo información sobre los propios volcanes, además de los productos y erupciones volcánicas más comunes. 

## Requisitos

- Python 3.11
- Django

## Instalación

- Clona el repositorio: 'git clone https://github.com/BarbaraLopez912/Tercerapre-entregaLopez.git'.
- Entra al directorio raíz del proyecto.
- Crea y activa un entorio virtual.
- Ejecuta las migraciones: 'python manage.py migrate'
- Inicia el servidor: 'python manage.py runserver'

## Uso

1. Accede a la aplicación desde tu navegador: 'http://127.0.0.1:8000/'
2. Echa un vistazo a la página principal (VolcanesChile), hay varios datos interesantes sobre Volcanes de Chile.
3. En la barra de navegación puedes encontrar las opciones:
    * Lista de Volcanes: Te llevará a una lista de algunos de los Volcanes de Chile y su Región respectiva.
      Justo arriba de la lista tendrás a tu disposición una barra de búsqueda, donde puedes buscar Volcanes de Chile según la Región que indiques.
    * Agrega un volcán: En esta sección podrás registrar un nuevo volcán, del cual deberás indicar el nombre y la Región. Así mismo con las secciones Agregar producto y Agregar Clasificación.
    * Tipos de erupción volcánica: Aquí podrás ver una lista de los tipos más comunes de erupciones volcánicas.
    * Productos volcánicos: Te llevará a una lista de los productos volcánicos más comunes de una erupción volcánica.

## Archivos

- templates: En esta carpeta se encuentran todos los archivos .html que tienen las plantillas utilizadas en el proyecto. En la carpeta "sections" se encuentra una sección de la plantilla base ("base.html") llamada navigation.html, en la que se configuró la barra de navegación. En la carpeta "VolcanesChile" se encuentran aquellas plantillas específicas de cada función (vista) del proyecto.
- TerceraPreentrega: Aquí se encuentran los archivos base del proyecto django creado originalmente. Contiene las configuraciones respectivas y las url básicas (app y admin)
- VolcanesChile: Contiene los archivos propios de la aplicación. Aquí se encuentran las vistas creadas (views.py), las url utilizadas (urls.py), los registros del panel administrativo (admin.py), los formularios y modelos creados (forms.py, models.py), entre otros.
- db.sqlite3: base de datos con los modelos creados y sus objetos.
- manage.py: script de gestión del proyecto.
