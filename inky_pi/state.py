#!/usr/bin/env python
from time import sleep
from screen_controller import ScreenController
class State():
  def __init__(self, name):
    self.name = name
    self.screen_controller = ScreenController()
    self.busy = True
    self.is_current_state = False
    self.next_state = name

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
    self.screen_controller.display_alert(self.name)
    self.set_idle()

  def update(self):
    return self.next_state

  def exit_state(self):
    self.set_busy()
    self.next_state = self.name
    self.set_inactive()

  def handle_a(self):
    self.next_state = self.name

  def handle_b(self):
    self.next_state = self.name

  def handle_c(self):
    self.next_state = self.name

  def handle_d(self):
    self.next_state = self.name
    
  def handle_e(self):
    self.next_state = self.name

  def handle_long_a(self):
    self.next_state = 'menu'

  def handle_long_b(self):
    self.next_state = self.name

  def handle_long_c(self):
    self.next_state = self.name

  def handle_long_d(self):
    self.next_state = self.name
    
  def handle_long_e(self):
    self.next_state = self.name
