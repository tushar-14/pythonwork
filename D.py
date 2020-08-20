num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
            90: 'ninety', 0: 'zero',100:'hundred'}

def n2w(n):
    if n<21:
        return num2words[n]
    else:
        return num2words[n-(n%10)] + num2words[n%10]

N=int(input())
l1=list(map(int,input().split()))
l2=[]
l3=['a','e','i','o','u']
count=0
for i in l1:
  l2.append(n2w(i))
for i in l2:
    for x in i:
        if x in l3:
            count=count+1 
D=count
count1 = 0
for i in range(0, len(l1)): 
    for j in range(i + 1, len(l1)): 
        if l1[i]+l1[j] ==D:
            count1 +=1

if count1>100:
  print("greater hundred\n")
else:
    print(n2w(count1)+"\n")
