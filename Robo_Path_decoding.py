import sys
readline = sys.stdin.readline
flush = sys.stdout.flush

T = int(readline().strip())
nums = set([str(_) for _ in range(10)])
N = 10**9

for t in range(1, T+1):
	program = readline().strip()
	
	cur = [0, 0]
	
	stack = []
	
	for char in program:
		if char == 'N':
			cur[0] -= 1
		elif char == 'S':
			cur[0] += 1
		elif char == 'W':
			cur[1] -= 1
		elif char == 'E':
			cur[1] += 1
		
		elif char in nums:
			stack.append((cur[0], cur[1], int(char)))
		
		elif char == '(':
			cur = [0, 0]
		
		elif char == ')':
			pop = stack.pop()
			cur = [pop[i] + pop[2]*cur[i] for i in [0, 1]]
	
	final_row = (1+cur[0])%N
	if final_row == 0:
		final_row = N
	
	final_column = (1+cur[1])%N
	if final_column == 0:
		final_column = N
	
	print("Case #%d: %d %d" % (t, final_column, final_row))
