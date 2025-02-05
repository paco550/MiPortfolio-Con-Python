import reflex as rx


def reflex_text(imagen: str) -> rx.Component:
    return rx.box(
        rx.image(
            src="/P5200122.jpg",  # Reemplaza con la ruta de tu imagen
            class_name="reflex-background"
        ),
    )