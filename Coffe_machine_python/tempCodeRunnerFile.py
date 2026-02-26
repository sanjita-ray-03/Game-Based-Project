choice= input("Enter your Choice: ")
for i in range(len(data_base.data)):
    if(choice==data_base.data[i]["Name"]):
        print(f"You have to pay: {data_base.data[i]["Price"]}")
        print(f"Here is your {data_base.data[i]["Name"]}")
    