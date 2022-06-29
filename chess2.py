import pygame as pg
from pygame.locals import *
from numpy import *
import Input
import board
pg.init()
mouse = Input.Mouse()
b = board.Board()
picked ='x10'
placed='x10'
labels=[]
screen = pg.display.set_mode((1000,800))
clock = pg.time.Clock()
def fontsize(sz):
	font = pg.font.Font("8b.ttf",sz)
	return font
defaultfont = fontsize(18)	
class Label:
	def __init__(self, screen, text, x, y, size=20, color="white"):
		if size != 20:
			self.font = fontsize(size)
		else:
			self.font = defaultfont
		self.image = self.font.render(text, 10, color)
		_, _, w, h = self.image.get_rect()
		self.rect = pg.Rect(x, y, w, h)
		self.screen = screen
		self.text = text
		labels.append(self)
	def draw(self):
		self.screen.blit(self.image, (self.rect))
def showlbls():
	for l in labels:
		l.draw()

class UIBoard:
	def __init__(self,width=9,height=8):
		self.w = width
		self.h = height
		self.pcsz = 80
		self.tilesize = 80
		self.r = 0
		self.mainboard = b.mainboard()
		self.constboard = b.constboard()
		self.board = b.setup('xRMFQKFMRx','xRMFQKFMRx'.lower(),'xFFEFFEFFx','xFFEFFEFFx'.lower())
		self.ltts1 = ['','','A','B','C','D','E','F','G','H']
		#self.materials = ["R","M","F","Q"]
		self.etcandhornyjails = ["Jb1","Jb2","Jw1","Jw2"]
		self.materials = ['b',"Jb1","Jb2","Jw1","Jw2",'0','x',"E","R","M","F","Q","K","r","m","f","q","k","e"]
		self.images={}
	def load_pieces(self):
		for p in self.materials:
			self.images[p]=pg.image.load("sprites/"+p+".png")
			#self.images[p] = pg.transform.scale(self.images[p],(50,55))
	def draw_board(self):
		for x in range(1,9):
			for y in range(1,len(self.board[1])+1):
				if self.r % 2  == 0:
					pg.draw.rect(screen,(116,139,189),[self.tilesize*y,self.tilesize*x,
													self.tilesize,self.tilesize])
					for cc in range(1,8):
						if cc==1 or cc==6:
							pg.draw.rect(screen,(24,24,25),[self.tilesize,self.tilesize*cc,
																self.tilesize,self.tilesize*3])
							pg.draw.rect(screen,(24,24,25),[self.tilesize*10,self.tilesize*cc,
																self.tilesize,self.tilesize*3])
						
				else: pg.draw.rect(screen,(255,255,255),[self.tilesize*y,self.tilesize*x,
													self.tilesize,self.tilesize])
				self.r+=1
			self.r-=1
	def draw_pieces(self):
		for xx in range(1,9):
			for yy in range(-1,len(self.board[1])):
				self.pces = self.mainboard[f'{xx}'][yy]
				if self.pces != '-':
					screen.blit(self.images[self.pces],pg.Rect(self.pcsz*yy+90,xx*self.pcsz+20,self.pcsz,self.pcsz))
	def draw_letters_and_num(self):
		for cnt in range(0,len(self.ltts1)):
			Label(screen,self.ltts1[cnt],1.06*self.tilesize*cnt,40,40)
		for cnt2 in range(1,9):
			Label(screen,str(cnt2),30,cnt2*self.tilesize+10,40)
if __name__ == "__main__":
	running=True
	
	pgi = pg.image
	
	screen.fill("#181819")
	uib = UIBoard()
	uib.draw_letters_and_num()
	uib.load_pieces()
	while running:
		events = pg.event.get()
		Input.set_events(events)
		for event in events:
			if event.type == pg.QUIT:
				running = False
		mouse.check_mouse()
		left = mouse.is_mouse_pressing(1)
		right = mouse.is_mouse_pressing(3)
		SUS=0
		if mouse.get_mouse_pos()[0]>=500:SUS=-45
		else: SUS=45
		if left[0]:
			pos=left[1]
			col = str((pos[1])/80).split('.')[0]
			row = str((pos[0]-SUS)/95).split('.')[0]
			print(pos[0])
			if int(row)>0 and int(col)>0 and uib.mainboard[str(int(col))]!='0' and int(row)<9 and int(col)<9:
				picked = list(uib.mainboard[col][abs(int(row)-9)]+col+str((int(row))))
				print(picked)
		if  right[0] and picked!='0':
			pos1=right[1]
			col1 = str((pos1[1])/80).split('.')[0]
			row1= str((pos1[0]-SUS)/95).split('.')[0]
			print(pos1[0])
			if int(row1)>0 and int(col1)>0 and uib.mainboard[str(int(col))]!='0' and int(row1)<9 and int(col1)<9:
				placed = uib.mainboard[col1][abs(int(row1)-9)]+col1+str((int(row1)))
				print(placed)
				if placed!=picked:
					uib.mainboard[placed[1]][int(placed[2])] = uib.mainboard[picked[1]][int(picked[2])]
					uib.mainboard[picked[1]][int(picked[2])] = '0'
					picked='0'
		uib.draw_board()
		uib.draw_pieces()
		#b.printboard()
		showlbls()
		clock.tick(60)
		pg.display.flip()
	pg.quit()
	quit()
