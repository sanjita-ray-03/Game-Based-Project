a = input("What is your name?: ")
b = input("What is your bid?: ")

data={"Name: ": a , "Bid: ": b}
main_list=[]
main_list.append(data)
c=input("Are there any other bidders? (yes/no): ")

while(c == "yes"):
    a = input("What is your name?: ")
    b = input("What is your bid?: ")
    data={"Name: ": a , "Bid: ": b}
    main_list.append(data)
    c=input("Are there any other bidders? (yes/no): ")

print(main_list)
largest= int(main_list[0]["Bid: "])
x=0
for i in range(len(main_list)):
    if(int(main_list[i]["Bid: "])> largest):
        largest = int(main_list[i]["Bid: "])
        x = i
print(f"The winner is {main_list[x]["Name: "]} with the price {main_list[x]["Bid: "]}")