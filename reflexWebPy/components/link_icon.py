import reflex as rx
from reflexWebPy.styles.styles import size as size


def link_icon(image: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=size.DEFAULT.value,
        ),
        href=url,
        is_external=True
    )