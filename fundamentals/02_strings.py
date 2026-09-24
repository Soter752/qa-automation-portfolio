name = "Matt"
passed = 231
total = 250
rate = passed / total
print(f"Cześć {name}!")
print(f"Zdane: {passed}/{total}")
print(f"Pass rate: {rate:.1%}")
print(f"Czas: {3.14159:.2f} s")

url = "https://www.saucedemo.com/inventory.html"
print(len(url)) # 40 — liczba znaków
print(url[0])  # h — pierwszy znak (liczymy od 0
print(url[0:5]) # https — znaki 0..4, koniec jest wyłączny
print(url[-4:]) # html — cztery ostatnie
print("dupa" in url) # True lub jak teraz false
print(url.upper()) # HTTPS://WWW.SAUCEDEMO.COM/INVENTORY.HTML

age_text = input("ile masz lat? ")
age = int(age_text)
print(f"Twój wiek za 10 lat: {age + 10}")

suite = "Smoke"
passed = 18
failed = 2
duration = 74.4567
rate = passed / (passed+failed)
print(f"{suite}: {passed} passed, {failed} failed ({rate:.1%}) in {duration:.2f}s" )

email = "tester.matt@example.com"
at = email.index("@")
login = email[:at]
domain = email[at +1:]
print(login)
print (domain)

name = input("Imię: ")
birth_year = int(input("Rok orodzenia: "))
print(f"{name}, wiek w 2026 roku: {2026 - birth_year}")