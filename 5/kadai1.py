# -*- coding:utf-8 -*-
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

  def put(self):
      print("student name= %s (%d)" %(self.name,self.grade))
