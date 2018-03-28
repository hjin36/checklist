#! /usr/bin/env python3
"""
This module is for defining all the checklist item classes. Since it's the first time I'm trying to develop a real software, I'm not
sure if I'll use this module as a top-level module or not
"""

"""This class defines one item on the checklist. It'll be used as the top-level class. I planned to add an value attribute
on it."""
class Item:
	def __init__(self,name,deadline,category,note=''):
		self.name = name
		self.deadline = deadline
		self.category = category
		self.note = note

"""This class defines the category, which includes a bunch of items"""
class Category:
	def __init__(self,name,value,*args):
		self.name = name
		self.value = value
		self.items = list(args)
	def addItem(self,item):
		self.items.append(item)
	def dropItem(self,item):
		self.items.remove(item) 
	def showAll(self):
		for i in self.items:
			print(i.name)



if __name__ == '__main__':
	academics = Category('Academics',10)
	hobby = Category('hobby',5,'piano','coding')
	study = Item('study Python','June 1, 2018','Academics')
	print([study.name,study.deadline,study.category])
	print([academics.name,academics.value,academics.items])
	print([hobby.name,hobby.value,hobby.items])
	academics.addItem(study)
	academics.showAll()
