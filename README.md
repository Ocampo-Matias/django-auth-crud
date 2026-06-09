# Django Tasks CRUD (Django Auth CRUD)

Una aplicación web de gestión de tareas con sistema de autenticación de usuarios integrado. Este es un proyecto educativo desarrollado como parte del proceso de aprendizaje siguiendo el curso práctico de Django impartido por **Fazt Code** en YouTube. Su finalidad es consolidar e implementar de forma guiada conocimientos fundamentales de desarrollo backend, base de datos relacionales y configuración de despliegue.

---

## 🚀 Características Principales

- **Gestión de Sesiones (Autenticación):** Registro de usuarios (`UserCreationForm`), inicio de sesión (`AuthenticationForm`) y cierre de sesión seguro utilizando el sistema nativo de autenticación de Django.
- **Operaciones CRUD Completas:** Creación, lectura, actualización y eliminación de tareas asociadas de forma única a cada usuario.
- **Estados de Tareas:** Posibilidad de marcar tareas como "Importantes" (priorizadas) y "Completadas" (con registro automático de fecha/hora de finalización).
- **Vistas Filtradas:** Separación clara entre tareas pendientes y completadas para una mejor organización de la interfaz.
- **Seguridad en Rutas y Datos:** Control de acceso mediante el decorador `@login_required` a nivel de vista y validación en las consultas del ORM (`get_object_or_404(task, pk=id, user=request.user)`) para asegurar que un usuario solo pueda interactuar con sus propios registros.
- **Configuración de Producción:** Integración de `dj-database-url` para el manejo dinámico de la base de datos, `WhiteNoise` para servir archivos estáticos de forma eficiente y scripts de construcción listos para plataformas de hosting como Render.

---

## 🛠️ Tecnologías y Herramientas

- **Backend:** Python 3.x / Django 5.0.x
- **Base de Datos:** PostgreSQL (en desarrollo y producción)
- **Frontend:** HTML5, Plantillas de Django (MVT), Bootstrap 5.3 (estilos responsivos cargados vía CDN)
- **Servidor y Despliegue:** Gunicorn, Uvicorn, WhiteNoise (compresión y caché de archivos estáticos)

---

## 📸 Capturas de Pantalla (Placeholder)

*Próximamente se añadirán capturas de pantalla de la interfaz de usuario en funcionamiento.*

| Vista de Inicio | Panel de Tareas | Crear / Editar Tarea |
|:---:|:---:|:---:|
| ![Inicio / Bienvenida](https://via.placeholder.com/400x250?text=Vista+de+Inicio) | ![Lista de Tareas](https://via.placeholder.com/400x250?text=Panel+de+Tareas+Pendientes) | ![Formulario Tarea](https://via.placeholder.com/400x250?text=Crear/Editar+Tarea) |

---

## 🔧 Instalación y Configuración Local

Para ejecutar este proyecto en tu entorno local, sigue estos pasos:

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/django-auth-crud.git
cd django-auth-crud
```

### 2. Crear y activar un entorno virtual
En Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```
En macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```
*(Nota: Asegúrate de tener instalado `dj-database-url` para el mapeo dinámico de la base de datos si usas la configuración por defecto de PostgreSQL. Puedes instalarlo con `pip install dj-database-url` si no se instala automáticamente).*

### 4. Configurar la Base de Datos
El proyecto está preconfigurado para utilizar **PostgreSQL**.

- **Opción A (PostgreSQL - Local):** Asegúrate de tener un servidor de PostgreSQL corriendo localmente y crea una base de datos llamada `mysite` (o ajusta la cadena de conexión en `djangocrud/settings.py` línea 87).
- **Opción B (SQLite - Desarrollo rápido):** Si prefieres probar el proyecto rápidamente con SQLite, puedes modificar temporalmente la configuración en `djangocrud/settings.py`:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
  }
  ```

### 5. Ejecutar migraciones
Aplica la estructura de datos a tu base de datos:
```bash
python manage.py migrate
```

### 6. Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```
Accede a `http://127.0.0.1:8000/` en tu navegador para ver la aplicación.

---

## 💡 Aprendizajes Obtenidos

Desarrollar este proyecto me permitió adquirir y consolidar las siguientes habilidades técnicas fundamentales:

1. **Flujo MVT (Model-View-Template):** Comprensión del patrón arquitectónico de Django, conectando modelos de base de datos con vistas de control y plantillas HTML dinámicas.
2. **Seguridad y Control de Accesos:** Implementación práctica del sistema de autenticación nativo de Django (`contrib.auth`), asegurando rutas individuales y restringiendo el acceso del ORM únicamente a los registros del usuario autenticado.
3. **Manejo de Formularios y Validación:** Integración de Django `ModelForm` y definición de widgets personalizados para enlazar modelos con componentes HTML estilizados mediante clases de Bootstrap de manera segura.
4. **Preparación para Producción:** Configuración y adecuación de variables de entorno, serving de archivos estáticos optimizados con `WhiteNoise` y creación de un script de construcción (`build.sh`) listo para despliegues automatizados.

---

## 📈 Posibles Mejoras Futuras

- [ ] **Desarrollo de API REST:** Migrar el backend hacia Django REST Framework (DRF) para desacoplar el frontend y poder conectar el backend con interfaces de una sola página (React, Vue) o aplicaciones móviles.
- [ ] **Búsqueda y Paginación:** Añadir una barra de búsqueda de tareas y controles de paginación para mejorar la experiencia de usuario cuando haya un volumen alto de registros.
- [ ] **Etiquetas y Categorías:** Incorporar relaciones de uno a muchos o muchos a muchos para clasificar las tareas (ej. Trabajo, Universidad, Personal).
- [ ] **Pruebas Automatizadas:** Desarrollar tests unitarios para las vistas y formularios utilizando la suite de testing nativa de Django.
- [ ] **Notificaciones y Alertas:** Añadir mensajes dinámicos en pantalla tras realizar acciones exitosas (crear, completar, borrar tareas) y soporte para recordatorios por correo electrónico.
