import reflex as rx
from reflexWebPy.styles.styles import size as size
from reflexWebPy.styles.colors import TextColor as TextColor 
# from reflexWebPy.components.ant_components import float_button

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium",), 
        href=url,
        _hover={"color": TextColor.TITLE.value },
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
                       rx.link( "F.Fernández",href="/#", size="7", weight="bold", _hover={"color": TextColor.TITLE.value },),
                    ),
                    align_items="center",
                ),
                # float_button(),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("Proyectos", "/#proyectos",),
                    navbar_link("Comunidad", "/#comunidad",),
                    navbar_link("Cursos", "/#cursos",),
                    justify="end",
                    spacing="5",
                     _hover={"color": TextColor.TITLE.value },
                    # color=textcolor.BODY.value,
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
                       rx.link( "F.Fernández", href="/#", size="6", weight="bold", _hover={"color": TextColor.TITLE.value },),
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30,         _hover={"color": TextColor.TITLE.value },
)
                    ),
                    rx.menu.content(
                        rx.link("Home", href="/#",_hover={"color": TextColor.TITLE.value },),
                        rx.link("Proyectos", href="/#proyectos", _hover={"color": TextColor.TITLE.value },),
                        rx.link("Comunidad", href="/#comunidad",_hover={"color": TextColor.TITLE.value }, ),
                        rx.link("Cursos", href="/#cursos",_hover={"color": TextColor.TITLE.value },),
                        
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
        
        
    )