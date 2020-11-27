# -*- coding: utf-8 -*-
a=input("숫자를 입력하세요")
b=int(a)
for i  in range(1,b+1):
  for i  in range(1,i):
    print("*", end='')
  print("")

