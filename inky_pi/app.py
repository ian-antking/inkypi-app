#!/usr/bin/env python

class App():
  def __init__(self, state_manager):
    self.state = state_manager
  
  def setMode(self, mode):
    print('Mode set to {}'.format(mode))
    self.state.setState(mode)


if __name__ == '__main__':
  import buttonshim
  import signal
  from state import State
  from state_manager import StateManager
  from message_state import MessageState

  states = [
    MessageState(),
    State('mode a'),
    State('mode b'),
    State('mode c'),
    State('mode d')
  ]

  state_manager = StateManager(states)

  app = App(state_manager)

  buttonshim.set_pixel(0xff, 0x00, 0x00)

  @buttonshim.on_press(buttonshim.BUTTON_A)
  def button_a(button, pressed):
    buttonshim.set_pixel(0x94, 0x00, 0xd3)
    app.setMode('mode a')

  @buttonshim.on_press(buttonshim.BUTTON_B)
  def button_b(button, pressed):
    buttonshim.set_pixel(0x00, 0x00, 0xff)
    app.setMode('mode b')

  @buttonshim.on_press(buttonshim.BUTTON_C)
  def button_c(button, pressed):
    buttonshim.set_pixel(0x00, 0xff, 0x00)
    app.setMode('mode c')

  @buttonshim.on_press(buttonshim.BUTTON_D)
  def button_d(button, pressed):
    buttonshim.set_pixel(0xff, 0xff, 0x00)
    app.setMode('mode d')

  @buttonshim.on_press(buttonshim.BUTTON_E)
  def button_e(button, pressed):
    buttonshim.set_pixel(0xff, 0x00, 0x00)
    app.setMode('message')

  while True:
    app.state.currentState.update()
