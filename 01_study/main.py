#import my_math
#import my_math as m
#from lib.my_math import add # lib파일 밑에 있다면
from my_math import add
a, b = map(int, input().split())
print(add(a, b))