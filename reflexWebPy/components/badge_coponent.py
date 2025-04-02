import reflex as rx
from reflexWebPy.components.title import title

def badges_component():
    return rx.vstack(
        rx.hstack(
            title("Credenciales",),
            rx.link(
                rx.image(
                    src="/ibm-z-xplore-concepts (1).png",
                    height="150px",
                    width="130px",
                    margin="20px",
                ),
                href="https://www.credly.com/badges/b31d68ea-4fc8-492b-a57c-db46690ed499",
                is_external=True
            ),
            rx.link(
                rx.image(
                    src="/web-development-with-python.png",
                    height="150px",
                    width="130px",
                    margin="20px",
                ),
                href="https://www.credly.com/badges/557aa98b-a358-4d4d-a725-6f14606287c8",
                is_external=True
            ),
            rx.link(
                rx.image(
                    src="/working-in-a-digital-world-professional-skills.png",
                    height="150px",
                    width="130px",
                    margin="20px",
                ),
                href="https://www.credly.com/badges/a948315d-6439-4797-95d7-1c7b1cbcc748",
                is_external=True
            ),
            rx.link(
                rx.image(
                    src="/artificial-intelligence-fundamentals.png",
                    height="150px",
                    width="130px",
                    margin="20px",
                ),
                href="https://www.credly.com/badges/31c34f75-66a0-4ffc-ac80-650c9f210c3b/public_url",
                is_external=True
            ),
            
            spacing="4",
            margin="20px",
            height="auto",
                    # display="block",
                    # justify="center",
            wrap="wrap"
        )
    )