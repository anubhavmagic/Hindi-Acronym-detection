import re

poorna = r'(।)'
brac = r'(\()'
def test(test2):
	searchObj = re.search(poorna, test2, flags = re.UNICODE)
	if searchObj:
		return(searchObj.group())
	else:
		return 0;

def test2(test):
	searchObj = re.search(brac, test, flags = re.UNICODE)
	if searchObj:
		return(searchObj.group())
	else:
		return 0;
		
def main():	
	g = open('raw.txt', 'r')
	i= open('input.txt', 'w')
	i.write("")
	i.close()
	k = open('input.txt', 'w')
	with g as f:
		for line in f:
			kanishk = line
			words = kanishk.split()
			for word in words:
				res = test(word)
				if res:
					k.write((word.strip('-,\\,/,(,),[,],^')).strip('-,\\,/,(,),[,],^'))
					k.write("\n")
				else:
					k.write((word.strip('-,\\,/,(,),[,],^')).strip('-,\\,/,(,),[,],^') + " ")
	
	g.close()
	k.close()
	print "Corpus fixed ! :)"
	

if __name__ == '__main__':
   main()
#f.close()
