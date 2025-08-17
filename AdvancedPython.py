
#Unpacking with * (splat operator)
nums = [1, 2, 3, 4, 5]
first, *middle, last = nums
print(first, middle, last)  # 1 [2, 3, 4] 5

# Unpacking with * in function arguments
def func(*args):
    print(args)

func(1, 2, 3)  # (1, 2, 3)

# Unpacking with ** (double splat operator)
def func(**kwargs):
    print(kwargs)

func(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}     

#Inline if (ternary operator)
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)