name = input("Nazwa testu: ").strip()
steps = int(input("Liczba kroków: "))
seconds_per_step = float(input("Sekundy na krok: "))
priority = input("Priorytet: ").strip().upper()
autor = "Matt"


total_minutes = steps * seconds_per_step / 60
line = "=" * 30

print(line)
print(f" TC: {name}")
print(f" {'Kroki:':<11} {steps}")
print(f" {'Czas:':<11} {total_minutes:.1f} min")
print(f" {'Priorytet:':<11} {priority}")
print(f" Autor: {autor}")
print(line)
