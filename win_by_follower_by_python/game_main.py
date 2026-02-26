import data_base
import game_art
import random
flag=True
count=0
print(game_art.gameLogo)
def comparison(Follower_1, Follower_2,response):
        
        if(response==1):
            if(Follower_1>Follower_2):
                return True
            else:
                return False
        else:
            if(Follower_2>Follower_1):
                return True
            else:
                return False
            

def check(Follower_1,Follower_2,response,flag):
    compare= comparison(Follower_1, Follower_2,response)
    if(compare==True):
        
        global count
        count= count+1
        flag=True
        print(f"Hurrah!!You won\nYou got {count}")
        return flag
            
    else:
        print(f"Sorry!!! You are Wrong\nYour Score {count}")
        flag=False
        return flag


while(flag==True):
    if(player_1!= player_2):
        player_1 = random.choice(data_base.data)
        player_2 = random.choice(data_base.data)

        Name_1= player_1["Name"]
        Country_1 = player_1["Country"]
        Occupation_1 = player_1["Occupation"]
        Follower_1 = player_1["Follower"]

        Name_2= player_2["Name"]
        Country_2 = player_2["Country"]
        Occupation_2 = player_2["Occupation"]
        Follower_2 = player_2["Follower"]
        print("Who's follower is more\n\n")
        print(f" {Name_1} from {Country_1} is {Occupation_1}")
        print(game_art.vs)
        print(f" {Name_2} from {Country_2} is {Occupation_2}")
        response=int(input(f"Type-1 for {Name_1} \nType-2 for {Name_2}: "))
        flag=check(Follower_1,Follower_2,response,flag)
    


   