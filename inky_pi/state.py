#!/usr/bin/env python
from time import sleep
from screen_controller import ScreenController
class State():
  def __init__(self, name):
    self.name = name
    self.screen_controller = ScreenController()
    self.busy = False

  def busy(self):
    self.busy = True

  def idle(self):
    self.busy = False

  def enterState(self):
    print('entering {}'.format(self.name))
    self.screen_controller.display_message(self.name)

  def update(self):
    sleep(1)

  def exitState(self):
    print('exiting {}'.format(self.name))
