import reflex as rx
from reflexWebPy.components.link_icon import link_icon
from reflexWebPy.components.title import title
from reflexWebPy.components.info_text import info_text
from reflexWebPy.styles.styles import size as size
from reflexWebPy.styles.colors import TextColor as textcolor
from reflexWebPy.styles.colors import Color as color


def header() -> rx.components:
    return rx.vstack(
        rx.hstack( 
            rx.section(id="header"),
            rx.avatar( src="/perfil.ico",
                       radius="full", 
                       size="7",  
                       position="relative", 
                       top="20px",
                       padding="2px",
                       border="4px",
                       border_color="#14A1F0",
                       border_style="dotted",
                       ),
            rx.vstack(
                title("F.Fernández",),
                rx.text(
                    "@F.Fernández",
                    margin_top="0px !important",
                    color=textcolor.BODY.value,
                    spacing=size.MEDIUM.value,
                    ),
                    
                    rx.hstack(
                    link_icon(
                        "icons/file-solid.svg",
                        "Data/Francisco Fernández Bailén (1).pdf",
                        text="CV"
                        ),
                    link_icon(
                        "icons/github-brands-solid.svg",
                        "https://github.com/paco550",
                        ),
                    link_icon(
                        "icons/linkedin-brands-solid.svg",
                        "https://www.linkedin.com/in/francisco-fern%C3%A1ndez-bail%C3%A9n/", 
                        ),
                     ),
                     width="100%",
                    align_items="start",
            ),
            ),
            rx.flex(
                info_text(" ","  "),
                link_icon(
                    "icon_tec/angular-icon-1.svg",
                    " "
                ),
                rx.spacer(),
                link_icon(
                    "icon_tec/python-5.svg",
                    " "
                ),
                rx.spacer(),
                link_icon(
                    "icon_tec/git (1).svg",
                    " "
                ),
                rx.spacer(),
                link_icon(
                    "icon_tec/react-2.svg",
                    " "
                ),
                rx.spacer(),
                link_icon(
                    "icon_tec/nodejs-2.svg",
                    " "
                ),
                rx.spacer(),
                link_icon(
                    "icon_tec/sqlite.svg",
                    " "
                ),
                rx.spacer(),
                link_icon(
                   "icon_tec/logo-javascript.svg",
                    " "
                ),
                  rx.spacer(),
                link_icon(
                    "icon_tec/docker.svg",
                    " "
                ),
                   rx.spacer(),
                link_icon(
                    "icon_tec/csharp.svg",
                    " "
                ),
                   rx.spacer(),
                link_icon(
                    "icon_tec/mongodb-icon-1.svg",
                    " "
                ),
                # rx.spacer(),
                # info_text("+13", "años de esperiencia"),
                # rx.spacer(),
                # info_text("+13", "años de esperiencia"),
                width="100%",
                color=textcolor.BODY.value,
                margin_top="20px",
            ),
             rx.text(
                 """Soy Francisco Fernández Bailén, desarrollador 
                        web full stack con experiencia en Angular y .NET, y 
                        conocimientos en diversas tecnologías como Astro, Node.js, 
                        Python, Java y bases de datos. Tengo experiencia 
                        liderando proyectos, organizando equipos con 
                        herramientas como Trello y trabajando con tecnologías 
                        innovadoras como reflex. Cuento con una discapacidad del 33%, 
                        lo que me permite acceder a incentivos para la contratación.""",
                 spacing=size.DEFAULT.value,
                 align_items="start",
                 color=textcolor.BODY.value,
                 margin_top="20px",
                 ),
                  position="relative",
                
                  
                  
                   
    )
