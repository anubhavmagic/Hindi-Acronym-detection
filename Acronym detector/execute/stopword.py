import re
test1= "बहुजन समाज एक्स पार्टी . आईआईटी मा.या.व.ती. ने मंगलवार को भारतीय जनता"
test2 = "hello my name is A.N.U.B.H.A.V. ok? so you must find M.E. as an acronym."
test3 = "मंगलवार"
#letter10 = r'(\S)*(\.)(\S)*'
#searchObj = re.search( letter10, test1,re.UNICODE)
stopword = r'(\.)*(\.)'
stopword2 = r'(\.)*(\.)'
def test(test2):
	searchObj = re.search(stopword2,test2, flags = re.UNICODE)
	if searchObj:
		return(searchObj.group())
	else:
		return 0

							
def main():	
	g = open('input.txt', 'r')
	i= open('res.txt', 'w')
	i.write("")
	i.close()
	k = open('res.txt', 'a')
	#print "file created \n"
	with g as f:
		for line in f:
			kanishk = line
			words = kanishk.split()
			#print "line detected \n"
			for word in words:
				res = test(word)
				#print res
				if res:
					k.write(word)
					k.write("\n")
           
	
	g.close()
	k.close()

if __name__ == '__main__':
   main()


