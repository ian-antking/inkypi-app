#!/usr/bin/env python
BLUE = (0,0,127)
GREEN = (0,127,0)
RED = (127, 0, 0)

class App():
  def __init__(self, state_manager):
    self.state = state_manager
    self.led = BLUE
    self.busy = self.state.busy

  def set_busy(self):
    self.busy = True

  def set_idle(self):
    self.busy = False

  def update(self):
    self.state.update()
    self.busy = self.state.busy
    self.led = GREEN if not self.busy else BLUE

if __name__ == '__main__':
  import buttonshim
  import signal
  import os
  from state_manager import StateManager
  from message_state import MessageState
  from dotenv import load_dotenv
  from menu_state import MenuState

  load_dotenv()

  mqtt_broker = os.getenv('MQTT_BROKER')
  message_topic = os.getenv('MESSAGE_TOPIC')

  buttonshim.set_pixel(*BLUE)

  states = [
    MenuState('menu'),
    MessageState('message', mqtt_broker, message_topic),
  ]

  state_manager = StateManager(states)

  app = App(state_manager)

  c_button_held = False

  @buttonshim.on_press(buttonshim.BUTTON_A)
  def button_a(button, pressed):
    if not app.busy:
      app.set_busy()
      buttonshim.set_pixel(*app.led)
      app.state.currentState.a_button()
      app.set_idle()

  @buttonshim.on_press(buttonshim.BUTTON_B)
  def button_b(button, pressed):
    if not app.busy:
      app.state.currentState.b_button()

  @buttonshim.on_press(buttonshim.BUTTON_C)
  def button_b(button, pressed):
    global c_button_held
    c_button_held = False

  @buttonshim.on_hold(buttonshim.BUTTON_C, hold_time=2)
  def hold_handler(button):
    global c_button_held
    c_button_held = True

  @buttonshim.on_release(buttonshim.BUTTON_C)
  def button_c(button, pressed):
    if not app.busy and not c_button_held:
      app.state.currentState.c_button()
    elif not app.busy and c_button_held:
      app.state.currentState.menu_button()

  @buttonshim.on_press(buttonshim.BUTTON_D)
  def button_d(button, pressed):
    if not app.busy:
      app.state.currentState.d_button()


  @buttonshim.on_press(buttonshim.BUTTON_E)
  def button_e(button, pressed):
    if not app.busy:
      app.state.currentState.e_button()


  while True:
    previous_colour = app.led
    app.update()
    if not previous_colour == app.led:
      buttonshim.set_pixel(*app.led)
