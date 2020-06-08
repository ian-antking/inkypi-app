#!/usr/bin/env python

class StateManager:
  def __init__(self, states):
    self.states = states
    self.currentState = states[0]
    self.currentState.enter_state()

  def findState(self, state_name):
    return next((state for state in self.states if state.name == state_name), None)

  def setState(self, state_name):
    if not self.currentState.name == state_name: 
      self.currentState.exit_state()
      self.currentState = self.findState(state_name)
      self.currentState.enter_state()
