import reflex as rx
from reflexWebPy.components.animated_text import animated_text
from reflexWebPy.components.scroll_button import scroll_button
from reflexWebPy.components.title import title
from reflexWebPy.styles import styles
from reflexWebPy.styles.colors import TextColor
from reflexWebPy.styles.styles import size as size

# Definir el estado para manejar el scroll


# Componente Hero
def hero():
    return rx.box(
        rx.section(id="inicio"),
        rx.center(
            animated_text("Hola, soy Francisco Fernández",),
            width="100%",  
           
            ),
            
            rx.center(scroll_button(),
                       margin_top="50px"),  # Botón de scroll

        position="relative",
        background_image="url('/cafe.jpeg')",
        background_size="cover",
        background_position="center",
        width="100%",
        height="100vh",
        # display="flex",
        justify_content="center",
        transition="opacity 5s",

    )