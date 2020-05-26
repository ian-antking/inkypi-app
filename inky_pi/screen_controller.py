#!/usr/bin/env python
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_source_serif_pro import SourceSerifProSemibold
from font_source_sans_pro import SourceSansProSemibold
from screen import Screen
from alert_screen import AlertScreen
from prompt_screen import PromptScreen
from message_screen import MessageScreen

class ScreenController():
  def __init__(self):
        self.inky_display = InkyPHAT('red')
        self.screen_width = self.inky_display.WIDTH
        self.screen_height = self.inky_display.HEIGHT

  def reflow_message(self, message, width, font, quote=True):
    words = message.split(" ")
    reflowed = '"' if quote else ''
    line_length = 0

    end_of_string = '"' if quote else ''

    for i in range(len(words)):
        word = words[i] + " "
        word_length = font.getsize(word)[0]
        line_length += word_length

        if line_length < width:
            reflowed += word
        else:
            line_length = word_length
            reflowed = reflowed[:-1] + "\n  " + word

    reflowed = reflowed.rstrip() + end_of_string

    return reflowed

  def display_message(self, message, theme = 'light'):
    screen = MessageScreen(message['theme'] or theme, self.inky_display, message)

    message_font = ImageFont.truetype(SourceSerifProSemibold, 16)
    author_font = ImageFont.truetype(SourceSansProSemibold, 18)

    message_text = self.reflow_message(message['text'], int(self.screen_width * 0.9), message_font)
    message_author = '- ' + message['author']

    print(message_text, message_author)

    tw, th = message_font.getsize(message_text)
    aw, ah = author_font.getsize(message_author)

    text_x = (self.screen_width - int(self.screen_width * 0.9) ) / 2
    text_y = (self.screen_height - int(self.screen_height * 0.9) ) / 2

    author_x = self.screen_width - (aw + int(self.screen_width * 0.1))
    author_y = self.screen_height - (ah + int(self.screen_height * 0.1))

    screen.draw.multiline_text((text_x, text_y), message_text, screen.theme.text, message_font)
    screen.draw.text((author_x, author_y), message_author, screen.theme.highlight, author_font)
    self.inky_display.set_image(screen.image)

    self.inky_display.show()

  def display_alert(self, message, theme = 'light'):
    screen = AlertScreen(theme, self.inky_display, message)
    self.inky_display.set_image(screen.image)
    self.inky_display.show()

  def display_prompt(self, message, instruction, theme = 'light'):
    screen = PromptScreen(theme, self.inky_display, message, instruction)
    self.inky_display.set_image(screen.image)
    self.inky_display.show()

