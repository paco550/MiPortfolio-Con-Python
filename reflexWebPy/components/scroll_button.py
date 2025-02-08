import reflex as rx

def scroll_button():
    return rx.box(
                rx.link(
                    rx.button(
                         rx.icon(tag="chevron_down", font_size="24px"),  # Ícono de flecha hacia abajo
                         width="50px",
                         height="50px",
                         border_radius="5px",  # Bordes cuadrados
                         background_color="rgba(0, 0, 0, 0.5)",  # Fondo semi-transparente
                         color="white",
                         _hover={"background_color": "rgba(0, 0, 0, 0.7)"},  # Cambio de color al pasar el cursor
                        ),
                            href="#header",  # Enlace a la sección con ID "header"
                            position="center",
                          )
                     )