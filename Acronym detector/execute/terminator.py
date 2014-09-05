import re

regex= r'(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|y|Z|हैं|\.\.)'
regex2= r'(a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|y|Z|हैं|\.\.)'
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_eng(s):
	searchObj = re.search(regex, s, flags = re.UNICODE)
	if searchObj:
		return True
	else:
		return False
def main():	
	g = open('out.txt', 'r')
	i= open('out2.txt', 'w')
	i.write("")
	i.close()
	k = open('out2.txt', 'a')
	#print "file created \n"
	with g as f:
		for line in f:
			kanishk = line
			words = kanishk.split()
			#print "line detected \n"
			for word in words:
				res = is_number(word)
				if not res:
					res2 = is_eng(word)
					if not res2:
						k.write(word)
						k.write("\n")
           
	
	g.close()
	k.close()
	print "Processing complete :)"

if __name__ == '__main__':
   main()

