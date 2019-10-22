
def oddOne(pa):
    x=0
    for i in pa:
        x=x^i
    return x

people_ages = list(map(int,input("enter the ages of people present").split()))
print(oddOne(people_ages))
