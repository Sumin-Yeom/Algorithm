N = int(input())
xCoordinate = list(map(int, input().split()))
countSmall = [0*i for i in range(N)]
overlapCheckDic = {}

indexCount = 0
for x in range(N):
	for i in range(N):
		if xCoordinate[x] > xCoordinate[i]:
			if xCoordinate[i] in overlapCheckDic:
				continue
			
			overlapCheckDic[xCoordinate[i]] = True
			countSmall[indexCount] += 1
			
	overlapCheckDic = {}
	indexCount += 1

print(*countSmall)
			
