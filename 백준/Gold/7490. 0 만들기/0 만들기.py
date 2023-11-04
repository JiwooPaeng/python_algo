def num_string(s, nums):
  global n
  nums += str(s)

  if s == n:
    calc(nums)
    return

  num_string(s + 1, nums + ' ')
  num_string(s + 1, nums + '+')
  num_string(s + 1, nums + '-')

def calc(nums):
  nums_modified = nums.replace(' ', '')
  ans = eval(nums_modified)
  if ans == 0:
    print(nums)

tc = int(input())

for _ in range(tc):
  n = int(input())

  s = 1
  nums = ''
  num_string(s, nums)

  print()