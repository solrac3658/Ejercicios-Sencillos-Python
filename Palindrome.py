def palindrome (word):
	reverse_word=""
	word=word.replace(" ","")
	for i in reversed (range(len(word))):
		reverse_word += word[i]
	return reverse_word.lower() == word.lower()

print(palindrome("Amad a la dama"))

