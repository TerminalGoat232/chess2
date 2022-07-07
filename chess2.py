from pickle import PicklingError
import pygame as pg
from pygame.locals import *
from numpy import *
import Input
import board
import pygame_button as btt
pg.init()
mouse = Input.Mouse()
key = Input.Key()

b = board.Board()

picked ='x10'
placed='x10'
labels=[]
captured = []
lastcap = []
captured_log=['']
moves_log=[]
screen = pg.display.set_mode((1000,800))
clock = pg.time.Clock()
imagesetc={}

def fontsize(sz):
	font = pg.font.Font("8b.ttf",sz)
	return font
defaultfont = fontsize(18)	

class Label:
	def __init__(self, screen, text, x, y, size=20, color="white",command=None):
		if size != 20:
			self.font = fontsize(size)
		else:
			self.font = defaultfont
		self.image = self.font.render(text, 10, color)
		_, _, w, h = self.image.get_rect()
		self.rect = pg.Rect(x, y, w, h)
		self.screen = screen
		self.text = text
		key.check_key()
		left = mouse.is_mouse_pressing(1)
		labels.append(self)
		if left[0]:command()
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
		self.materials = ['i','O','w','n','y','b',"j","J","s","S",'0','x',"E","R","M","F","Q","K","r","m","f","q","k","e"]
		self.images={}
		self.images1={}
	def load_pieces(self):
		for p in self.materials:
			self.images[p]=pg.image.load("sprites/"+p+".png")
	def draw_board(self):
		for x in range(1,9):
			for y in range(1,len(self.board[1])+1):
				if self.r % 2  == 0:
					pg.draw.rect(screen,(116,139,189),[self.tilesize*y,self.tilesize*x, self.tilesize,self.tilesize])
					for cc in range(1,8):
						if cc==1 or cc==6:
							pg.draw.rect(screen,(24,24,25),[self.tilesize,self.tilesize*cc,self.tilesize,self.tilesize*3])
							pg.draw.rect(screen,(24,24,25),[self.tilesize*10,self.tilesize*cc,self.tilesize,self.tilesize*3])
				else: pg.draw.rect(screen,(255,255,255),[self.tilesize*y,self.tilesize*x,self.tilesize,self.tilesize])
				self.r+=1
			self.r-=1
	def draw_pieces(self):
		for xx in range(1,9):
			for yy in range(0,len(self.board[1])):
				self.pces = self.mainboard[f'{xx}'][yy]
				screen.blit(self.images[self.pces],pg.Rect(self.pcsz*yy+90,xx*self.pcsz+20,self.pcsz,self.pcsz))
	def draw_letters_and_num(self):
		for cnt in range(0,len(self.ltts1)):
			Label(screen,self.ltts1[cnt],1.06*self.tilesize*cnt,40,40)
		cnt2=9
		while cnt2>1:
			cnt2-=1
			Label(screen,str(cnt2),30,abs(cnt2-9)*self.tilesize+10,40)
   	#SpEcIl CaSe DoNt AsK mE WhY
	def Rook(self,r:str,c):
		self.res=[]
		for x1 in range(1,9):
			for x2 in range(1,len(self.board[1])-1):
				if self.mainboard[str(x2)][x1]=="0":
					self.res.append(str(x2)+str(x1))
		for abc in captured:
			if abc!= "0" and abc!= "b" and (abc.isupper() == self.mainboard[r][c].isupper() or abc.islower() == self.mainboard[r][c].islower()):
				self.res+=b.hNv_near(r,c,0,False)
		return self.res
