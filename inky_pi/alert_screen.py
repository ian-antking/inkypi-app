from PIL import ImageFont
from font_source_sans_pro import SourceSansProSemibold
from screen import Screen

class AlertScreen(Screen):
  def __init__(self, colour_scheme, inky_display, message):
    super().__init__(colour_scheme, inky_display)

    message_font = ImageFont.truetype(SourceSansProSemibold, 18)
    message_text = self.reflow_message(message, self.width, message_font, False)

    tw, th = message_font.getsize(message)

    text_x = (self.width  / 2) - (tw / 2)
    text_y = (self.height / 2) - (th / 2)

    self.draw.rectangle((0, 0, self.width, (self.height - th) / 2), fill=self.theme.highlight)
    self.draw.rectangle((0, text_y + th + 5, self.width, self.height), fill=self.theme.highlight)

    self.render_hatches(24, 3)

    self.draw.multiline_text((text_x, text_y), message_text, self.theme.text, message_font, align='center')