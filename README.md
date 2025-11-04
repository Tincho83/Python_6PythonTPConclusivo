# TP Conclusivo de Python para CoderHouse
# Proyecto Django - Sistema de Ecommerce y Gestión de Pedidos

## Link Video Demo: 
> https://drive.google.com/file/d/12YVDx1acwX9ZsLJgJgm1nWwI_vzMhtKJ/view?usp=sharing

## Link Video Explicativo: 
> https://drive.google.com/file/d/1jIkr1n8fSEqDXEL5F1yEepbS_AYGcZEl/view?usp=sharing

## Descripción
Proyecto eCommerce en Python usando Django. 
Este proyecto es un sistema de ecommerce desarrollado en **Django**, que permite la gestión de productos, categorías, tipos de documento, pedidos y usuarios con perfiles. 

# Proyecto Django - eCommerce

## Instalación y ejecución
## Cómo probar:
1. Descargar el proyecto desde el Repo: 
      `https://github.com/Tincho83/Python_6PythonTPConclusivo`
   o Clonarlo desde: 
      `https://github.com/Tincho83/Python_6PythonTPConclusivo.git`

2. Una vez clonado o descomprimido el proyecto, debe estar dentro de la     carpeta del proyecto (Ej. Python_6PythonTPConclusivo_main).
   `cd Python_6PythonTPConclusivo`
   o
   `cd Python_6PythonTPConclusivo_main`

3. Crear un entorno virtual: 
      `python -m venv ent_virt_ecommerce`
   
   Si presenta error de permisos debe ejecutar este comando powershell como admin: 
   `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
   y luego volver a ejecutar la creacion del entorno virtual.

4. Ingresar/Activar al Entorno virtual: 
      Windows:`ent_virt_ecommerce/Scripts/Activate`
      Linux / macOS: `source ent_virt_ecommerce/bin/activate`

      en caso que se desee salir del entorno virtual:
      `deactivate`

5. Instalar Dependencias del proyecto: 
   `pip install -r requeriments.txt`

   Si deseas instalar los modulos por separado:
   `pip install django`
   `pip install pillow`
   `pip install git`
   `pip install django-ckeditor`

6. Preparar/Aplicar migraciones a la Base de Datos:
   `python manage.py makemigrations`
   `python manage.py migrate`

7. Crear superusuario para el acceso a Admin del sitio:
      `python manage.py createsuperuser`

      Para la Demo utilizo:
      usuario: super
      contraseña: super

8. Iniciar el proyecto:
   `python manage.py runserver`

9. Desde un navegador Web ingresar:
      `http://localhost:8000/`

      Para el Portal Admin:
      `http://localhost:8000/Admin`


## Navegacion:
1. Luego de ingresar a la url `http://localhost:8000/`, se podra ver la barra de navegacion en donde se podra:
   - Ir al Inicio (`/`)
   - Ver productos (`/productos/`)
   - Buscar productos (`/buscar/`)
   - Ver informacion sobre el programador (`/paginas/about/`)
   - Registrar Usuario (`/cuentas/registro/`)
   - Iniciar sesion de Usuario (`/cuentas/login/`)

2. Registro de Usuario:
      `http://localhost:8000/cuentas/registro/`

      En esta seccion se solicitara ingresar:
      "Nombre de Usuario",
      "EMail (Correo Electronico)",
      "Nombre (First Name)",
      "Apellido (Last Name)",
      "Contraseña",
      "Repetir Contraseña"

      Luego clic en "Registrarse"
      Si no se presenta ningun error de validacion, se redirecionara a la pagina de inicio de sesion con un cartel informando que se registro el usuario correctamente.

3. Inicio de sesion:
      `http://localhost:8000/cuentas/login/`

      En esta seccion se solicitara:
      "Nombre de Usuario",
      "Contraseña"

      Luego clic en "Entrar"
      Si no se presenta ningun error de validacion, se redirecionara a la pagina de inicio mostrando en el navbar el perfil de sesion iniciado.

      Si por alguna razon desde el Home, el usuario hizo clic en Iniciar sesion, esta seccion posee un vinculo a la pagina de Registracion.

