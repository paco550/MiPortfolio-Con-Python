import reflex as rx
from reflexWebPy import utils
from reflexWebPy.components.header_text import header_text
from reflexWebPy.components.hero_section import hero
from reflexWebPy.components.navbar import navbar
from reflexWebPy.views.header import header
from reflexWebPy.views.links import links
from reflexWebPy.components.footer import footer
import reflexWebPy.styles.styles as styles


@rx.page(
    title=utils.index_titulo, 
    description=utils.index_descripcion,
    image=utils.imagen,
    meta=utils.index_meta,    
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        hero(),
        rx.center(
            rx.vstack(
                header(),
                header_text(),
                links(),
                max_whith=styles.MAX_WIDTH,
                width="100%",
                margin= styles.size.MEDIUM_BIG.value,     
            ),
        ),
       rx.center(footer()),
    )