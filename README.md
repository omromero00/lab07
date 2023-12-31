# INFORME DE LABORATORIO 07
<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AUGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
                  </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía del Estudiante / Talleres / Centros de Simulación</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2023/06/08</td><td><span style="font-weight:bold;">Código</span>: GUIA</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">GUÍA DEL ESTUDIANTE</span><br />
<span>(formato del estudiante)</span>
</div>


<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Laboratorio 07</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>07</td><td>AÑO LECTIVO:</td><td>2023 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>
<tr>
<td>FECHA INICIO::</td><td>JUL-2023</td><td>FECHA FIN:</td><td>JUL-2023</td><td>DURACIÓN:</td><td>04 horas</td>
</tr>
<tr><td colspan="6">INTEGRANTE:
<ul>
<li>ROMERO CHIPANA OMAR -------------------- oromero@unsa.edu.pe</li>
</ul>
</td>
</<tr>
<tr><td colspan="6">DOCENTE:
<ul>
<li>Carlo CORRALES DELGADO</li>
</ul>
</td>
</<tr>
</tdbody>
</table>




<table>
<theader>
<tr><th colspan="6">SOLUCIÓN Y RESULTADOS</th></tr>
</theader>
<tbody>
</tr>
<tr><td colspan="6">
<tr>
#I. PRESENTAMOS EL LABORATORIO 07 RELACIONES DE UNO A MUCHOS, DE MUCHOS A MUCHOS E 
IMPRESIÓN DE PDF Y EMAILS:
A. <br><br>
-   En primer lugar presentaremos la estructura del proyecto, cabemencionar que 
se ha establecido un entorno virtual, instalacionde Django dentro de nuestro entorno:
    

![Estructura](src/imagenes/estructura.png)

</tr>
<tr>
-   Configuramos el settings.py, insertamos la app example y agregamos la ruta del template:

![Estructura](src/imagenes/example_en_app.png)
![Estructura](src/imagenes/templates.png)
</tr><tr>

-   Empezamos modificando el models.py de nuestra aplicacion:

![models](src/imagenes/modificando_el_models.png)

</tr><tr>
-   Realizamos makemigrations y migrate:

![migracion](src/imagenes/makemigrations_migrate_2.png)

</tr><tr>
- Para poder observar, debemos realizar la instalacion del gestor de BD.

![Instalación](src/imagenes/instalacion_DB_browser.png)
</tr><tr>

- Observamos desde el DB Browser:

![se observan las celdas](src/imagenes/resultado1_BD.png)

</tr><tr>
-  Empezamos a insertar datos desde el shell:

![Insertando desde el shell](src/imagenes/insertando_shell.png)

</tr><tr>


-   Podemos observas en las tablas los datos insertados:

![primera inserción](src/imagenes/resultado2_BD.png)
</tr><tr>
-   Continuamos trabajando con el shell:

![java](src/imagenes/java_shell_consola.png)
</tr><tr>
-   Observamos los cambios:

![DB](src/imagenes/java_shell.png)
</tr><tr>
-   Tambien observamos en la tabla example_framework:

![example_framework](src/imagenes/spring_2.png)

</tr><tr>

# CONTINUAMOS CON EL VIDEO 20:<br>

-     Realizamos las modificaciones del models.py de nuestra aplicacion:

![Modificando el models.py](src/imagenes/models_met_def.png)
</tr><tr>

-   Trabajamos con filter y all:
![filter y all](src/imagenes/all_filter_shell.png)

</tr><tr>

# CONTINUAMOS CON EL VIDEO 21:<br>

</tr><tr>

-   Implementando la class Movie y la class Character en el models.py de la aplicación:

```python
    class Movie(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=10)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

```
</tr><tr>
-   Se muestra la imagen:

![Class Movie y Class Character](src/imagenes/class_movie_character.png)

-   Luego de la modificación realizamos python manage.py makemigrations y 
python manage.py migrate.
</tr><tr>

