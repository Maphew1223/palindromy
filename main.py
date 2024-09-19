def palindrom_check(word):
    if word == word[::-1]:
        return True
    else:
        return False
print(palindrom_check("kajak"))
print(palindrom_check("kamilślimak"))
print(palindrom_check("konstantynopolitańczykowianeczka"))

print()

user_word = input("Podaj słowo: ")
if palindrom_check(user_word):
  print(f'Słowo {user_word} jest palindromem')
else:
  print(f'Słowo {user_word} nie jest palindromem')