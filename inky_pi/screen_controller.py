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

