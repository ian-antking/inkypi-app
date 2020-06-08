#!/usr/bin/env python
from time import sleep
from screen_controller import ScreenController
class State():
  def __init__(self, name):
    self.name = name
    self.screen_controller = ScreenController()
    self.busy = False
    self.is_current_state = False

  def set_busy(self):
    self.busy = True

  def set_idle(self):
    self.busy = False

  def set_active(self):
    self.is_current_state = True

  def set_inactive(self):
    self.is_current_state = False

  def enter_state(self):
    self.set_active()
    self.set_busy()
    self.screen_controller.display_message(self.name)
    self.set_idle()

  def update(self):
    return None

  def exit_state(self):
    self.set_inactive()