4. Desde una sesion iniciada, se puede comprobar que ya el usuario posee mas opciones a realizar:
   - Ir al Inicio (`/`)
   - Ver y crear productos(`/productos/`). Antes de crear un producto debe tener su categoria creada (TV, radio, Electro, etc).
   - Buscar productos (`/buscar/`). Busca por titulo o descripcion.
   - Ver informacion sobre el programador (`/paginas/about/`)
   - Ver y crear Tipo de Documento (`/operaciones/tipodoc/crear/`)
   - Ver y crear Pedidos (`/operaciones/pedido/crear/`). Antes de hacer un pedido debe haber un usuario y producto creado.
   - Ver y crear Categorias (`/operaciones/categoria/crear/`)
   - Ver y modificar perfil de Usuario (`/cuentas/perfil/`). Antes de modificar el Documento del Usuario debe tener creado el tipo de documento.
   - Cierre de sesion de Usuario (`/cuentas/logout/`)
      

---

## Contenido

- [Funcionalidades](#funcionalidades)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Tecnologías usadas](#tecnologías-usadas)
- [Instalación y ejecución](#instalación-y-ejecución)
- [Pre-requisitos](#pre-requisitos)
- [Configuración de imágenes](#configuración-de-imágenes)
- [Notas y recomendaciones](#notas-y-recomendaciones)
- [Licencia](#licencia)

---

## Funcionalidades

- Registro y gestión de **productos** con nombre, subtítulo, descripción (CKEditor), imagen local o URL, precio y stock.
- Gestión de **categorías** y **tipos de documento**.
- Registro de **pedidos**:
  - Selección de uno o varios productos.
  - Registro de cantidad y subtotal.
  - Cálculo automático del total del pedido.
  - Relación entre `Pedido` y `DetallePedido` para almacenar el detalle por producto.
- Gestión de **usuarios** con perfiles extendidos (`Perfil`).
- Visualización de listas para cada módulo (ABM: alta, baja, modificación, listado).
- Validaciones de stock y precios.
- Manejo de imágenes:
  - Imágenes **locales** dentro de `media/productos/`.
  - Imágenes **externas** mediante URL.
  - Imagen por defecto cuando no hay imagen disponible.

---

## Estructura del proyecto

project_root/
│
├─ app_ecommerce/ # Gestión de productos
│ ├─ models.py
│ ├─ views.py
│ ├─ templates/app_ecommerce/
│ │ ├─ product_list.html
│ │ └─ product_detail.html
│ └─ ...
│
├─ app_operaciones/ # Pedidos, categorías, tipos de documento
│ ├─ models.py
│ ├─ views.py
│ ├─ forms.py
│ └─ templates/app_operaciones/
│ ├─ pedido_form.html
│ ├─ pedido_list.html
│ ├─ categoria_form.html
│ └─ tipodoc_list.html
│
├─ app_cuentas/ # Usuarios y perfiles
│ ├─ models.py
│ ├─ views.py
│ └─ templates/app_cuentas/
│ └─ profile.html
│
├─ media/ # Carpeta para almacenar imágenes subidas
│ └─ productos/
│
├─ static/ # Archivos estáticos (CSS, JS, imágenes por defecto)
│
├─ manage.py
└─ requirements.txt



---

## Tecnologías usadas

- **Backend:** Python 3.8+, Django 4.2+
- **Frontend:** HTML, Bootstrap 5, CKEditor (para descripciones de productos)
- **Base de datos:** SQLite (por defecto, se puede configurar otra)
- **Dependencias adicionales:** Pillow, django-ckeditor, etc.
- **Control de versiones:** Git
- **Sistema de plantillas:** Django Templates (Handlebars no usado)

---

Pre-requisitos:
Python 3.8 o superior
pip
Virtualenv (opcional pero recomendado)
SQLite (por defecto, incluido con Python)

Configuración de imágenes

Las imágenes subidas por el usuario se guardan en:
media/productos/

Imágenes externas se guardan en la propiedad imagen_url.

Cuando no hay imagen disponible, se usa una imagen por defecto ubicada en:
static/img/no_image.jpg

Configuración de imágenes
Tipo de imagen          Ubicación	               Descripción
📂 Dinámicas	         media/productos/	         Imágenes subidas por usuarios
🌐 Externas	            URL del producto	         Cargadas desde la web
🖼️ Por defecto	      static/img/no_image.jpg	     Usada cuando no hay imagen disponible


Nota: Asegúrate de configurar correctamente MEDIA_URL y MEDIA_ROOT en settings.py para servir las imágenes.
📌 Asegurate de configurar en settings.py:
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'



Notas y recomendaciones

El campo total en Pedido ahora tiene max_digits=20 y decimal_places=2 para soportar precios y cantidades grandes.

Se recomienda no ingresar cantidades excesivamente altas para evitar overflow en la base de datos.
Validaciones de stock y precio se realizan al guardar un producto.
CKEditor requiere instalación de dependencias para que funcione correctamente.
Para producción, configurar almacenamiento de archivos estáticos y media correctamente.

Módulos principales
app_ecommerce
Gestión de productos (Producto):
Nombre, subtítulo, descripción enriquecida, imagen local o URL, precio, stock y categoría.
imagen_final: devuelve URL válida de la imagen a mostrar.

app_operaciones
Gestión de pedidos (Pedido y DetallePedido):
Relación ManyToMany entre Pedido y Producto a través de DetallePedido.
Cálculo automático del total.
Gestión de categorías (Categoria) y tipos de documento (TipoDoc).

Formularios y vistas para ABM de cada módulo.
app_cuentas
Gestión de usuarios y perfiles extendidos (Perfil).
Datos del usuario: nombre, apellido, email, avatar, biografía, link y fecha de cumpleaños.


Otros detalles
Se recomienda usar Python Decimal para todas las operaciones con precios para evitar errores de redondeo.

Todas las plantillas usan Bootstrap 5 para diseño responsive.
Logs y mensajes se manejan con django.contrib.messages.

📌 Notas y recomendaciones

Se recomienda mantener max_digits=20 y decimal_places=2 en el campo total de Pedido.

Evitar cantidades extremadamente altas al registrar pedidos.

Revisar configuraciones de MEDIA_ROOT y STATICFILES_DIRS antes de despliegue.

En producción, configurar almacenamiento de media y archivos estáticos en un servicio como AWS S3 o Cloudinary.

CKEditor requiere configuración específica si se despliega en hosting compartido.

💾 Pre-requisitos
Python 3.8 o superior
pip y virtualenv
Git instalado
Conexión a internet (para dependencias y CKEditor)


🌟 Autor y contribuciones
Desarrollado por Martin Hernandez. PRoyecto eCommerce para Curso Python CoderHouse
💬 Si querés contribuir, enviá un pull request o creá un issue en GitHub.

🧭 Estado del proyecto

✅ Funcionalidades principales implementadas

🔄 Mejoras en progreso (gestión avanzada de stock, informes, permisos por rol)

🧪 Tests unitarios planificados


💡 “Un sistema bien documentado es un sistema fácil de mantener.”

## Cumple con:
- Patrón MVT de Django.
- Herencia de plantillas HTML (base.html).
- 3 modelos: Cliente, Producto, Pedido.
- Formularios para ABM de cada modelo.
- Formulario de búsqueda en la BD.

Pre-requisitos:
Python 3.8 o superior
pip
Virtualenv (opcional pero recomendado)
SQLite (por defecto, incluido con Python)

Configuración de imágenes

Las imágenes subidas por el usuario se guardan en:
media/productos/

Imágenes externas se guardan en la propiedad imagen_url.

Cuando no hay imagen disponible, se usa una imagen por defecto ubicada en:
static/img/no_image.jpg

Configuración de imágenes
Tipo de imagen          Ubicación	               Descripción
📂 Dinámicas	         media/productos/	         Imágenes subidas por usuarios
🌐 Externas	            URL del producto	         Cargadas desde la web
🖼️ Por defecto	      static/img/no_image.jpg	     Usada cuando no hay imagen disponible


Nota: Asegúrate de configurar correctamente MEDIA_URL y MEDIA_ROOT en settings.py para servir las imágenes.
📌 Asegurate de configurar en settings.py:
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
