import reflex as rx
import reflexWebPy.styles.styles as styles

def title(text: str) -> rx.components:
    return rx.heading(
        text,
        size="5",
        style=styles.title_style
        )