import reflex as rx
from reflexWebPy.styles import styles
from reflexWebPy.styles.colors import TextColor
from reflexWebPy.styles.styles import size as size


def animated_text(text: str):
    return rx.center(
        rx.vstack(
            rx.text(
                text,
                size="7",
                text_align="center",
                        _hover={"color": TextColor.BODY1.value },

                style=styles.title_style
            ),
            width="100%",
            margin_top="10em",  # Ajusta este valor para mover verticalmente
            align_items="center",
            justify_content="center"
        ),
        width="100%",
        height="100%"
    )