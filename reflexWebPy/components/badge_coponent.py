import reflex as rx

from reflexWebPy.components.title import title

def badges_component():
    return rx.vstack(
        rx.hstack(
            title("Credenciales"),
            rx.html("""
                <div 
                    data-iframe-width="130" 
                    data-iframe-height="200" 
                    data-share-badge-id="b31d68ea-4fc8-492b-a57c-db46690ed499" 
                    # data-share-badge-host="https://www.credly.com">
                </div>
            """),
            rx.html("""
                <div 
                    data-iframe-width="130" 
                    data-iframe-height="200" 
                    data-share-badge-id="557aa98b-a358-4d4d-a725-6f14606287c8">
                </div>
            """),
             rx.html("""
                <div 
                    data-iframe-width="130" 
                    data-iframe-height="200" 
                    data-share-badge-id="a948315d-6439-4797-95d7-1c7b1cbcc748" 
                    >
                </div>
            """),
            spacing="4",
            wrap="wrap",
        ),
        rx.script(
            src="//cdn.credly.com/assets/utilities/embed.js",
            is_async=True
        )
    )