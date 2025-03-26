import reflex as rx
from reflexWebPy.styles.styles import size as size
from reflexWebPy.styles.styles import TextColor as textcolor

def header_text() -> rx.Component:
    return  rx.text(
                 """Soy Francisco Fernández Bailén, desarrollador backend 
                 avanzado en Python y frameworks como Django y 
                 Flask. También tengo conocimientos en otras tecnologías 
                 como Node.js, .NET, bases de datos SQL y NoSQL, así 
                 como en arquitectura de APIs y optimización de rendimiento. 
                 He liderado proyectos, organizado equipos con herramientas 
                 como Trello y trabajado con tecnologías innovadoras como Reflex. 
                 Además, cuento con una discapacidad del 33%, lo que 
                 permite acceder a incentivos para la contratación.""",
                 spacing=size.DEFAULT.value,
                 align_items="start",
                 color=textcolor.BODY1.value,
                 margin_top="20px",
                 width="100%",
                    height="auto",
                    display="block",
                    justify="center",
                    
                    margin="20px",

                 ),
position="relative",

