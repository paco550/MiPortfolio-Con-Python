import reflex as rx
from reflexWebPy.components.badge_coponent import badges_component
from reflexWebPy.components.linksButton import links_button
from reflexWebPy.components.title import title
from reflexWebPy.rutas import Rutas

def links() -> rx.components:
    return rx.vstack(
        rx.section(id="proyectos"),
        title("Proyectos"),
        links_button(
            "Conecta 4",
            "Un juego de conecta 4 desarrollado con Reflex.",
             "icons/python.svg",
             "https://conecta4-gray-book.reflex.run/"
             ),
        links_button(
            "Pasarela de pago con Stripe",
            "Implementación de una pasarela de pago segura y eficiente con Stripe, permitiendo procesar transacciones en línea mediante tarjetas de crédito en múltiples divisas.",
            "icons/python.svg",
            "https://github.com/paco550/pasarela-pago-stripe"
            ),
        links_button(
            "Bot de twitter",
            "Un bot de twitter que publica frases de programación.", 
             "icons/python.svg",
             "https://github.com/paco550/bot_twitter"
             ),
        links_button(
            "MiFacturacion",
             "Una aplicación full-stack para gestionar cuentas y finanzas.", 
             "icons/code-solid.svg",
             "https://github.com/paco550/MiFacturacion"
             ),
        links_button(
            "devNotes",
             "una página de documentación creada con Astro para organizar y compartir notas de desarrollo.",
             "icons/cabeza-gorila.png",
             "https://devnotess.netlify.app/"
             ), 
            rx.box(
                badges_component(),
                width="100%",
                align_items="center",
                justify_content="center",
                margin_top="30px",
                
            ),
             rx.section(id="comunidad"),
             title("comunidad"),
        links_button(
            "GitHub",
            "Soluciones creativas y código eficiente.", 
            "icons/github-brands-solid.svg",
            "https://github.com/paco550"
             ),
        links_button(
            "linkedin",
             "Impulso proyectos tecnológicos con innovación y eficiencia.", 
             "icons/linkedin-brands-solid.svg",
             "https://www.linkedin.com/in/francisco-fern%C3%A1ndez-bail%C3%A9n/"
             ),
        links_button(
            "Discord",
            "chat comuniti",
            "icons/discord-brands-solid.svg",
            "https://discord.com/channels/729672926432985098/809090465760149545"
            ),

            rx.section(id="cursos"),
             title("Cursos"),
        links_button(
            "Cursos",
            "Mis cursos de programacion.", 
            "icons/code-solid.svg",
            Rutas.CURSOS.value,
            is_external=False
             ),
             width="100%",
            
    )
           

    
