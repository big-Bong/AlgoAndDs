def isRobotBounded(instructions):
	directions = {(0,'L'):(-1,0,3),
				(0,'R'):(1,0,2),
				(1,'L'):(1,0,2),
				(1,'R'):(-1,0,3),
				(2,'L'):(0,1,0),
				(2,'R'):(0,-1,1),
				(3,'L'):(0,-1,1),
				(3,'R'):(0,1,0)}
	x = y = 0
	x_adder = 0
	y_adder = 1
	pointer = 0

	for elem in instructions:
		if(elem == 'G'):
			x += x_adder
			y += y_adder
		else:
			x_adder, y_adder, pointer = directions[(pointer,elem)]

	return (((x==0 and y==0) or pointer!=0))

instructions = "L"
print(isRobotBounded(instructions))

