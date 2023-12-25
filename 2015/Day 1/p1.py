def p1(s: str):
  counter = 0
  for char in s:
    if char == '(':
      counter += 1
    else:
      counter -= 1
  return counter

with open('input.txt', 'r') as file:
    print(p1(file.read()))