# Odbierz od użytkownika 5 adresów email. Sprawdź, czy adres zawiera @ oraz .com lub .pl, jeśli tak to dodaj adres do
# listy. Na koniec zamień listę na zbiór. Wyświetl ilość prawidłowych adresów email i wypisz je.
emails = []
for i in range(1, 6):
    email = input(f'Podaj przykładowy adres email ({i}/5): ')
    if '@' in email and (email.endswith('.com') or email.endswith('.pl')):
        emails.append(email)

print('Ilość prawidłowych adresów podanych przez użytkownika, to:', len(emails))
emails = set(emails)
print('Prawidłowe adresy email, to: ', emails)