#World to map 
world = [[1,1,1,0,1,1,1,1,1],
		 [1,0,0,0,1,0,0,1,0],
		 [1,0,1,0,1,0,1,1,1],
		 [1,0,1,0,0,0,0,0,1],
		 [1,0,1,1,1,1,0,1,1],
		 [1,0,1,0,0,0,0,0,1],
		 [1,1,1,1,0,1,1,0,1],
		 [1,0,0,0,0,1,0,0,1],
		 [1,1,1,1,0,1,1,1,1]]

class dynamics(object):
	def __init__(self,pos,heading):
		self.pos = pos
		self.heading = heading
	def moveForward(self,steps):
		for i in range(steps):
			self.pos = [self.pos[0] + self.heading[0], self.pos[1] + self.heading[1]]
	def print_parameters(self):
		print self.pos, self.heading
init = [8, 4]
goal = [0, 3] 
delta = [[-1, 0,'^'], # go up
         [ 0,-1,'<'], # go left
         [ 1, 0,'v'], # go down
         [ 0, 1,'>']] # go right
grid = [[-1 for row in range(len(world[0]))] for col in range(len(world))]
def Mapping(delta):
	heading = delta[0]
	flag = True
	me = dynamics(init,heading)
	while flag:
		for j in delta:
			new = [me.pos[0] + j[0], me.pos[1] + j[1]]
			if new[0] >= 0 and new[1] >= 0 and new[0] < len(world) and new[1] < len(world[0]):
				if world[new[0], new[1]] is 0 and grid[new[0], new[1]] is -1:
					


