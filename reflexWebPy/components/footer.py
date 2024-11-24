import reflex as rx
import datetime
from reflexWebPy.styles.styles import size as size



def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
           f"este es el footer {datetime.date.today().year}",
            href="https://moure.dev/",
            is_external=True,
            font_size=size.MEDIUM.value
        ),
                rx.text("Francisco Fernández Bailén"),
                margin_bottom=size.BIG.value,
                margin_top="0px !important",
                align="center",
                       


        )
    