from day2 import find_nemo

print(find_nemo("I am finding Nemo !") == "I found Nemo at 4!")

print(find_nemo("Nemo is me") == "I found Nemo at 1!")

print(find_nemo("I Nemo am") == "I found Nemo at 2!")

print(find_nemo("I am") == "Nemo is not in list")