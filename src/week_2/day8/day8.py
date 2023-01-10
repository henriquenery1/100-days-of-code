KEYBOARD = {
  "2": ["a","b","c"],
  "3": ["d","e","f"],
  "4": ["g","h","i"],
  "5": ["j","k","l"],
  "6": ["m","n","o"],
  "7": ["p","q","r", "s"],
  "8": ["t","u","v"],
  "9": ["w","x","y","z"],
}

def find_combinations(digits):
    if len(digits) == 1 and int(digits[0]) > 1:
        return KEYBOARD[digits[0]]
    elif len(digits) == 0:
        return []

    temp_array=[]

    for i in digits[1:]:
        temp_array+=KEYBOARD[i]

    combinations = [ x+y for x in KEYBOARD[digits[0]] for y in temp_array ]

    return combinations