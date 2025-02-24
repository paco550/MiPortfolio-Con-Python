import reflex as rx
from reflexWebPy import utils
from reflexWebPy.components.hero_section import hero
from reflexWebPy.components.navbar import navbar
from reflexWebPy.views.education_section import education_section
from reflexWebPy.views.header import header
from reflexWebPy.views.links import links
from reflexWebPy.components.footer import footer
import reflexWebPy.styles.styles as styles
from reflexWebPy.rutas import Rutas


@rx.page(
    route=Rutas.CURSOS.value,
    title=utils.cursos_title, 
    description=utils.cursos_descripcion,
    image=utils.imagen,
    meta=utils.cursos_meta,    
)
def cursos() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
         
        # hero(),
       
        rx.center(
            rx.vstack(
                header(),
                 education_section(),
                
                # links(),
                max_whith=styles.MAX_WIDTH,
                width="100%",
                margin= styles.size.MEDIUM_BIG.value,  
                margin_top="20px",   
            ),
        ),
       rx.center(footer()),
    )