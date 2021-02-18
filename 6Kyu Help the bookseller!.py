import re
def stock_list(listOfArt,listOfCat):
	print(listOfArt,listOfCat)
	daf = {}
	for i in listOfArt:
		# print(listOfArt[0])
		if i[0] in daf.keys():
			# print(i[0])
			# print(daf[i[0][0]])
			daf[i[0][0]] = int(daf[i[0][0]]) + int(re.search(r'\d+', i).group())
			continue
		daf[i[0][0]] = int(re.search(r'\d+', i).group())
	# print(i)
	print(daf)
	returned = []
	for i in listOfCat:
		# print(i)
		if daf.get(i) == None:
			print(i)
		returned.append("({} : {})".format(i,daf[i] if daf.get(i) != None else 0))
	print(' - '.join(returned) if bool(listOfArt) else '')
print(stock_list(["ABAR 200", "CDXE 500", "BKWR 0250", "DRTY 600"],["A", "B","w"]))

import re
def stock_list(listOfArt,listOfCat):
	daf = {}
	for i in listOfArt:
		if i[0] in daf.keys():
			daf[i[0][0]] = int(daf[i[0][0]]) + int(re.search(r'\d+', i).group())
		else:
			daf[i[0][0]] = int(re.search(r'\d+', i).group())
	returned = []
	for i in listOfCat:
		print(i)
		returned.append("({} : {})".format(i,daf[i] if daf.get(i) != None else 0))
	return(' - '.join(returned) if bool(listOfArt) and bool(listOfCat) else '')
