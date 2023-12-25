def p1(s: str):
  counter = 0
  pos = 0
  for char in s:
    pos += 1
    if char == '(':
      counter += 1
    else:
      counter -= 1
    if counter == -1:
      return pos

with open('input.txt', 'r') as file:
    print(p1(file.read()))