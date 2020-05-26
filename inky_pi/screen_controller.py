#!/usr/bin/env python
from inky import InkyPHAT
from alert_screen import AlertScreen
from prompt_screen import PromptScreen
from message_screen import MessageScreen

class ScreenController():
  def __init__(self):
        self.inky_display = InkyPHAT('red')
        self.screen_width = self.inky_display.WIDTH
        self.screen_height = self.inky_display.HEIGHT

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

