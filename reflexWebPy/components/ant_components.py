import reflex as rx
from reflexWebPy.styles.colors import Color as Color

class FloatButton(rx.Component): 
    library = "antd"
    tag = "FloatButton"
    href="Data/Francisco Fernández Bailén (4).pdf"
    target="_blank"
    badge = {"dot": True, "color": Color.BADGE.value}

float_button = FloatButton.create
