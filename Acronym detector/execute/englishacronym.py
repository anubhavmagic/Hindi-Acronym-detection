﻿import re
#test= "check if match dove or not veer"
#test1= "बहुजन समाज एक्स पार्टी आईआईटी आईआईटीके  सपा एक्स बसपा सुप्रीमो मायावती ने मंगलवार को भारतीय जनता पार्टी (भाजपा) पर निशाना साधते हुए कहा कि गोधरा कांड करवाने वाले नरेंद्र मोदी अगर गलती से प्रधानमंत्री बन गए तो देश में सांप्रदायिक दंगे आम बात हो जाएंगे। मंगलवार को यहां मिनी स्टेडियम परेड में चुनावी रैली मायावती ने कांग्रेस को भी जमकर कोसा"
#result = re.match(r'(f|o|x){3}',test,re.M|re.I)

#check= r'(स|ब|पा)'
letter10 = r'(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)'
letter9 =  r'(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)'
letter8 = r'(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)'
letter7 = r'(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)'
letter6 = r'(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)'
letter5 = r'(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)'
letter4 = r'(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)'
letter3 = r'(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)'
letter2 = r'(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)'
letter1 = r'(एक्स|बी|सी|डी|ई|एफ|जी|एच|आई|आइ|जेड|के|एल|एम|एन|ओ|पी|क्यू|आर|एस|टी|यू|वी|डब्ल्यू|डब्लू|ए|वाई|जे)'

#f= open('out.txt', 'w')

def test(test2):
	searchObj = re.search( letter10, test2, flags = re.UNICODE)
	if searchObj:
		return(searchObj.group())
	else:
		searchObj = re.search( letter9, test2, flags = re.UNICODE)
		if searchObj:
			return(searchObj.group())
		else:
			searchObj = re.search( letter8, test2, flags = re.UNICODE)
			if searchObj:
				return(searchObj.group())
			else:
				searchObj = re.search( letter7, test2, flags = re.UNICODE)
				if searchObj:
					return(searchObj.group())
				else:
					searchObj = re.search( letter6, test2, flags = re.UNICODE)
					if searchObj:
						return(searchObj.group())
					else:
						searchObj = re.search( letter5, test2, flags = re.UNICODE)
						if searchObj:
							return(searchObj.group())
						else:
							searchObj = re.search( letter4, test2, flags = re.UNICODE)
							if searchObj:
								return(searchObj.group())
							else:
								searchObj = re.search( letter3, test2, flags = re.UNICODE)
								if searchObj:
									return(searchObj.group())
								else:
									searchObj = re.search( letter2, test2, flags = re.UNICODE)
									if searchObj:
										return(searchObj.group())
									else:
										return 0

										
def main():	
	g = open('input.txt', 'r')
	i= open('outpu.txt', 'w')
	i.write("")
	i.close()	
	k = open('outpu.txt', 'a')
	#print "file created \n"
	print "Please wait: detecting english word acronyms."
	with g as f:
		for line in f:
			kanishk = line
			words = kanishk.split()
			#print "line detected \n"
			for word in words:
				res = test(word)
				#print res
				if res:
					k.write(res+'\n')
           
	
	g.close()
	k.close()
	print "English acronyms detected."

if __name__ == '__main__':
   main()
#f.close()