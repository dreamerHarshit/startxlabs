'''2. A sentence splitter is a program capable of splitting a text into sentence s. The standard set of heuristics for sentence splitting includes (but isn't limited to) the following rules:

Sentence boundaries occur at one of "." (periods), "?" or "!", except that

- Periods followed by whitespace followed by a lower case letter are not sentence boundaries.

- Periods followed by a digit with no intervening whitespace are not sentence boundaries.

- Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles are not sentence boundaries. Sample titles include Mr., Mrs., Dr., and so on.

- Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries (for example, http://email.hasgeek.com/wf/click?upn=GNxjqnaF4XBry8wapt5A9wNzxaawyAxW3B-2FDTKtianbWZ9D5Q9e9uM6ygi5aERfAKw58ue4EvohSFbU41EKlmC9bhePqCxHs7FTeBWMtX2s35fzXcc6KddMBmoyOFly6_FVP9ITVZttLCsZ9Lh-2FYnwKbnM99IWToYugCu4zOUf7jakxRjopsvbRCbxJrO0YnVX8S6AMDSIFMb3z5ukUInmIvRy5gfaPCsPUOv8ArK-2FH5lrpmbAl98xDkXjT-2BpI-2BwJWwPGvzHPd-2FCg-2FJXk-2BzJg275btFGpZvx-2Bt-2B4k6gH0NT6nLR5ENgeLLlwuiQma06tLMW4ChUg2XdkBJV9lgaKIQg-3D-3D, or e.g ).'''
import re

def stop_positions(line):
	if re.search(r"[.?!]+",line):
		stops = re.search(r"[.?!]+",line).group()
   		stop_pos = line.find(stops)
   		stop_pos = stop_pos+len(stops)-1
   	else:
   		stop_pos=-1
   	return stop_pos


if __name__ == "__main__":
	f = open('para_to_sentence_test.txt',"r") #test cases are stored in para_to_sentence_test.txt

	for line in f:
		line = line.strip()
		while line:
			pos = stop_positions(line)
			if pos>0:
				line_nxt = line[:pos+1].split(" ")
				length = len(line_nxt)
				last_word = line_nxt[length-1]

				try:
					if re.search(r"[A-Z]+.*", last_word) or line[pos+1]!= " " or line[pos+2].islower():
				
						print line[:pos+1],
						line = line[pos+1:]

					else:
						print line[:pos+1]
						line = line[pos+1:]
				except:
					print line
					line = ""

			else :
				print line
				line = ""

	f.close()


