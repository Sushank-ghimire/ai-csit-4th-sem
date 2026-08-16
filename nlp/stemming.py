def stem_word(word):
  word = word.lower()
  suffixes = ["ing", "ed", "ly", "ies", "es", "s"]

  for suffix in suffixes:
    if word.endswith(suffix) and len(word) > len(suffix) + 2:
      word = word[:-len(suffix)]
      break

  return word

sentence = input("Enter a sentence: ")

words = sentence.split()

print("\nStemming Result")
print(f"{'Word':<20}{'Stem':<15}")
print("-" * 40)

for word in words:
    stem = stem_word(word)
    print(f"{word:<20}{stem:<15}")
