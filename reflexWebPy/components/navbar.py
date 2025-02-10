import reflex as rx
from reflexWebPy.styles.styles import size as size
from reflexWebPy.styles.colors import TextColor as textcolor


def navbar() -> rx.components:
    return rx.box(
        rx.hstack(
            rx.link("F. Fernández", href="#inicio", font_size="24px", font_weight="bold", color=textcolor.BODY.value,),
            rx.spacer(),
            rx.hstack(
                rx.link("Proyectos", href="#proyectos", padding="1rem", color=textcolor.BODY.value,),
                # rx.link("Estudios", href="#estudios", padding="1rem"),
                rx.link("Comunidad", href="#comunidad", padding="1rem", color=textcolor.BODY.value,),
            ),
            align_items="center",
            padding="1rem",
        ),
        position="fixed",
        top="0",
        width="100%",
        height="0px",
        background_color="rgba(255, 255, 255, 0.5)",  # Fondo blanco con 50% de transparencia
        backdrop_filter="blur(10px)",  # Efecto de desenfoque de fondo
        z_index="1000",  # Asegura que el navbar esté por encima de otros elementos
    ),
    