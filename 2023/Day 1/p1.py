def calibrationVal(s: str) -> int:
    nums = []
    for char in s:
        if char.isnumeric():
            nums += char
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        val = nums[0] + nums[-1]
        return int(val)
    
def solution(s: str):
    txt = s.split(' ')
    #for data in txt:
        

file = open('input.txt', 'r')
lines = file.readlines()
# solution("rwoapropw xD")