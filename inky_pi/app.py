#!/usr/bin/env python

class App():
  def __init__(self, state_manager):
    self.state = state_manager
    self.busy = True
  
  def setMode(self, mode):
    print('Mode set to {}'.format(mode))
    self.state.setState(mode)

  def set_busy(self):
    self.busy = True
    buttonshim.set_pixel(0x00, 0x00, 0xff)

  def set_idle(self):
    self.busy = False
    buttonshim.set_pixel(0x00, 0xff, 0x00)

if __name__ == '__main__':
  import buttonshim
  import signal
  from state_manager import StateManager
  from message_state import MessageState

  states = [
    MessageState(),
  ]

  state_manager = StateManager(states)

  app = App(state_manager)

  app.set_idle()

  @buttonshim.on_press(buttonshim.BUTTON_A)
  def button_a(button, pressed):
    return None

  @buttonshim.on_press(buttonshim.BUTTON_B)
  def button_b(button, pressed):
    return None

  @buttonshim.on_press(buttonshim.BUTTON_C)
  def button_c(button, pressed):
    if not app.busy:
      app.set_busy()
      app.state.currentState.c_button()
      app.set_idle()

  @buttonshim.on_press(buttonshim.BUTTON_D)
  def button_d(button, pressed):
    return None


  @buttonshim.on_press(buttonshim.BUTTON_E)
  def button_e(button, pressed):
    return None
    
  signal.pause()
