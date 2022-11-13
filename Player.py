from random import random
from browser import window
j = window.jQuery

# INTE KLART, SAKNAR ÅTMINSTONE SPELARLOOPEN OCH NÄTVERK


class Player:
  selected = False
  maxCubeHealth = 50.0
  currentCubeHealth = 50.0
  maxTriangleHealth = 30.0
  currentTriangleHealth = 30.0
  healthDashes = 5
  def __init__(self, color,spel_plan,shape, health):
   self.id = 'id' + str(random()).split('.')[1]
   self.color = color
   self.spel_plan = spel_plan
   self.bind_events()
   self.shape = shape
   self.health = self.maxCubeHealth
   if self.shape == 'cube':
    self.health = 50
   else:
    self.health = 30
  
  def bind_events(self):
    j('body').on('click', f'#{self.id}', self.click)

  def animationEnd(self, event):
    j(event.target).removeClass('blueani')
    j(event.target).removeClass('redani')

  def cubeDealDamage(self):
    cubeMaxDamage = 8
    cubeMinDamage = 1
    cubeDamage = (random.randint(cubeMinDamage,cubeMaxDamage))
    #return cubeDamage

  def triangleDealDamage(self):
    triangleMaxDamage = 15
    triangleMinDamage = 3
    triangleDamage = (random.randint(triangleMinDamage, triangleMaxDamage))
    #return triangleDamage


  def cubeHealth(self):
    dashConvert = int(self.maxCubeHealth/self.healthDashes)
    currentDashes = int(self.currentCubeHealth/dashConvert)
    remainingHealth = self.healthDashes - currentDashes

    healthDisplay = '-' * currentDashes
    remainingDisplay = ' ' * remainingHealth
    percent = str(int((self.currentCubeHealth/self.maxCubeHealth) * 100)) + "%"

    print("|" + healthDisplay +  remainingDisplay + "|")
    print("              " + percent)

  def triangleHealth(self):
    dashConvert = int(self.maxTriangleHealth/self.healthDashes)
    currentDashes = int(self.currentTriangleHealth/dashConvert)
    remainingHealth = self.healthDashes - currentDashes

    healthDisplay = '-' * currentDashes
    remainingDisplay = ' ' * remainingHealth
    percent = str(int((self.currentTriangleHealth/self.maxCubeHealth) * 100)) + "%"

    print("|" + healthDisplay +  remainingDisplay + "|")
    print("              " + percent)

  def TakeDamage(self):
    # fungerar inte för tillfället
    if self.shape == 'cube':
      self.health - self.cubeDealDamage
    else:
      self.health - self.triangleDealDamage
    #if self.cubeHealth == 0:
      #j(f'{self.color} {self.shape} is dead, dont beat a dead corpse.')
    #else:
      #self.cubeHealth - self.cubeDealDamage


  #def triangleTakeDamage(self):
    #if self.triangleHealth == 0:
      #j(f'{self.color} {self.shape} is dead, dont beat a dead corpse.')
    #else:
      #self.triangleHealth - self.cubeDealDamage

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
            # fungerar inte för tillfället
            print(f'{spelare.color} {spelare.shape} hit {self.color} {self.shape} for {self.cubeDealDamage}')
            

            #j(f'.{spelare.color}{spelare.shape}').removeClass(f'{spelare.color}ani')
            print(f'{spelare.color} {spelare.shape} is hitting {self.color} {self.shape}')
            j(f'.{spelare.color}{spelare.shape}').addClass(f'{spelare.color}ani').on('animationend', self.animationEnd)
            j(f'#{self.spel_plan.id} .player').css('opacity', 0.3)
          else:
            #j(f'#{self.spel_plan.id} .player').css('opacity', 0.3)
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
