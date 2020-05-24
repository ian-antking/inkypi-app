#!/usr/bin/env python

class State():
  def __init__(self, name):
    self.name = name

  def enter(self):
    print('entering {} mode'.format(name))

  def exit(self):
    print('exiting {} mode'.format(name))
