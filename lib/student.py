#!/usr/bin/env python

from user import User
from teacher import Teacher

# class Student(User, Teacher): this line gave an error: "student.py X Cannot create consistent method ordering" = ambiguous MRO.
class Student(User, Teacher):
    
    def __init__(self, first_name, last_name, knowledge):
        #Initialize attrubites using super (forum answer)
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def learn(self):
        pass


#  I've tried this for MRO errro but it didin't work. 
    # def __init__(self, first_name, last_name, knowledge):
        # Initialize attributes from User
        # super(User, self).__init__(first_name, last_name)
        # Initialize attributes from Teacher
        # super(Teacher, self).__init__(knowledge)

#  I've tried this for MRO errro but it didin't work, too. 
    # def __init__(self, first_name, last_name, knowledge):
        # Initialize attributes from User
        # User.__init__(self, first_name, last_name, knowledge)
        # Initialize attributes from Teacher
        # Teacher.__init__(self, knowledge)


