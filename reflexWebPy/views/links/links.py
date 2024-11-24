import reflex as rx
from reflexWebPy.components.linksButton import links_button
from reflexWebPy.components.title import title

def links() -> rx.components:
    return rx.vstack(
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
