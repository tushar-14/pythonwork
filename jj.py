from itertools import combinations

num_cars=int(input())
speed=list(map(int,input().split()))

per=1
for i in range(1,num_cars+1):per*=1
  
total_com=[combinations(speed,i) for i in range(1,num_cars+1)]

print(len(total_com)/per)