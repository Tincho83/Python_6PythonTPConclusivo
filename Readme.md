# Proyecto Django - Sistema de Ecommerce y Gestión de Pedidos

Link Video Explicativo:
Link Video Demo:

Este proyecto es un sistema de ecommerce desarrollado en **Django 4.2**, que permite la gestión de productos, categorías, tipos de documento, pedidos y usuarios con perfiles. Incluye funcionalidades de carrito de compras, registro de pedidos y detalle de cada pedido.

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

## Instalación y ejecución

1. **Clonar el proyecto desde GitHub:**

```bash
git clone https://github.com/usuario/proyecto-django-ecommerce.git
cd proyecto-django-ecommerce

2. **Crear y activar un entorno virtual:**
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate


3. **Instalar dependencias:**
pip install -r requirements.txt

4. Aplicar migraciones de base de datos:

python manage.py makemigrations
python manage.py migrate

5. Crear un superusuario (opcional, para administración):
python manage.py createsuperuser

6. Ejecutar servidor de desarrollo:
python manage.py runserver

7. Acceder al proyecto:
http://127.0.0.1:8000/


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

Licencia
Este proyecto está bajo licencia MIT (puedes adaptarla según corresponda).

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

📜 Licencia
Este proyecto se distribuye bajo licencia MIT.
Podés usarlo, modificarlo y redistribuirlo libremente citando al autor original.

🌟 Autor y contribuciones
Desarrollado por Martin Hernandez. PRoyecto eCommerce para Curso Python CoderHouse
💬 Si querés contribuir, enviá un pull request o creá un issue en GitHub.

🧭 Estado del proyecto

✅ Funcionalidades principales implementadas

🔄 Mejoras en progreso (gestión avanzada de stock, informes, permisos por rol)

🧪 Tests unitarios planificados


💡 “Un sistema bien documentado es un sistema fácil de mantener.”