#!/usr/bin/env python

from user import User
from teacher import Teacher

class Student(User):
    
    def __init__(self, first_name, last_name, knowledge = []):
        #Initialize attrubites using super 
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def learn(self, string):
        self.string = string
        return self.knowledge.append(self.string)

