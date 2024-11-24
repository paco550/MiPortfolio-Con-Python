# Mi Portfolio con Reflex

Este proyecto es una aplicación web de portfolio profesional creada con Reflex. 
La aplicación permite mostrar habilidades, proyectos, experiencia laboral y ofrece un formulario de contacto interactivo.

## ¿Qué es Reflex?

Reflex es un framework que permite crear aplicaciones web frontend y backend usando únicamente Python. 
Con Reflex, puedes concentrarte en la lógica de tu aplicación sin preocuparte por la configuración del frontend.

Para más información sobre Reflex, visita su documentación oficial: https://reflex.dev/docs

---

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes elementos:

- Python 3.7 o superior
- Pip (gestor de paquetes de Python)
- Navegador moderno para la ejecución

---

## Instalación y configuración

Sigue estos pasos para instalar y ejecutar el proyecto en tu máquina local:

### 1. Clonar el repositorio

$ git clone https://github.com/paco550/MiPortfolio-Con-Python.git
$ cd MiPortfolio-Con-Python

### 2. Instalar Reflex

Si aún no tienes Reflex instalado, ejecútalo desde pip:

$ pip install reflex

### 3. Configuración inicial

Asegúrate de configurar las variables necesarias en el archivo rxconfig.py si deseas personalizar el comportamiento del proyecto.

### 4. Ejecutar en modo desarrollo

Para iniciar el servidor de desarrollo y ver tu aplicación en tiempo real, usa:

$ reflex dev

Esto abrirá automáticamente tu navegador en: http://localhost:3000

---

## Despliegue

Reflex soporta múltiples opciones de despliegue. Para generar los archivos de producción y subirlos a un servidor:

### 1. Exportar los archivos

$ reflex export

Esto generará una carpeta "out" con los archivos listos para producción.

### 2. Subir a un servidor

Puedes usar servicios como:

- Vercel
- AWS
- Heroku

Consulta la guía de despliegue de Reflex para detalles específicos: https://reflex.dev/docs/hosting/deployment

---

## Estructura del proyecto

El proyecto está organizado de la siguiente manera:

MiPortfolio-Con-Python/
│
├── assets/             # Archivos estáticos (imágenes, CSS)
├── components/         # Componentes reutilizables
├── pages/              # Definición de las páginas de la aplicación
├── rxconfig.py         # Configuración del proyecto Reflex
└── main.py             # Punto de entrada de la aplicación

---

## Personalización

Para personalizar las secciones del portfolio, edita los componentes y páginas en las carpetas correspondientes. Reflex te permite usar lógica Python para definir el diseño y comportamiento.

---

## Contribución

¿Quieres contribuir al proyecto? Sigue estos pasos:

1. Haz un fork del repositorio.

2. Crea una rama nueva para tu funcionalidad:

$ git checkout -b feature/nueva-funcionalidad

3. Realiza tus cambios y haz un commit:

$ git commit -m "Añadir nueva funcionalidad"

4. Abre un pull request en este repositorio.

---

## Recursos adicionales

- Documentación de Reflex: https://reflex.dev/docs
- Comunidad en Discord de Reflex: https://discord.com/invite/reflex

---

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más información.

---

### Autor

Creado por Francisco Fernández Bailén. ¡Espero que este proyecto te inspire a desarrollar tus propias aplicaciones con Reflex! 🚀

