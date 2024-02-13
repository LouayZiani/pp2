# Task 6:

def reverse(sentence):
    words = sentence.split() 
    reversed_words = reversed(words) 
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

text = input("Enter a sentence: ")
reversed_sentence = reverse(text)
print("Reversed sentence:", reversed_sentence)
