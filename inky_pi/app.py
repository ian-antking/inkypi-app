#!/usr/bin/env python

class App():
  def __init__(self, state_manager):
    self.state = state_manager
    self.led = (0x00, 0x00, 0xff)
    self.busy = self.state.currentState.busy
  
  def setMode(self, mode):
    print('Mode set to {}'.format(mode))
    self.state.setState(mode)

  def update(self):
    self.busy = self.state.currentState.busy
    self.led = (0x00, 0xff, 0x00) if not self.busy else (0x00, 0x00, 0xff)


if __name__ == '__main__':
  import buttonshim
  import signal
  from state_manager import StateManager
  from message_state import MessageState

  buttonshim.set_pixel(0x00, 0x00, 0xff)

  states = [
    MessageState(),
  ]

  state_manager = StateManager(states)

  app = App(state_manager)

  @buttonshim.on_press(buttonshim.BUTTON_A)
  def button_a(button, pressed):
    return None


  @buttonshim.on_press(buttonshim.BUTTON_B)
  def button_b(button, pressed):
    return None


  @buttonshim.on_press(buttonshim.BUTTON_C)
  def button_c(button, pressed):
    if not app.busy:
      app.state.currentState.c_button()
    else: 
      print('busy')

  @buttonshim.on_press(buttonshim.BUTTON_D)
  def button_d(button, pressed):
    return None


  @buttonshim.on_press(buttonshim.BUTTON_E)
  def button_e(button, pressed):
    return None


  while True:
    previous_colour = app.led
    app.update()
    if not previous_colour == app.led:
      buttonshim.set_pixel(*app.led)