![makemigrations y migrate](src/imagenes/makemigrations_migrate_2.png)

</tr><tr>

-   Insertando datos desde el shell a la tabla Movie y Character:

![Insertando desde el shell a Movie y Character](src/imagenes/peliculas_shell.png)

</tr><tr>
-   Observamos en el gestor los datos insertados desde el shell:

![Se observa los datos insertados](src/imagenes/example_character_movie.png)

</td><tr>

![Visualizando la tabla Movie](src/imagenes/example_movie.png)

</td><tr>

-   Creando el campo Winter Soldier desde el shell:
![Creando el campo winter soldier](src/imagenes/create_winter_soldier.png)

</tr><tr>

![Creando el campo winter soldier](src/imagenes/winter_soldier_DB.png)

</tr><tr>

# CONTINUAMOS CON EL VIDEO 22:<br>

</tr><tr>

-   En este punto se continúa trabajando con filter, con el get y set:

![Trabajando con el get y set](src/imagenes/get_shell.png)

</tr><tr>

# CONTINUAMOS CON EL VIDEO 23:<br>

</tr><tr>

-   Se expone con relacion al uso de las bases de datos con las cuales 
el usuario puede interarctuar.


</tr><tr>

# DJANGO Y PDF:<br>

</tr><tr>

-   Iniciamos esta parte realizando las configuraciones en el settings de nuestro 
proyecto:

```python
   TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,

    }
   ]
```

![Configurando el settings](src/imagenes/templates.png)

</tr><tr>

-   Ahora para cumplir con los requisitos, instalaremos los paquetes con el siguiente
comando: "pip install --prehhtml2pdf".

![Configurando el settings](src/imagenes/pip_install_xhtml2pdf.png)

</tr><tr>

-   Creamos el archivo utils.py, en este archivo agregamos la funcion
render_to_pdf.

```python
   from io import BytesIO
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa

    def render_to_pdf(template_src, context_dict={}):
        template = get_template(template_src)
        html  = template.render(context_dict)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None
```

![Funcion render](src/imagenes/render_to_pdf.png)

</tr><tr>

-   Creamos una carpeta templates, dentro de ella creamos el archivo invoice.html.

![Archivo invoice.html](src/imagenes/invoice.png)

</tr><tr>

-   Creamos un archivo views.py dentro de nuestro proyecto y a quí debemos tener la clase
GeneratePDF(View).


```python
   class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            'invoice_id': 123,
            'customer_name': "Omar Romero",
            'amount': 1399.99,
            'today':"Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='aplication/pdf')
            filename = "Invoice_%s.pdf" %("123456789")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response ['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
```
</tr><tr>

-   Modificaremos el urls.py:

```python
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('pdf/', GeneratePDF.as_view()),
]
```
</tr><tr>

-   Corremos el servidor y observamos los resultados en el navegador:

![Primera vista del PDF](src/imagenes/pdf_1.png)

</tr><tr>

-   Modificamos la clase GeneratePDF:

![Modificando la clase GeneratePDF](src/imagenes/modificacion_class_Generate.png)

</tr><tr>

-   Observamos los resultados:

![Vista del PDF](src/imagenes/pdf_2.png)

</tr><tr>

-   Realizamos la modificación en la clase GeneratePDF, para retornar el PDF:

![Modificando la clase GeneratorPDF](src/imagenes/modificacion_class_Generate_2.png)

</tr><tr>

-   Observamos los resultados:

![Vista del PDF](src/imagenes/pdf_3.png)

</tr><tr>

-   Ahora realizamos la modificacion de la clase para poder descargar el PDF:

![Modificando la clase GeneratorPDF](src/imagenes/modificacion_class_Generate_3.png)

</tr><tr>

-   Observamos los resultados:

![Vista del PDF](src/imagenes/pdf_4.png)

</tr><tr>

