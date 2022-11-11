from random import random
from browser import window
j = window.jQuery
from SpelPlan import SpelPlan
class Application:

    def __init__(self):
        # create a unique id 
        # (that is also an allowed id in html)
        self.id = 'id' + str(random()).split('.')[1]
        
        self.spel_plan = SpelPlan()
 

    def __str__(self):
        return f"""
            <div class="application" id={self.id}>
              {''.join(str(self.spel_plan))}
            </div>
        """
