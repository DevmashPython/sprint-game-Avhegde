import msvcrt
import time

first=5 
count=0 
fin=0
y=0  
print "PRESS ENTER"
raw_input()
s_time=time.time()

def down():
	flag=1
	count2=0
	fin=1
	while(flag==1):
		key=msvcrt.getch()
		if key=='s':
			print 18*' ',
			print"|"
			count2=count2+1
		else:
			print "YOU LOST,TRY AGAIN"
			break	
		if count2==first:
			flag=2
			print 10*" "+"TURN RIGHT",
			right(1)

def right(fin):
	count=0
	finish=5
	while(1):
		key=msvcrt.getch()
		if key=='d':
			count=count+1
			print "-->",
			if count==finish:
				print "MOVE DOWN"
				if(fin==0):
					down()
				else:
					time_elap=time.time()-s_time
					print "YOU WON"
					print "TIME TAKEN IS: " +str(round(time_elap))
					x=raw_input("PRESS ENTER TO QUIT")
					quit()
		else:
			print "GAME OVER"
			break

while(1):
	right(0)




'''
1. Mention controls for the game.
2. The program should end after game is lost.	
'''

					
					
		


