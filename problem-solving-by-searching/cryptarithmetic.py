# Cryptarthmetic Problem Solving
first_str = input("Enter first string: ").strip().upper()
second_str = input("Enter second string: ").strip().upper()
resulting_str = input("Enter the resulting string: ").upper()

non_repeating_letters = set(first_str + second_str + resulting_str)

if len(non_repeating_letters) > 10:
    print("No solutions")
    exit()

mapping = {}
used_digits = set()

leading_letters = {first_str[0], second_str[0], resulting_str[0]}

letters = list(non_repeating_letters)

def word_to_num(word):
    num = ""
    for ch in word:
        num += str(mapping[ch])
    return int(num)


def backtrack(idx):
    if idx == len(letters):
        n1 = word_to_num(first_str)
        n2 = word_to_num(second_str)
        n3 = word_to_num(resulting_str)

        if n1 + n2 == n3:
            print("\nSolution Found: ")
            for ch in sorted(mapping):
                print(f"{ch} = {mapping[ch]}")
            print(f"\n{n1} + {n2} = {n3}")
            return True
        return False
    curr_letter = letters[idx]

    for digit in range(10):
        if digit in used_digits:
            continue
        if digit == 0 and curr_letter in leading_letters:
            continue
        mapping[curr_letter] = digit
        used_digits.add(digit)

        if backtrack(idx + 1):
            return True
        del mapping[curr_letter]
        used_digits.remove(digit)
    return False

if not backtrack(0):
    print("No solution exists")
