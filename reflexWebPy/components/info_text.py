import reflex as rx
from reflexWebPy.styles.styles import size as size

def info_text(title: str, body: str,) -> rx.components:
    return rx.box(
        rx.text.span(
            title, 
            font_weight="bold",
            color="blue"
        ),
        f"   {body}", font_size=size.MEDIUM.value,
        
    )