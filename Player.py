from random import random
from browser import window
j = window.jQuery

class Player:
  selected = False
  def __init__(self, color,spel_plan,shape):
   self.id = 'id' + str(random()).split('.')[1]
   self.color = color
   self.spel_plan = spel_plan
   self.bind_events()
   self.shape = shape
  
  def bind_events(self):
    j('body').on('click', f'#{self.id}', self.click)

  def animationEnd(self, event):
    j(event.target).removeClass('blueani')
    j(event.target).removeClass('redani')

  def click(self, event):
    if self.selected:
      self.selected = False
      j(f'#{self.spel_plan.id} .player').css('opacity', 0.3)
    else:
      self.selected = True
    # Dim rest of shapes except the user clicked on
      for spelare in self.spel_plan.spelar_lista:
          if spelare.color is not self.color and spelare.selected:
          # put attack here
            #j(f'.{spelare.color}{spelare.shape}').removeClass(f'{spelare.color}ani')
            print(f'{spelare.color} {spelare.shape} is hitting {self.color} {self.shape}')
            j(f'.{spelare.color}{spelare.shape}').addClass(f'{spelare.color}ani').on('animationend', self.animationEnd)
            j(f'#{self.spel_plan.id} .player').css('opacity', 0.3)
          else:
            print('that is a teammate')
            j(f'#{self.spel_plan.id} .player').css('opacity', 0.3)
            continue

          for s in self.spel_plan.spelar_lista:
            s.selected = False
          break

      j(f'#{self.spel_plan.id} .player').css('opacity', 1)
      if self.shape=='cube':
        j(f'#{self.spel_plan.id} .{self.color}Triangle').css('opacity', 0.3)
      elif self.shape=='triangle':
        j(f'#{self.spel_plan.id} .{self.color}Cube').css('opacity', 0.3)

      # Undim me
      j(f'#{self.id}').css('opacity', 1)

  def __str__(self):
    if self.shape == 'cube':
      return f"""
        <div class="{self.color}cube player" id="{self.id}">
        </div>
        """
    elif self.shape == 'triangle':
      return f"""
        <div class="{self.color}triangle player" id="{self.id}">
        </div>
        """      
