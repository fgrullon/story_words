 #We import the urlopen from the library urllib
 from urllib.request import urlopen
 
 #usin with we retract the data from the url using urlopen and store it on story
 
 with urlopen('http://sixty-north.com/c/t.txt') as story:
 
 #Now we create a list
	story_words = []
  
 #Using a for loop we retract every line and decode it from bytes to str and store it in the list line_words
	for line in story:
		line_words = line.decode('utf-8').split()
#Then using a for loop we select every element 'word' of the list in line_words and insert it at the end of the story words list    
		for word in line_words:
			story_words.append(word)

