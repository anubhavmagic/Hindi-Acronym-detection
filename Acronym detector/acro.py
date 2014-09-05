
import os
os.chdir("execute")
os.system("englishacronym.py")
os.system("stopword.py")
os.system("eliminator.py")
os.system("terminator.py")
os.system("combine.py")
os.remove("outpu.txt")
os.remove("out.txt")
os.remove("res.txt")
os.remove("out2.txt")
os.chdir("./..")
print os.getcwd()



print "Acronym detection done \n"
