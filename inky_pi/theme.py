class Theme():
  def __init__(self, theme, inky_display):
    if theme == 'light' or theme == 'mono_light':
      self.background = inky_display.WHITE
      self.text = inky_display.BLACK
      self.highlight = inky_display.RED if theme == 'light' else inky_display.BLACK
    if theme == 'dark' or theme == 'mono_dark':
      self.background = inky_display.BLACK
      self.text = inky_display.WHITE
      self.highlight = inky_display.RED if theme == 'dark' else inky_display.WHITE
    if theme == 'red':
      self.background = inky_display.RED
      self.text = inky_display.WHITE
      self.highlight = inky_display.BLACK
    inky_display.set_border(self.background)