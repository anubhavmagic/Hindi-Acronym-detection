import re

acro = r'(\^)'
def test(test2):
	searchObj = re.search(acro,test2, flags = re.UNICODE)
	if searchObj:
		return(searchObj.group())
	else:
		return 0

							
def main():	
	g = open('htinput.txt', 'r')
	i= open('htres.txt', 'w')
	i.write("")
	i.close()
	k = open('htres.txt', 'a')
	#print "file created \n"
	number = 0
	with g as f:
		for line in f:
			kanishk = line
			words = kanishk.split()
			#print "line detected \n"
			for word in words:
				res = test(word)
				#print res
				if res:
					k.write((word.strip('^,(,\',),[,],-,/')).rstrip('।'))
					k.write("\n")
					number = number + 1
           
	
	k.write("number of acronyms:"+str(number))
	g.close()
	k.close()
	print "Done"

if __name__ == '__main__':
   main()


