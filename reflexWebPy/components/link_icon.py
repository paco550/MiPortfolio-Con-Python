import reflex as rx
from reflexWebPy.styles.styles import size as size
from reflexWebPy.styles.styles import TextColor as textcolor

def link_icon(image: str, url: str,) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(
                src=image,
                width=size.DEFAULT.value,
                # height=size.MEDIUM.value,
                margin="5px 10px",
                
            ),
            
        ),
        href=url,
        is_external=True
    )