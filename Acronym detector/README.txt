This Folder contains the following files:
1. Acro.py  			-main script.
2. Corpus align.py 		-To prepare corpus, it removes hand tags as well if you want to use the same corpus.
3. raw.txt				-Raw corpus.
4. README.txt			-instructions.
5. htinput.txt			-Contains handtagged corpus.
6. handtaganalysis.py 	-Performs analysis on hand tagged corpus.
Folder execute/
contains:
englishacronym.py		-Finds out english based acronyms.
stopword.py				-Finds out stopword acronyms.
eliminator.py			-Eliminates Garbage.
terminator.py			-Eliminates Garbage.
combine.py				-Combines final results, outputs 2 files, result.txt and acronyms.txt.
Acronyms.txt will contain all the detected acronyms, and result.txt will contain the count.

Done on python 2.7, used module re.
To use the code, First, put any Hindi text in the raw.txt, don't forget to create a copy first, if modifying.
We use the htinput.txt file, as it is our hand-tagged file.
RUN 'corpus.py'. It will generate 'input.txt' from 'raw.txt', which will have corpus properly fixed.
Put this 'input.txt' in the execute folder, and run the 'acro.py' file. It will generate the final output. It deletes all the intermediate files,if you need them too, comment the deletion lines os.remove, from acro.py
Hope you find a lot of acronyms ;) 


You can use 'handtaganalysis.py' to generate info regarding 'htinput.txt'. It will list the acronyms present in the hand tagged corpus.
It will also give a count of these acronyms.

method of tagging- '^' before any acronym. eg- ^IIT.
Another code for dictionary word elimination has been put, but it is not used. to run it, go to dict folder, and run candidate_seperate.py, then final_seperation.py.
The corpus in this directory should be named india.txt. The seperated wordlist which are candidate acronyms will go to finallyseperated.txt
