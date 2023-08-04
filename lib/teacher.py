#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    #super() function to call the constructor (test says positional arguments) of the base class.
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge =[
            "programming is hard, but it's worth it",
            "Python function call definition",
            "object-oriented teacher instance",
        ]

    def teach(self):
       random_knowledge = random.choice(self.knowledge)
       return random_knowledge
    
    #test calls for random.randint but random.choice worked. here is alternative with it.
    # def teach(self):
        # random_index = random.randint(0, len(self.knowledge) - 1)
        # random_knowledge = self.knowledge[random_index]
        # return random_knowledge


