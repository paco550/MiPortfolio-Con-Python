import reflex as rx
from reflexWebPy.styles.styles import size as size
from reflexWebPy.styles.styles import TextColor as textcolor

def header_text() -> rx.Component:
    return  rx.text(
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
                 color=textcolor.BODY1.value,
                 margin_top="20px",
                 ),
position="relative",

