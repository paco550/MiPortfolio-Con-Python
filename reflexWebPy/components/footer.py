import reflex as rx
import datetime
from reflexWebPy.styles.styles import size as size
from reflexWebPy.styles.styles import TextColor as textcolor



def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
           f"© 2022 - {datetime.date.today().year} Francisco Fernández Bailén. Todos los derechos reservados.",
            href="https://www.linkedin.com/in/francisco-fern%C3%A1ndez-bail%C3%A9n/",
            is_external=True,
            font_size=size.MEDIUM.value
        ),
                rx.text("Hecho con 💻 y ☕ por Francisco Fernández Bailén. Construyendo ideas en la web. ", color="#C3C7CB"),
                rx.link("¿Hablamos?", href="mailto: pacofb70@gmail.com", color="blue",underline="hover"),
                margin_bottom=size.BIG.value,
                margin_top="0px !important",
                align="center",
        )
    