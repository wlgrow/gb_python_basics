from sys import argv


script_name, production, rate, prize = argv
print(f"employee salary: {float(production) * float(rate) + float(prize)}")
