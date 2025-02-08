import reflex as rx
from reflexWebPy.components.animated_text import animated_text
from reflexWebPy.components.scroll_button import scroll_button
from reflexWebPy.styles.styles import size as size

# Definir el estado para manejar el scroll
class State(rx.State):
    scroll_position: int = 0

    def update_scroll(self, scroll_pos: int):
        self.scroll_position = scroll_pos

# Componente Hero
def hero():
    return rx.box(
        rx.section(id="inicio"),
        rx.center(
            animated_text(),
            margin_top="250px",),
            
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
        opacity=50 - State.scroll_position / 900,  # Ajusta la opacidad según el scroll
        transition="opacity 5s",

    )