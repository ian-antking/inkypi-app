from PIL import ImageFont
from font_source_sans_pro import SourceSansProSemibold
from font_source_serif_pro import SourceSerifProSemibold
from screen import Screen

class messageScreen(Screen):
  def __init__(self, colour_scheme, inky_display, message):
    super().__init__(colour_scheme, inky_display)