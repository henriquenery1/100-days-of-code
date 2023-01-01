from day3 import find_veg

grill = [
  "--oooo-ooo--",
  "--xx--x--xx--",
  "--o---o--oo--",
  "--xx--x--ox--",
  "--xx--x--ox--"
]

second_grill = [
  "--oooo-ooo--",
  "--xxxxxxxx--",
  "--o---",
  "-o-----o---x--",
  "--o---o-----"
]

print(find_veg(grill) == [2, 3])

print(find_veg(second_grill) == [3, 2])