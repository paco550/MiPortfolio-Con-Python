import reflex as rx
import reflexWebPy.styles.styles as styles

def links_button(title:str = "", body:str = "",  image: str = "", url: str = "", institution: str = "", duration: str="", description: str="", is_external=True) -> rx.components:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width="2em",
                    height="2em"
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    rx.text(institution, style=styles.button_body_style),
                    rx.text(duration, style=styles.button_body_style),
                    rx.text(description, style=styles.button_body_style),
                ),
            ),
                  
        ),
        href=url,
        is_external=is_external,
        width="100%"
        
    )