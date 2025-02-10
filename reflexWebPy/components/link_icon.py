import reflex as rx
from reflexWebPy.styles.styles import size as size
from reflexWebPy.styles.styles import TextColor as textcolor

def link_icon(image: str, url: str, text: str = "") -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(
                src=image,
                width=size.DEFAULT.value,
            ),
            rx.text(text,
                    color=textcolor.BODY.value,
                    size=size.SMALL.value,
                    )  # Añadimos el texto debajo de la imagen
        ),
        href=url,
        is_external=True
    )