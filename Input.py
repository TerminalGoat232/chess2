import pygame

global_events = []
def set_events(events):
	global global_events
	global_events = events

class Key:
	def __init__(self):
		self.key = {}
		self.bind = {}
	def add_key(self,name,sig):
		self.key[str(name)] = {"pressing": False}
		self.bind[str(sig)] = name
	def check_key(self):
		for event in global_events:
			if event.type == pygame.KEYDOWN:
				if str(event.key) in self.bind:
					name = self.bind[str(event.key)]
					if name in self.key:
						self.key[name]["pressing"] = True
			if event.type == pygame.KEYUP:
				if str(event.key) in self.bind:
					name = self.bind[str(event.key)]
					if name in self.key:
						self.key[name]["pressing"] = False
	def is_key_pressing(self, key):
		if key in self.key:
			return self.key[key]['pressing']
class Mouse:
	def __init__(self):
		self.last_post = (0,0)
		self.button = {"1":{"pressing":False,"last_click_pos":(0,0)},
		               "2":{"pressing":False,"last_click_pos":(0,0)},
		               "3":{"pressing":False,"last_click_pos":(0,0)},
		               "4":{"pressing":False,"last_click_pos":(0,0)},
		               "5":{"pressing":False,"last_click_pos":(0,0)},
		               "6":{"pressing":False,"last_click_pos":(0,0)},
		               "7":{"pressing":False,"last_click_pos":(0,0)}}
	def check_mouse(self):
		for event in global_events:
			if event.type == pygame.MOUSEMOTION:
				if event.pos != None:
					self.last_post = event.pos
			if event.type == pygame.MOUSEBUTTONDOWN:
				if str(event.button) not in self.button:
					self.button[str(event.button)] = {"pressing":False,"last_click_pos":(0,0)}
				self.button[str(event.button)]["pressing"] = True
				self.button[str(event.button)]["last_click_pos"] = event.pos
			if event.type == pygame.MOUSEBUTTONUP:
				if str(event.button) not in self.button:
					self.button[str(event.button)] = {"pressing":False,"last_click_pos":(0,0)}
				self.button[str(event.button)]["pressing"] = False
				self.button[str(event.button)]["last_click_pos"] = event.pos
	def get_mouse_pos(self):
		return self.last_post
	def is_mouse_pressing(self,button):
		return self.button[str(button)]['pressing'],self.button[str(button)]['last_click_pos']

