print("Insert marks below(if not known type zero)")
print("mathematics")
inp = int(input())
print("hindi")
inp1 = int(input())
print("english")
inp2 = int(input())
print("science")
inp3 = int(input())
print("sst")
inp4 = int(input())
print("IT")
inp5 = int(input())
if inp5 == 0:
    print((inp + inp1 + inp2 + inp3 + inp4)/4)
else:
    print((inp + inp1 + inp2 + inp3 + inp4 + inp5)/4.5)

