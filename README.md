Proyecto Flask - Aplicación de Productos y Usuarios
Este es un proyecto de ejemplo utilizando Flask para construir una aplicación web sencilla. La aplicación permite mostrar una lista de productos en una página y una tabla de usuarios en otra, utilizando plantillas de Jinja2 para separar el Back-End y el Front-End.

## Estructura del Proyecto

```plaintext
Wolf-s-unlock-game/
├── app.py            # Código Python con la lógica de Flask
├── static/           # Archivos estáticos (CSS, imágenes, etc.)
│   └── styles.css    # Archivo CSS para los estilos
├── templates/        # Plantillas HTML
│   ├── base.html     # Plantilla base con la estructura general
│   ├── index.html    # Página de inicio
│   ├── pagina1.html  # Página 1 (Lista de productos)
│   └── pagina2.html  # Página 2 (Tabla de usuarios)
└── requirements.txt  # Dependencias del proyecto
```

Instalación
Clona el repositorio:

```plaintext
git clone https://github.com/DJWolfboi/Wolf-s-unlock-game.git
```
Navega a la carpeta del proyecto:
```plaintext
cd Wolf-s-unlock-game
```
(Opcional) Crea un entorno virtual para instalar las dependencias:

```plaintext
python -m venv venv
source venv/bin/activate  # En Mac o Linux
venv\Scripts\activate     # En Windows
```
Instala Flask y otras dependencias:
``` plaintext
pip install -r requirements.txt
```

Ejecuta la aplicación Flask:

```plaintext
python app.py
```

Abre tu navegador y ve a http://127.0.0.1:5000/ para ver la página de inicio.

Navega a las siguientes rutas:

```plaintext
/pagina1: Para ver la lista de productos para la mejora de tu consola.

/pagina2: Para ver la tabla de usuarios Recientes.
```
Explicación
```plaintext
base.html: Contiene la estructura común del sitio (encabezado, menús de navegación).

index.html: Página principal que muestra los enlaces a las demás páginas.

pagina1.html: Página que muestra una lista de productos utilizando datos dinámicos.

pagina2.html: Página que muestra una tabla con información de usuarios.
```
Reflexión
La separación entre Back-End y Front-End mejora la claridad del proyecto al permitir que cada parte tenga una responsabilidad única. Además, hace que el proyecto sea más escalable, ya que podemos modificar el diseño o la funcionalidad de forma independiente sin afectar al otro.
