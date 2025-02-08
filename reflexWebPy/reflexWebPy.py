
import reflex as rx
from reflexWebPy.components.hero_section import hero
from reflexWebPy.components.navbar import navbar
from reflexWebPy.views.header.header import header
from reflexWebPy.views.links.links import links
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
app.add_page(index)
app._compile()
