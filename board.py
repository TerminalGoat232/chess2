#! /usr/bin/env python
import random
class Board:
	def __init__(self,tp=0):

		self.consttiles={
				
      				'1':['x','0','0','0','0','0','0','0','0','x'],\
					'2':['x','0','0','0','0','0','0','0','0','x'],\
					'3':['x','0','0','0','0','0','0','0','0','x'],\
				'4':['Jb1','0','0','0','0','0','0','0','0','Jw1'],\
				'5':['Jb2','0','0','0','0','0','0','0','0','Jw2'],\
					'6':['x','0','0','0','0','0','0','0','0','x'],\
					'7':['x','0','0','0','0','0','0','0','0','x'],\
					'8':['x','0','0','0','0','0','0','0','0','x']}

		self.tiles={
      				'1':['x','0','0','0','0','0','0','0','0','x'],\
					'2':['x','0','0','0','0','0','0','0','0','x'],\
					'3':['x','0','0','0','0','0','0','0','0','x'],\
				'4':['Jb1','0','0','0','0','0','0','0','0','Jw1'],\
				'5':['Jb2','0','0','0','0','0','0','0','0','Jw2'],\
					'6':['x','0','0','0','0','0','0','0','0','x'],\
					'7':['x','0','0','0','0','0','0','0','0','x'],\
					'8':['x','0','0','0','0','0','0','0','0','x']}
		self.l1=[]
		self.wmove = True
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
	def hNv_near(self,r:str,c,bw=False):
		self.up = str(int(r)+1)+str(c);self.down=str(int(r)-1)+str(c)
		self.left=r+str(c-1);self.right=r+str(c+1)
		self.res = [self.up,self.down,self.left,self.right]
		if r == 8: self.res.remove(self.up)
		if r == 1: self.res.remove(self.down)
		if self.tiles[r][c]=='8':self.res.remove(self.right)
		if self.tiles[r][c]=='1':self.res.remove(self.left)
		return self.res
	def corners_near(self,r:str,c,bw=False):
		self.tleft = str(int(r)+1)+str(c-1)
		self.tright =str(int(r)+1)+str(c+1)
		self.bleft = str(int(r)-1)+str(c-1)
		self.bright = str(int(r)-1)+str(c+1)
		self.res = [self.tleft,self.tright,self.bleft,self.bright]
		if c == 1:self.res.remove(self.tleft);self.res.remove(self.bleft)
		if c == 8:self.res.remove(self.tright);self.res.remove(self.bright)
		# if r == "1":self.res.remove(self.bleft);self.res.remove(self.bright)
		# if r == "8":self.res.remove(self.tright);self.res.remove(self.tleft)
		return self.res       
class LegalMoves(Board):
	def __init__(self,board):
		super().__init__()
		self.board = board
	def King(self,r:str,c):
		return self.hNv_near(r,c)+self.corners_near(r,c)
	def Feesh(self,r:str,c,h):
		if h == "f":
			res1 = []
			
			self.forward = str(int(r)-1)+str(c)
			self.left1=r+str(c-1);self.right1=r+str(c+1)
			self.tleft1 = str(int(r)-1)+str(c+1);self.tright1 =str(int(r)-1)+str(c-1)
			res1 = [self.forward,self.left1,self.right1,self.tleft1,self.tright1]
			
			if self.board[self.forward[0]][int(self.forward[1])] != '0' : res1.remove(self.forward) 
			if self.board[self.left1[0]][int(self.left1[1])] !='0' and self.board[self.forward[0]]!="1":res1.remove(self.left1)
			if self.board[self.right1[0]][int(self.right1[1])] != '0' and self.board[self.forward[0]]!="1":res1.remove(self.right1)
			print(self.forward[0])
			if self.forward[0] == "1":print('cuwts')
			return res1
			
		if h == "F":
			res2 = []
			self.forward1 = str(int(r)+1)+str(c)
			self.left2=r+str(c-1);self.right2=r+str(c+1)
			self.tleft2 = str(int(r)+1)+str(c-1);self.tright2 =str(int(r)+1)+str(c+1)
			res2 = [self.forward1,self.left2,self.right2,self.tleft2,self.tright2]
			if self.board[self.forward1[0]][int(self.forward1[1])]!= '0' or self.board[self.forward1[0]] == "8" : res2.remove(self.forward1)
			if self.board[self.left2[0]][int(self.left2[1])] !='0' and self.board[self.forward1[0]]!="8":res2.remove(self.left2)
			if self.board[self.right2[0]][int(self.right2[1])] != '0' and self.board[self.forward1[0]]!="8":res2.remove(self.right2)
			# else: 
			# 	try: res2.remove(self.tleft2);res2.remove(self.tright2)
			# 	except:pass
			if self.board[self.forward1[0]] == "8": res2.remove(self.forward1);res2.remove(self.tleft2);res2.remove(self.tright2)
			return res2
#test
cc = Board()
cc.setup('xRMFQKFMRx','xRMFQKFMRx'.lower(),'xFFEFFEFFx','xFFEFFEFFx'.lower())
cc.printboard()
a = cc.mainboard()


