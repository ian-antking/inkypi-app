#!/usr/bin/env python
from screen_controller import ScreenController
class State():
  def __init__(self, name):
    self.name = name
    self.screen_controller = ScreenController()

  def enter(self):
    print('entering {} mode'.format(name))
    screen_controller.display_message(self.name)

  def exit(self):
    print('exiting {} mode'.format(name))
