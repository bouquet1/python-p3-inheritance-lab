#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    #super() function to call the constructor (test says positional arguments) of the base class.
    def __init__(self, first_name, last_name, knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def teach(self):
       return self.knowledge[random.randint(1, 8)]
    
    
    #here are alternatives. 
    # def teach(self):
    #    random_knowledge = random.choice(self.knowledge)
    #    return random_knowledge

    # def teach(self):
        # random_index = random.randint(0, len(self.knowledge) - 1)
        # random_knowledge = self.knowledge[random_index]
        # return random_knowledge


