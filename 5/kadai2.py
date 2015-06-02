# -*- coding:utf-8 -*-
class Lab:
  members = None

  def __init__(self):
    self.members = []

  def add_member(self,new_member):
    self.members.append(new_member)

  def print_member(self):
    for member in self.members:
        member.print_info()

class LabMember:
    name = None
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name
class Student(LabMember):
  grade = 0

  def __init__(self,name):
    LabMember.__init__(self,name)

  def set_grade(self,grade):
    self.grade = grade

  def get_grade(self):
    return self.grade

  def promotion(self):
    self.grade+=1
  def print_info(self):
      print("student name = %s (%d)" % (self.name,self.grade))

class Professor(LabMember):
    room = 0

    def __init__(self,*args,**kwargs):
        LabMember.__init__(self,*args,**kwargs)
    def set_room(self,room):
        self.room = room
    def get_room(self):
        return self.room

    def print_info(self):
        print("professor name = %s (%d)"%(self.name,self.room))
