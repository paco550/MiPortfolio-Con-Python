import reflex as rx
from reflexWebPy.components.linksButton import links_button
from reflexWebPy.components.title import title

def links() -> rx.components:
    return rx.vstack(
        title("Proyectos"),
        links_button(
            "MiPortfolio-Con-Python",
             "Un portfolio profesional desarrollado con Reflex.", 
             "https://github.com/paco550/MiPortfolio-Con-Python"
             ),
        links_button(
            "MiFacturacion",
             "Una aplicación full-stack para gestionar cuentas y finanzas.", 
             "https://github.com/paco550/MiFacturacion"
             ),
        links_button(
            "devNotes",
             "una página de documentación creada con Astro para organizar y compartir notas de desarrollo.",
             "https://devnotess.netlify.app/"
             ),
        links_button(
            "Chat-backend",
            "Este proyecto es un backend para un sistema de chat en tiempo real.",
            "https://github.com/paco550/Chat-backend"
            ),
            
        title("comunidad"),
        links_button(
            "twitch",
             "de lunes a viernes", 
             "https://www.twitch.tv/"
             ),
        links_button(
            "Youtube",
             "tutoriales semanales", 
             "https://www.youtube.com/"
             ),
        links_button(
            "Youtube (secundario)",
             "kakaka",
             "https://www.youtube.com/watch?v=n2YrGsXJC6Y&t=8709s"
             ),
        links_button(
            "Discord",
            "chat comuniti",
            "https://discord.com/channels/729672926432985098/809090465760149545"
            ),
            width="100%",
    ),
