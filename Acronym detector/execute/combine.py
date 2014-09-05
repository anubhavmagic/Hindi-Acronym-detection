import re

										
def main():	
	g = open('outpu.txt', 'r')
	h= open('out2.txt','r')
	i= open('acronyms.txt', 'w')
	i.write("")
	i.close()
	k = open('acronyms.txt', 'a')
	#print "file created \n"
	number = 0
	with g as f:
		for line in f:
			kanishk = line
			words = kanishk.split()
			#print "line detected \n"
			for word in words:
				k.write(word+'\n')
				number = number +1
	with h as f:
		for line in f:
			kanishk = line
			words = kanishk.split()
			#print "line detected \n"
			for word in words:
				k.write(word+'\n')
				number = number +1
	
	g.close()
	k.close()
	h.close()
	i = open('result.txt', 'w')
	i.write("Total number of acronyms detected are:" + str(number))
	#print "Total number of acronyms detected are:",number
	i.close()
	
	
if __name__ == '__main__':
   main()
#f.close()
