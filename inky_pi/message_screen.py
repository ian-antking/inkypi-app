from PIL import ImageFont
from font_source_sans_pro import SourceSansProSemibold
from font_source_serif_pro import SourceSerifProSemibold
from screen import Screen

class MessageScreen(Screen):
  def __init__(self, colour_scheme, inky_display, message):
    super().__init__(colour_scheme, inky_display)

    message_font = ImageFont.truetype(SourceSerifProSemibold, 16)
    author_font = ImageFont.truetype(SourceSansProSemibold, 18)

    message_text = self.reflow_message(message['text'], int(self.width * 0.9), message_font)
    message_author = '- ' + message['author']

    tw, th = message_font.getsize(message_text)
    aw, ah = author_font.getsize(message_author)

    text_x = (self.width - int(self.width * 0.9) ) / 2
    text_y = (self.height - int(self.height * 0.9) ) / 2

    author_x = self.width - (aw + int(self.width * 0.1))
    author_y = self.height - (ah + int(self.height * 0.1))

    self.draw.multiline_text((text_x, text_y), message_text, self.theme.text, message_font)
    self.draw.text((author_x, author_y), message_author, self.theme.highlight, author_font)