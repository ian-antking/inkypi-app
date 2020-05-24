#!/usr/bin/env python

class StateManager:
  def __init__(self, states):
    self.states = states
    self.state = list(states.values())[0]

  def setState(self, state):
    self.state['exit']()
    self.state = self.states[state]
    self.state['enter']()
  
  def getState(self):
    return self.state['name']

if __name__ == '__main__':
  states = {
    'namebadge': {
      'name': 'namebadge',
      'enter': lambda : print('setting mode to namebadge'),
      'execute': lambda : print('executing namebadge'),
      'exit': lambda : print('exiting nambadge')
    },
    'message': {
      'name': 'message',
      'enter': lambda : print('setting mode to message'),
      'execute': lambda : print('executing message'),
      'exit': lambda : print('exiting message')
    }
  }

  state_manager = StateManager(states)

  state_manager.state['execute']()

  print(state_manager.getState())

  state_manager.setState('message')

  state_manager.state['execute']()