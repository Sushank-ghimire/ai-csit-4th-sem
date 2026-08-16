# Dictionary containing words and their base forms
lemma_dict = {
  "students": "student",
  "student": "student",
  "studies": "study",
  "studying": "study",
  "studied": "study",
  "playing": "play",
  "played": "play",
  "plays": "play",
  "games": "game",
  "better": "good",
  "best": "good",
  "mice": "mouse",
  "children": "child",
  "men": "man",
  "women": "woman",
  "cars": "car",
  "running": "run",
  "ran": "run",
  "eating": "eat",
  "ate": "eat"
}


def lemmatize_word(word):
  word = word.lower()

  if word in lemma_dict:
    return lemma_dict[word]

  return word

sentence = input("Enter a sentence: ")

words = sentence.split()

print("\nLemmatization Result")
print(f"{'Word':<20}{'Lemma':<15}")
print("-" * 40)

for word in words:
  lemma = lemmatize_word(word)
  print(f"{word:<20}{lemma:<15}")
