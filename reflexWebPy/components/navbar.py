import reflex as rx
from reflexWebPy.styles.styles import size as size
from reflexWebPy.styles.colors import TextColor as textcolor


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", color=textcolor.BODY.value,), href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    # rx.image(
                    #     src="/code-solid.svg",
                    #     width="2.25em",
                    #     height="auto",
                    #     border_radius="25%",
                    # ),
                    rx.heading(
                        "F.Fernández", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("Proyectos", "/#proyectos",),
                    navbar_link("Comunidad", "/#comunidad",),
                    # navbar_link("Cursos", "/#cursos",),
                    justify="end",
                    spacing="5",
                    color=textcolor.BODY.value,
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    # rx.image(
                    #     src="/logo.jpg",
                    #     width="2em",
                    #     height="auto",
                    #     border_radius="25%",
                    # ),
                    rx.heading(
                        "F.Fernández", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.link("Home", href="/#", color=textcolor.BODY.value,),
                        rx.link("Proyectos", href="/#proyectos", color=textcolor.BODY.value,),
                        rx.link("Comunidad", href="/#comunidad", color=textcolor.BODY.value,),
                        rx.link("Cursos", href="/#cursos", color=textcolor.BODY.value,),
                       
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
      position="fixed",  # Se posiciona dentro del contenedor hero
        top="0",
        left="0",
        width="100%",
        z_index="10",  # Asegura que se superponga al fondo del hero
        bg="transparent",
        padding="1em",
        color=textcolor.BODY.value,
        
    )