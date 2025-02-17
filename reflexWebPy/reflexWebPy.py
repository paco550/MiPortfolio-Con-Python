
import reflex as rx
from reflexWebPy.components.hero_section import hero
from reflexWebPy.components.navbar import navbar
from reflexWebPy.views.header import header
from reflexWebPy.views.links import links
from reflexWebPy.components.footer import footer
import reflexWebPy.styles.styles as styles

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        hero(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_whith=styles.MAX_WIDTH,
                width="100%",
                margin= styles.size.BIG.value,     
            ),
        ),
       rx.center(footer()),
    )
    
    

app = rx.App(
    style=styles.BASE_STYLE
)

titulo = "F.Fernández"
descripcion = "hola soy Francisco Fernández, desarrollador de software"
imagen = "https://ffernandez.netlify.app"

meta = [
    {"name": "theme_color", "content": "#FFFFFF"},
    {"property": "og:type", "content": "website"},
    {"property": "og:title", "content": titulo},
    {"property": "og:description", "content": descripcion}, 
    {"property": "og:image", "content": imagen},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:title", "content": titulo},
    {"name": "twitter:description", "content": descripcion},
    {"name": "twitter:image", "content": imagen},
    {"name": "twitter:site", "content": "@F.Fernandez"}
]

app.add_page(
    index,
    title=titulo,
    description=descripcion, 
    image=imagen,
    meta=meta
)
