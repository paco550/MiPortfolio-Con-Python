from enum import Enum
import reflex as rx
from .colors import Color as color, TextColor
from .fonts import Font as font


MAX_WIDTH = "600PX"

class size(Enum):
    VERY_SMALL = "0.1em"
    SMALL = "0.5em"
    MEDIUM = "0.8EM"
    DEFAULT = "1em"
    MEDIUM_BIG = "2em"
    BIG = "13em"

# styles

BASE_STYLE = {
    "font_family": font.DEFAULT.value,
    "background_color": color.BACKGROUND.value,
   rx.button: {
       "width": "100%",
       "height": "100%",
       "display": "block",
       "padding": size.SMALL.value,
       "border_radius": size.DEFAULT.value,
       "color": TextColor.HEADER.value,
       "background_color": color.CONTENT.value,
       "_hover": {
           "background_color": color.SECONDARY.value,
       }

   },
   rx.link:{
       
   }
}

navbar_title_style = dict(
    font_family=font.LOGO.value,
    font_size=size.MEDIUM.value,
)

title_style = dict(
    font_family=font.TITLE.value,
    size="md",
    width="100%",
    padding_top=size.DEFAULT.value,
    color=TextColor.HEADER.value,
)

button_title_style = dict(
    font_family=font.TITLE.value,
    font_size=size.DEFAULT.value, 
    color=TextColor.HEADER.value,  
)

button_body_style = dict(
    font_size=size.MEDIUM.value,
    color=TextColor.BODY.value,
)

tex_animated= {
    "animation": "fadeIn 2s infinite",
    "background_clip": "text",
    "background_image": "linear-gradient(90deg, #f12711, #f5af19, #f5af19, #f12711)",
}