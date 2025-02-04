import reflex as rx
from reflexWebPy.components.link_icon import link_icon
from reflexWebPy.components.title import title
from reflexWebPy.components.info_text import info_text
from reflexWebPy.styles.styles import size as size
from reflexWebPy.styles.colors import TextColor as textcolor

def header() -> rx.components:
    return rx.vstack(
        rx.hstack(
            rx.avatar(src="/perfil.ico", radius="full", size="7",  position="relative", top="20px"),
            rx.vstack(
                title("F.Fernández",),
                rx.text(
                    "@F.Fernández",
                    margin_top="0px !important",
                    color=textcolor.BODY.value,
                    spacing=size.MEDIUM.value,
                    ),
                    
                    rx.hstack(
                    link_icon("https://www.twitch.tv/"),
                    link_icon("https://www.youtube.com/"),
                    link_icon("https://www.youtube.com/watch?v=n2YrGsXJC6Y&t=8709s"),
                     ),
                     width="100%",
                    align_items="start",
            ),

            ),
            rx.flex(
                info_text("+13", "años de esperiencia"),
                rx.spacer(),
                info_text("+13", "años de esperiencia"),
                rx.spacer(),
                info_text("+13", "años de esperiencia"),
                width="100%",
                color=textcolor.BODY.value,
            ),
             rx.text(
                 """Soy Francisco Fernández Bailén, desarrollador 
                 web full stack con experiencia en Angular y .NET, y 
                 conocimientos en diversas tecnologías como Astro, Node.js,
                 Python, Java y bases de datos. Tengo experiencia 
                 liderando proyectos, organizando equipos con 
                 herramientas como Trello y trabajando con tecnologías 
                 innovadoras como reflex.""",
                 spacing=size.BIG.value,
                 align_items="start",
                 color=textcolor.BODY.value,
                 ),
                  position="relative",
                  top="-100px",
    )