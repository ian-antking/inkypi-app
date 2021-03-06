#!/usr/bin/env python

class StateManager:
  def __init__(self, states):
    self.states = states
    self.busy = True
    self.currentState = states[0]
    self.currentState.enter_state()

  def find_state(self, state_name):
    return next((state for state in self.states if state.name == state_name), None)

  def set_state(self, state_name):
    self.busy = True
    self.currentState.exit_state()
    self.currentState = self.find_state(state_name)
    self.currentState.enter_state()

  def update(self):
    self.busy = self.currentState.busy
    state_name = self.currentState.update()
    if not self.currentState.name == state_name: 
      self.set_state(state_name)
