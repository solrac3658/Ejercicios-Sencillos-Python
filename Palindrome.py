def palindrome (word):
	reverse_word=""
	for i in reversed (range(len(word))):
		if word[i] != " ":
			reverse_word += word[i]
	return reverse_word.lower() == word.lower()

print(palindrome("Malayalam"))