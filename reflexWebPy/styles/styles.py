from enum import Enum
import reflex as rx
from .colors import Color as color, TextColor


MAX_WIDTH = "600PX"

class size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8EM"
    DEFAULT = "1em"
    BIG = "13em"

# styles

BASE_STYLE = {
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

title_style = dict(
    size="md",
    width="100%",
    padding_top=size.DEFAULT.value,
    color=TextColor.HEADER.value,
)

button_title_style = dict(
    font_size=size.DEFAULT.value, 
    color=TextColor.HEADER.value,  
)

button_body_style = dict(
    font_size=size.SMALL.value,
    color=TextColor.BODY.value,
)