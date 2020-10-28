import sys
readline = sys.stdin.readline
flush = sys.stdout.flush

T = int(readline())

for t in range(1, T+1):
	N, D = [int(_) for _ in readline().split()]
	X = [int(_) for _ in readline().split()]
	
	latest = D
	for i in range(N-1, -1, -1):
		latest = X[i] * (latest//X[i])
	
	print("Case #%d: %d" % (t, latest))
