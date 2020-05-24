#!/usr/bin/env python

class StateManager:
  def __init__(self, states):
    self.states = states
    self.currentState = states[0]
    self.currentState.enterState()

  def findState(self, state_name):
    return next((state for state in self.states if state.name == state_name), None)

  def setState(self, state):
    self.currentState.exitState()
    self.currentState = self.findState(state)
    self.currentState.enterState()
