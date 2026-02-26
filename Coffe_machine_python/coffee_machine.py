import coffee_art
import data_base

user= "yes"
print(coffee_art.logo)
name= input("Enter your name: ")
print(f"Hello {name} !! What would you like to have? ")

def coffee_machine(choice, income):
    
    for i in range(len(data_base.data)):
        if(choice == data_base.data[i]["Name"]):
            data_base.Storage["Milk"]= data_base.Storage["Milk"] - data_base.data[i]["Milk"]
            data_base.Storage["Coffee"]= data_base.Storage["Coffee"] - data_base.data[i]["Coffee"]
            data_base.Storage["Sugar"]= data_base.Storage["Sugar"] - data_base.data[i]["Sugar"]
            data_base.Storage["Water"]= data_base.Storage["Water"] - data_base.data[i]["Water"]
            # data_base.Storage["Milk"]= data_base.Storage["Milk"] - data_base.data[i]["Milk"]
            if(income == data_base.data[i]["Price"]):
               data_base.Storage["Balance"] = data_base.Storage["Balance"] + income
            elif(income>data_base.data[i]["Price"]):
                refund = income - data_base.data[i]["Price"]
                data_base.Storage["Balance"] = data_base.Storage["Balance"] + data_base.data[i]["Price"]
                print(f"Your Refund is: {refund}")
            else:
                print("This is not enough!!")
                # return left
                
    
print("Here is your menu:\n")


while(user=="yes"):  
    for i in range(len(data_base.data)):
        print(f"Coffee Name: {data_base.data[i]["Name"]} Price: {data_base.data[i]["Price"]}")

        
        
    choice= input("Enter your Choice: ")
    for i in range(len(data_base.data)):
        if(choice==data_base.data[i]["Name"]):
            print(f"You have to pay: {data_base.data[i]["Price"]}")
            income=int(input("Give Money: "))
            
            
    coffee_machine(choice, income)   
    user= input("Wanna add more?\nYes or No")

print(data_base.Storage)
    
