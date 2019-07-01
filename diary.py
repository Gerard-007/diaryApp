#!/usr/bin/env python3
from collections import OrderedDict
import sys
import os
import datetime

from peewee import *


db = SqliteDatabase('diary.db')

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = db

		
		
def initialize():
    '''Create the database table if not created'''
    db.connect()
    db.create_tables([Entry], safe=True)
	
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
    
def menu_loop():
	"""Show the menu"""
	choice = None
	
	while choice != 'q':
		clear()
		print("Enter 'q' to quit.")
		#looping through the ordered dict.
		for key, value in menu.items():
			print('{}) {}'.format(key, value.__doc__))#__doc__ prints the doc strings(""") in the function
		choice = input('Action: ').lower().strip()
		
		if choice in menu:
			clear()
			menu[choice]()

def add_entry():
	'''Add an entry'''
	print('Enter your entry. Press ctrl+d when finished.')
	data = sys.stdin.read().strip()
	
	if data:
		if input('Save entry? [Yn] ').lower() != 'n':
			Entry.create(content=data)
			print("Saved succesfully!")
		

def view_entry(search_query=None):
	'''View previous entry'''
	entries = Entry.select().order_by(Entry.timestamp.desc())
	if search_query:
		entries = entries.where(Entry.content.contains(search_query))
	
	for entry in entries:
		timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
		clear()
		print(timestamp)
		print('='*len(timestamp))
		print(entry.content)
		print('n) next entry')
		print('d) delete entry')
		print('q) return to main menu')
		
		next_action = input('Action: [Ndq] ').lower().strip()
		if next_action == 'q':
			break
		elif next_action == 'd':
			delete_entry(entry)
			
def search_entry():
	'''search an entry'''
	view_entry(input("Search query: "))

def delete_entry(entry):
	'''Delete an entry'''
	if input("Are you sure? [YN] ").lower() == 'y':
		entry.delete_instance()
		print('Entry deleted...')
	
	
#----------Program_Menu_Keys----------
menu = OrderedDict([
		('a', add_entry),
		('v', view_entry),
		('s', search_entry),
	])


#---------Program_Logic----------
if __name__ == '__main__':
    initialize()
    menu_loop()
	

  