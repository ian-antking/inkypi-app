from PIL import ImageFont
from font_source_sans_pro import SourceSansProSemibold
from screen import Screen

class PromptScreen(Screen):
  def __init__(self, colour_scheme, inky_display, message, instruction):
    super().__init__(colour_scheme, inky_display)