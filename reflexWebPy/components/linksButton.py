import reflex as rx
import reflexWebPy.styles.styles as styles

def links_button(title:str, body:str, url: str) -> rx.components:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow-right",
                    width="2em",
                    height="2em"
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                ),
            ),
                  
        ),
        href=url,
        is_external=True,
        width="100%"
    )