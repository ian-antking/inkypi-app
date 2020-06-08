#!/usr/bin/env python
BLUE = (0,0,127)
GREEN = (0,127,0)
RED = (127, 0, 0)
WHITE = (127, 127, 127)

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
  from state_manager import StateManager
  from states import states

  buttonshim.set_pixel(*BLUE)

  state_manager = StateManager(states)

  app = App(state_manager)

  BUTTONS = [buttonshim.BUTTON_A, buttonshim.BUTTON_B, buttonshim.BUTTON_C, buttonshim.BUTTON_D, buttonshim.BUTTON_E]

  button_was_held = False

  @buttonshim.on_press(BUTTONS)
  def press_handler(button, pressed):
    global button_was_held
    button_was_held = False

  @buttonshim.on_hold(buttonshim.BUTTON_A, hold_time=2)
  def hold_handler(button, pressed):
    global button_was_held
    button_was_held = True
    buttonshim.set_pixel(*WHITE)

  @buttonshim.on_release(BUTTONS)
  def release_handler(button, pressed):
    global button_was_held
    button_name = buttonshim.NAMES[button].lower()
    press_type = "long_" if button_was_held else ""
    if not app.busy:
      button_handler = "handle_{}{}".format(press_type, button_name)
      app.set_busy()
      buttonshim.set_pixel(*app.led)
      getattr(app.state.currentState, button_handler)()
      app.set_idle()

  while True:
    previous_colour = app.led
    app.update()
    if not previous_colour == app.led:
      buttonshim.set_pixel(*app.led)
