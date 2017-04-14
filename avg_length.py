'''4. Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens).'''

file_name = 'avg_length_test.txt'   #test cases are stored in avg_length_test.txt file
f = open(file_name,"r")		
add=0.0		
words = []
length_words = 0	
for line in f:			
   words = line.split()
   length_words += len(words) 
   for w in words:	
      add = add + len(w)

avg = add / length_words
print (avg)


