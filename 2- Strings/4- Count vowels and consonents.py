# Assumption 1: All characters are lower case
# Assumption 2: String may include special characters

vowels = "aeiou"

str1 = "__hel lo 123$world "
vowel_count = 0
consonant_count = 0

for character in str1:
    if character.isalpha():
        if character in vowels:
            vowel_count = vowel_count + 1
        else:
            consonant_count = consonant_count + 1
print(f"There are {vowel_count} vowels and {consonant_count} consonents in this string")