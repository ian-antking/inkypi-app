#!/usr/bin/env python

class StateManager:
  def __init__(self, states):
    self.states = states
    self.state = states[0]
    self.state['enterState']()

  def findState(self, state_name):
    return next((state for state in self.states if state.name == state_name), None)

  def setState(self, state):
    self.state['exitState']()
    self.state = self.findState(state)
    self.state['enterState']()
  
  def getState(self):
    return self.state['name']
