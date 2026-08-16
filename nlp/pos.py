# Program to implement Part-of-Speech (POS) Tagging
pos_names = {
  "DT": "Determiner",
  "PRP": "Pronoun",
  "CC": "Conjunction",
  "IN": "Preposition",
  "VB": "Verb",
  "VBG": "Verb (Gerund/Present Participle)",
  "RB": "Adverb",
  "JJ": "Adjective",
  "NN": "Noun",
  "NNS": "Plural Noun",
  "CD": "Cardinal Number"
}

def pos_tag(word):
  word = word.lower()

  # Determiners
  if word in ["a", "an", "the"]:
    return "DT"

  # Pronouns
  elif word in ["i", "you", "he", "she", "it", "we", "they"]:
    return "PRP"

  # Conjunctions
  elif word in ["and", "or", "but", "because"]:
    return "CC"

  # Prepositions
  elif word in ["in", "on", "at", "by", "with", "from", "to", "of"]:
      return "IN"

  # Common auxiliary verbs
  elif word in ["is", "am", "are", "was", "were", "be", "been", "being"]:
      return "VB"

  # # Common verbs
  # elif word in ["run", "runs", "eat", "eats", "play", "plays", "study", "studies", "read", "reads"]:
  #   return "VB"

  # Words ending with "ing" are treated as verbs
  elif word.endswith("ing"):
    return "VBG"

  # Words ending with "ly" are treated as adverbs
  elif word.endswith("ly"):
    return "RB"

  # Words ending with "ous", "ful", "able" are treated as adjectives
  elif word.endswith(("ous", "ful", "able")):
    return "JJ"

  # Numbers
  elif word.isdigit():
    return "CD"

  # Words ending with "s" are treated as plural nouns
  elif word.endswith("s"):
    return "NNS"

  # Default: noun
  else:
    return "NN"


# Take input from user
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Display POS tags
print("\nPart-of-Speech (POS) Tags")
print(f"{'Word':<20}{'Tag':<10}{'Full Form':<40}")
print("-" * 40)

for word in words:
  tag = pos_tag(word)
  full_form = pos_names[tag]
  print(f"{word:<20}{tag:<10}{full_form:<40}")