if __name__ == "__main__":
	running=True
	
	pgi = pg.image
	
	screen.fill("#181819")
	uib = UIBoard()
	uib.draw_letters_and_num()
	uib.load_pieces()
	ngu = 0
	while running:
		legal = board.LegalMoves(uib.mainboard)
		events = pg.event.get()
		Input.set_events(events)
		for event in events:
			if event.type == pg.QUIT:
				running = False
		mouse.check_mouse()
		key.check_key()
		left = mouse.is_mouse_pressing(1)
		middle = mouse.is_mouse_pressing(2)
		right = mouse.is_mouse_pressing(3)
		key.add_key("s",pg.K_s)
		SUStain=0
		if mouse.get_mouse_pos()[0]>=500:SUStain=-30
		else: SUStain=30
		if left[0]:
			pos=left[1]
			col = str((pos[1])/80).split('.')[0]
			row = str((pos[0]-SUStain)/95).split('.')[0]
			if int(row)>=0 and int(col)>=0 and uib.mainboard[str(int(col))]!='0' and int(row)<=9 and int(col)<=9:
				picked = list(uib.mainboard[col][abs(int(row))]+col+str((int(row))))
				print(picked)
			#print("[Q]>",legal.Queen(picked[1],int(picked[2])))
		if  right[0] and picked[0]!='0':
			pos1=right[1]
			col1 = str((pos1[1])/80).split('.')[0]
			row1= str((pos1[0]-SUStain)/95).split('.')[0]
			if int(row1)>0 and int(col1)>0 and uib.mainboard[str(int(col))]!='0' and int(row1)<9 and int(col1)<9:
				placed = uib.mainboard[col1][abs(int(row1)-9)]+col1+str((int(row1)))
				pp = int(placed[2])
				for o in range(0,len(uib.ltts1[2:len(uib.ltts1)])):
					if pp==o:pp=o
				#placed_log = picked[0]+placed[1:2]+uib.ltts1[1:len(uib.ltts1)][pp]+""+captured_log[ngu]
				print(placed)
				#moves_log.append(placed_log)
				# print(moves_log)
				if placed!=picked and (uib.mainboard[placed[1]][int(placed[2])].isupper()!=uib.mainboard[picked[1]][int(picked[2])].isupper())  or (uib.mainboard[placed[1]][int(placed[2])].islower()!=uib.mainboard[picked[1]][int(picked[2])].islower()) or uib.mainboard[placed[1]][int(placed[2])].lower() == 'b':
					print( uib.mainboard[picked[1]][int(picked[2])])
					#applies legal moves for those fellas
					h = uib.mainboard[picked[1]][int(picked[2])]
					rok,qee1,quee2,keeng2,monke,ber,feesh,eleft,fisk,saved_keeng,keeng1= False,False,False,False,False,False,False,False,False,False,False
					keeng1 = (h=="k") and uib.mainboard["5"][0] != 'k' and placed[1:3] in legal.King(picked[1],int(picked[2]))
					keeng3 = (h=="K") and uib.mainboard["5"][0] != 'K' and placed[1:3] in legal.King(picked[1],int(picked[2]))
					try: 
						feesh = placed[1:3] in legal.Fish(picked[1],int(picked[2]),h)
					except: pass
					ber = (h == 'b') and placed[1:3] in legal.Bear(picked[1],int(picked[2]))
					qee1 = (h =='q') and uib.mainboard["4"][9]!='q' and placed[1:3] in legal.Queen(picked[1],int(picked[2]))
					qee2 =  (h =='Q') and uib.mainboard["4"][0]!='Q' and placed[1:3] in legal.Queen(picked[1],int(picked[2]))
					fisk = (h=='n' or h=='w') and placed[1:3] in legal.Queen(picked[1],int(picked[2]))
					rok = (h.lower()=='r') and placed[1:3] in uib.Rook(picked[1],int(picked[2]))
					eleft = (h.lower()=='e') and placed[1:3] in legal.Elephant(picked[1],int(picked[2])) 
					monke = (h.lower()=='m') and placed[1:3] in legal.Monkey(picked[1],int(picked[2]))
					saved_keeng = (h=="i" or h=="O") and placed[1:3] in legal.King(picked[1],int(picked[2]))
					
					
					if keeng1 or keeng2 or feesh or rok or qee1 or qee2 or monke or ber or eleft or fisk or saved_keeng: # check if it's legal to move or capture
						if placed[1] == "1" and uib.mainboard[picked[1]][int(picked[2])]=='f':
							uib.mainboard[picked[1]][int(picked[2])] = 'w' #no fcking way white fishe evolved!!!!11
						if placed[1] == "8" and uib.mainboard[picked[1]][int(picked[2])]=='F':      
							uib.mainboard[picked[1]][int(picked[2])] = 'n' #no fcking way black fishe evolved!!!!11
						captured =  uib.mainboard[placed[1]][int(placed[2])]
						if captured!='0': 
							lastcap = captured if captured != "b" else ""
							captured_log.append('x'+uib.mainboard[placed[1]][int(placed[2])])
						ngu += 1
						print(uib.mainboard[picked[1]][int(picked[2])-1])
						if  (h=='M') and placed[1:3] == '53' and uib.mainboard["5"][0]=="K" and uib.mainboard["5"][2]!='0':
							uib.mainboard["5"][1]="O"
							uib.mainboard["5"][0]="x"
						if  (h=='m') and placed[1:3] == "56" and uib.mainboard["5"][9]=="k" and uib.mainboard["5"][7]!='0' :
							uib.mainboard["5"][8]="i"
							uib.mainboard["5"][9]="x"
						
						print("x"+uib.mainboard[placed[1]][int(placed[2])][0])
						for mm in captured[0]:
							if mm == 'K':
								uib.mainboard["5"][0] = 'K'
								
							if mm == 'O':uib.mainboard["5"][0] = 'O'
							if mm == 'i':uib.mainboard["5"][9] = 'i'
							if mm == "Q": uib.mainboard["4"][0]='Q'
							if mm == 'k':uib.mainboard['5'][9] = 'k'
							if mm =="q": uib.mainboard["4"][9]='q'
						uib.mainboard[placed[1]][int(placed[2])] = uib.mainboard[picked[1]][int(picked[2])]
						uib.mainboard[picked[1]][int(picked[2])] = '0'
						if uib.mainboard["5"][0]=="O" and uib.mainboard["4"][0]=="Q":
							print('black lose')
							Label(screen,text="BLACK LOSE",x=300,y=300,color="black",size=65)
						if uib.mainboard["5"][9]=="i" and uib.mainboard["4"][9]=="q":
							print('white lose')
							Label(screen,text="WHITE LOSE",x=300,y=300,color="black",size=65)
						picked='0'
						
		uib.draw_board()
		uib.draw_pieces()
		b.printboard()
		showlbls()
		clock.tick(60)
		pg.display.flip()
	pg.quit()
	quit()
