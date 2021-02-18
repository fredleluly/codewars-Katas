import re
def stock_list(listOfArt,listOfCat):
    daf = {}
    for i in listOfArt:
        if i[0] in daf.keys():
            daf[i[0][0]] = int(daf[i[0][0]]) + int(re.search(r'\d+', i).group())
        else:
            daf[i[0][0]] = int(re.search(r'\d+', i).group())
    return ' - '.join(["({} : {})".format(i,daf[i] if daf.get(i)!= None else 0) for i in listOfCat])  if bool(listOfArt) and bool(listOfCat) else ''
    
