ch = input("Enter a letter: ").strip().lower()
if len(ch) == 1 and ch.isalpha():
    print("Vowel" if ch in "aeiou" else "Consonant")
else:
    print("Invalid input")
