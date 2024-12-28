import reflex as rx
from reflexWebPy.styles.styles import size as size

def navbar() -> rx.components:
    return rx.hstack(
        rx.text.em("F.Fernández" 
        ),  
        position="stycky",
        bg="#d6d6d6",
        padding_x=size.DEFAULT.value,
        padding_y=size.SMALL.value,
        z_index="100",
    )