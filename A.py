num_cars=int(input())
speed=list(map(int,input().split()))
per=1

if num_cars!=0:
  for i in range(1,num_cars+1):per*=i
  Sum=1
  for i in range(1,num_cars+1):Sum=Sum+(1/i)

  groups=int((per*Sum)-per)
  output=groups/per

  print("{:.6f}".format(output))
  print("\n")

  
  
else:
  print("0\n")