text = input("Enter a text: ")

word_tokens = text.split()

sentence_tokens = []
sentence = ""

for char in text:
  sentence += char

  if char in ".!?":
    sentence_tokens.append(sentence.strip())
    sentence = ""

if sentence.strip():
  sentence_tokens.append(sentence.strip())

print("\nWord Tokenization")
for i, word in enumerate(word_tokens, start=1):
  print(f"{i}. {word}")


print("\nSentence Tokenization")
for i, sentence in enumerate(sentence_tokens, start=1):
  print(f"{i}. {sentence}")
