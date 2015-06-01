# -*- coding:utf-8 -*-
class Lab:
  members = None

  def __init__(self):
    self.members = []

  def add_member(self,new_member):
    self.members.append(new_member)

  def print_member(self):
    for member in self.members:
class Student:
  name = None
  grade = 0

  def __init__(self,name):
    self.name = name

  def set_grade(self,grade):
    self.grade = grade

  def get_grade(self):
    return self.grade

  def get_name(self):
    return self.name
  
  def promotion(self):
    self.grade+=1
