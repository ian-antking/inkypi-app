#!/usr/bin/env python
from time import sleep
from screen_controller import ScreenController
class State():
  def __init__(self, name):
    self.name = name
    self.screen_controller = ScreenController()

  def enterState(self):
    print('entering {} mode'.format(self.name))
    self.screen_controller.display_message(self.name)

  def update(self):
    sleep(1)

  def exitState(self):
    print('exiting {} mode'.format(self.name))