-   Hacemos una modificación para implementar el download desde el navegador:

![Modificando la clase GeneratorPDF](src/imagenes/modificacion_class_Generate_4.png)

![Vista del PDF](src/imagenes/download_barra.png)

</tr><tr>

# ENVÍO DE SMS:<br>

-   En primera instancia crearemos la app send "django-admin startapp send":

![Vista del PDF](src/imagenes/send.png)

-   Ahora modificaremos el urls.py del proyecto:

```python
   urlpatterns = [
        path('admin/', admin.site.urls),
        path('pdf/', GeneratePDF.as_view()),
        path('', include('send.urls')),
    ]
```
-   Creamos un archivo urls.py en al app send y ponemos el siguiente código:

```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index),
    ]
```
-   En el settings.py del proyecto añadimos la aplicación send:

```python
   INSTALLED_APPS = [
    'send',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'example',
    ]
```
-   Ahora modificamos el views.py de la app send:

```python
    from django.shortcuts import render
    from django.core.mail import send_mail

    def index(request):

        send_mail('Hola Omar', 'Este es un msm autogenerado', 
        'oromero@unsa.edu.pe', 
        ['oromero@unsa.edu.pe'], 
        fail_silently=False)
        return render(request, 'index.html')
```
-   Creamos nuestro archivo index.html en nuestra carpeta temaplates:

![Vista del PDF](src/imagenes/img_index.png)

-   Configuramos el settings.py de nuestro proyecto:

```python
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'oromero@unsa.edu.pe'
    EMAIL_HOST_PASSWORD = 'clave'
    EMAIL_USE_TLS = True
    EMAIL_USER_SSL = True
```

-   Finalmente s emuestran los resultados desde el navegador:

![Enlace para modificar los permisos](src/imagenes/send_email.png)

-   Envio del mensaje al correo institucional:

![Enlace para modificar los permisos](src/imagenes/sms_recibido.png)

![Enlace para modificar los permisos](src/imagenes/sms_recibido2.png)

-   Al usa el SMTP, GitHub nos da la siguiente advertencia:

![Enlace para modificar los permisos](src/imagenes/alerta.png)

-   Enlace para cambiar los permisos de gmail, para el acceso de aplicaciones menos seguras
es necesario habilitar esta opción para el envío de msn al gmail, se realiza en el siguiente enlace:

https://www.google.com/settings/security/lesssecureapps

![Enlace para modificar los permisos](src/imagenes/permisos_acceso_app.png)

# Se recuerda actualizar la clave del correo para que funcione correctamente.<br>

<tr><td colspan="6">II. SOLUCIÓN DE CUESTIONARIO: <br>

-   No hay cuestionario para esta réplica 


</tr>
</tr>
<tr><td colspan="6">III. CONCLUSIONES:

-   Se ha interactuado las relaciones uno a uno, uno a muchos, todo se ha realizado desde el shell.. 
</tr>

</tdbody>
</table>


<table>
<theader>
<tr><th colspan="6">RETROALIMENTACIÓN GENERAL</th></tr>
</theader>
<tbody>
</tr>
<tr><td colspan="6">
<ul>
<li><a </a></li>
<li><a </a></li>
<li><a </a></li>
</ul>
</td>
</<tr>
</tdbody>
</table>


<table>
<theader>
<tr><th colspan="6">REFERENCIAS BIBLIOGRÁFICAS</th></tr>
</theader>
<tbody>
</tr>
<tr><td colspan="6">
<ul>
<li>https://www.tutorialspoint.com/What-are-pyc-files-in-Python#:~:text=pyc%20files%20are%20created%20by,is%20newer%20than%20the%20corresponding%20.</li>

<li>https://web.archive.org/web/20160130165632/http://www.network-theory.co.uk/docs/pytut/CompiledPythonfiles.html
</li>

<li></li>
</ul>
</td>
</<tr>
</tdbody>
</table>




