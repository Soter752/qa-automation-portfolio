test_name = "Logowanie poprawnym hasłem"
steps = 5
duration = 2.75
passed = True

print(test_name)
print(type(test_name))
print(type(steps))
print(type(duration))
print(type(passed))

#arytmetyka
total_tests = 120
failed = 7
print(total_tests - failed)
print(failed / total_tests)
print(total_tests // 50)
print(total_tests % 50)
print(2 ** 10)

#konwersja między typami
status_code = "200"
print(status_code == 200)
print(int(status_code) == 200)


all_tests = 250
passed = 231
skipped = 4

failed_tests = all_tests - passed - skipped
pass_rate = passed / all_tests * 100
print(failed_tests)
print (pass_rate)