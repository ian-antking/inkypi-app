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

  BUTTONS = [buttonshim.BUTTON_A, buttonshim.BUTTON_B, buttonshim.BUTTON_C, buttonshim.BUTTON_D, buttonshim.BUTTON_E]

  @buttonshim.on_release(BUTTONS)
  def button_r_handler(button, pressed):
    if not app.busy:
      button_handler = "handle_{}".format(buttonshim.NAMES[button]).lower()
      app.set_busy()
      buttonshim.set_pixel(*app.led)
      getattr(app.state.currentState, button_handler)()
      app.set_idle()


  while True:
    previous_colour = app.led
    app.update()
    if not previous_colour == app.led:
      buttonshim.set_pixel(*app.led)
