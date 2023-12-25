def calibrationVal(s: str) -> int:
    nums = []
    for i, char in enumerate(s):
        if char.isdigit():
            nums.append(char)
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if s[i:].startswith(val):
                nums.append(str(d + 1))
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return int(nums[0] * 2)
    else:
        val = nums[0] + nums[-1]
        return int(val)

def solution(txtInput):
    total = 0
    for line in txtInput:
        total += calibrationVal(line)
    return total

with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

text = "1abc2 pqr3stu8vwx a1b2c3d4e5f treb7uchet"
test = text.split(' ')
# print(calibrationVal('eightwothree'))

print(solution(lines))