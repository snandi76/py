def CoinChange(input1,input2):
	ListAmount = []
	#print(range(0,input1))
	ArraySize = int(input1) + 1
	for i in range(0,ArraySize):
		#print(i)
		if i == 0:
			ListAmount.append(1)
		else:
			ListAmount.append(0)
	
	for nCoin in input2:
		print(ListAmount)
		for iAmount in range(0,ArraySize):
			if iAmount >= nCoin:
				ListAmount[iAmount] += ListAmount[iAmount - nCoin]
	
	print(ListAmount)
	#return str(ListAmount[input1])	

list = [1,2,3]	
CoinChange(12,list)