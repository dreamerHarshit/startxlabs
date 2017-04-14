'''3. According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards. ("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file name (pointing to a list of words) from the user an d finds and prints all pairs of words that are semordnilaps to the screen. For example, if "stressed" and "desserts" is part of the word list, the the output should include the pair "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!'''

file_name = 'semordnilap_test.txt'  #test cases are stored in semordnilap_test.txt 
f = open(file_name,"r")
d = {}                              #creating dictionary 
words = []
for line in f:
   words.append(line.rstrip())
   
for word in words:
   d[word] = 1
  
   
for word in words:
   '''checking if word is present in dictionary d and if its reverse is present in dictionary word '''
   if word in d and d[word] == 1 and word[::-1] in d and d[word[::-1]] == 1:  
      d[word] = 2
   
   
for word in d:
   if d[word] == 2:
      print word, word[::-1]
