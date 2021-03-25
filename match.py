def match(template, candidate):
	i =0
	if len(template)==0 or template == candidate and ('?') not in candidate:
		return True
	if len(template) != len(candidate) or not(candidate.isdigit()):
		return False
	while(i < len(template)):
		if template[i] != candidate[i] and (template[i] != '?' or ( template[i] == '?' and int(candidate[i])>1)):
			return False
		if candidate[i] in('0','1'):
			i+=1
	return True

print('match("","")', match("",""))
print('match("01","01")',match("01","01"))
print('match("0?1","011")',match("0?1","011"))
print('match("0?1","001")',match("0?1","001"))
print('match("0??1","0011")',match("0??1","0011"))
print('match("000?","111?")',match("000?","111?"))
print('match("1", "")',match("1", ""))
print('match("1", "101")',match("1", "101"))
print('match("?", "2")',match("?", "2"))
print('match("?", "?")',match("?", "?"))