#! /usr/bin/env python
import random
class Board:
	def __init__(self,tp=0):

		self.consttiles={'1':['x','0','0','0','0','0','0','0','0','x'],\
					'2':['x','0','0','0','0','0','0','0','0','x'],\
					'3':['x','0','0','0','0','0','0','0','0','x'],\
				'4':['Jb1','0','0','0','0','0','0','0','0','Jw1'],\
				'5':['Jb2','0','0','0','0','0','0','0','0','Jw2'],\
					'6':['x','0','0','0','0','0','0','0','0','x'],\
					'7':['x','0','0','0','0','0','0','0','0','x'],\
					'8':['x','0','0','0','0','0','0','0','0','x']}

		self.tiles={'1':['x','0','0','0','0','0','0','0','0','x'],\
					'2':['x','0','0','0','0','0','0','0','0','x'],\
					'3':['x','0','0','0','0','0','0','0','0','x'],\
				'4':['Jb1','0','0','0','0','0','0','0','0','Jw1'],\
				'5':['Jb2','0','0','0','0','0','0','0','0','Jw2'],\
					'6':['x','0','0','0','0','0','0','0','0','x'],\
					'7':['x','0','0','0','0','0','0','0','0','x'],\
					'8':['x','0','0','0','0','0','0','0','0','x']}
					
		self.l1=[]
		self.tiles[f'{random.randint(4,5)}'][random.randint(4,5)]='b'
	def setup(self,s1:str,s2:str,s3:str,s4:str):
		for x in s1:self.l1+=x
		self.tiles['1'] = self.l1
		self.l1=[] 
		for y in s2:self.l1+=y
		self.tiles['8'] = self.l1 
		self.l1=[]
		for z in s3:self.l1+=z
		self.tiles['2'] = self.l1
		self.l1 = []
		for a in s4:self.l1+=a
		self.tiles['7']=self.l1
		
		l1 = self.tiles['1'];l8=self.tiles['8']
		l2= self.tiles['2'];l7=self.tiles['7']
		self.rook = self.tiles['1'][1]
		return [l1,l8,l2,l7]
	def printboard(self):
		for x in range(1,len(self.tiles)+1):
			print(self.tiles[f'{x}'])
	def mainboard(self):return self.tiles
	def constboard(self):return self.consttiles
	#trash {
	def move(self,posx:str,posy:str):
		self.c1 = posx[0];self.r1=posx[1]
		self.c2 = posy[0];self.r2=posy[1]
		self.tiles[self.c2][int(self.r2)] = self.tiles[self.c1][int(self.r1)]
		self.tiles[self.c1][int(self.r1)]= self.consttiles[self.c1][int(self.r1)]
		#self.tiles[posx][posy] = self.consttiles[posx][posy]
		#self.rook = self.tiles[posx][posy]
		#if posy == 1 and posx == '1':self.tiles['1'][1]=self.rook
	#}
class LegalMoves(Board):
	def __init__(self):
		pass
cc = Board()
cc.setup('xRMFQKFMRx','xRMFQKFMRx'.lower(),'xFFEFFEFFx','xFFEFFEFFx'.lower())
cc.printboard()
a = cc.mainboard()

