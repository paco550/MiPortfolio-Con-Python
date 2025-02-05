import reflex as rx
from reflexWebPy.components.linksButton import links_button
from reflexWebPy.components.title import title

def links() -> rx.components:
    return rx.vstack(
        title("Proyectos"),
        links_button(
            "MiPortfolio-Con-Python",
             "Un portfolio profesional desarrollado con Reflex.", 
             "icons/address-card-solid.svg",
             "https://github.com/paco550/MiPortfolio-Con-Python"
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
        links_button(
            "Chat-backend",
            "Este proyecto es un backend para un sistema de chat en tiempo real.",
            "icons/code-solid.svg",
            "https://github.com/paco550/Chat-backend"
            ),

              title("Estudios"),
        links_button(
            "MiPortfolio-Con-Python",
             "Un portfolio profesional desarrollado con Reflex.", 
             "icons/github-brands-solid.svg",
             "https://github.com/paco550/MiPortfolio-Con-Python"
             ),
        links_button(
            "MiFacturacion",
             "Una aplicación full-stack para gestionar cuentas y finanzas.", 
             "icons/github-brands-solid.svg",
             "https://github.com/paco550/MiFacturacion"
             ),
        links_button(
            "devNotes",
             "una página de documentación creada con Astro para organizar y compartir notas de desarrollo.",
             "icons/github-brands-solid.svg",
             "https://devnotess.netlify.app/"
             ),
        links_button(
            "Chat-backend",
            "Este proyecto es un backend para un sistema de chat en tiempo real.",
            "icons/github-brands-solid.svg",
            "https://github.com/paco550/Chat-backend"
            ),
            
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
        # links_button(
        #     "Youtube (secundario)",
        #      "kakaka",
        #      "https://www.youtube.com/watch?v=n2YrGsXJC6Y&t=8709s"
        #      ),
        links_button(
            "Discord",
            "chat comuniti",
            "icons/discord-brands-solid.svg",
            "https://discord.com/channels/729672926432985098/809090465760149545"
            ),
            width="100%",
    ),
