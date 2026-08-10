import random
import time


#--dice roll--
def dice():
    roll=random.randint(1,6)
    return(roll)
 
 

  
  
 #----snake----
def snake(user_pos, bot_pos,user3_pos=0,user4_pos=0):

    snakes = {
        92:69,
        53:49,
        75:64,
        25:17,
        11:9,
        99:2
     }
    if(prince==1):
        if user_pos in snakes:
            print("🐍 Player bitten by snake!")
            user_pos = snakes[user_pos]
        if bot_pos in snakes:
            print("🐍 Bot bitten by snake!")
            bot_pos = snakes[bot_pos]
        return user_pos, bot_pos
    elif(prince == 2):
        if user_pos in snakes:
            print("👤Player1 bitten by snake!")
            user_pos = snakes[user_pos]
        if bot_pos in snakes:
            print("😛Player2 bitten by snake!")
            bot_pos = snakes[bot_pos]
        return user_pos, bot_pos
    elif(prince==3):
        if user_pos in snakes:
            print("👤Player1 bitten by snake!")
            user_pos = snakes[user_pos]
        if bot_pos in snakes:
            print("😛Player2 bitten by snake!")
            bot_pos = snakes[bot_pos]
        if user3_pos in snakes:
            print("😁player_3 bitten by snake!")
            user3_pos=snakes[user3_pos]
        return user_pos, bot_pos,user3_pos
    elif(prince==4):
        if user_pos in snakes:
            print("👤Player1 bitten by snake!")
            user_pos = snakes[user_pos]
        if bot_pos in snakes:
            print("😛Player2 bitten by snake!")
            bot_pos = snakes[bot_pos]
        if user3_pos in snakes:
            print("😁player_3 bitten by snake!")
            user3_pos=snakes[user3_pos]
        if user4_pos in snakes:
            print("😆Player_4 bitten by a snake")
            user4_pos=snake[user4_pos]   
        return (user_pos, bot_pos,user3_pos ,user4_pos)  
            
            
    

def ladder(user_pos, bot_pos,user3_pos=0,user4_pos=0):
    
    ladder={
        14:87,
        40:80,
        23:43,
        50:70
     }
    if(prince== 1):
        if user_pos in ladder:
            print("❇️Player got a ladder🪜")
            user_pos=ladder[user_pos]
        if bot_pos in ladder:
            print("❇️bot got a ladder 🪜")
            bot_pos=ladder[bot_pos]
        return (user_pos,bot_pos)   
    elif(prince == 2):
        if user_pos in ladder:
            print("👤Player1 got a ladder🪜")
            user_pos=ladder[user_pos]
        if bot_pos in ladder:
            print("😛player2 got a ladder 🪜")
            bot_pos=ladder[bot_pos]
        return (user_pos,bot_pos)
    elif(prince== 3):
        if user_pos in ladder:
            print("👤Player_1 got a ladder🪜")
            user_pos=ladder[user_pos]
        if bot_pos in ladder:
            print("😛player_2 got a ladder 🪜")
            bot_pos=ladder[bot_pos]
        if user3_pos in ladder:
            print("😁Player_3 got a ladder 🪜") 
            user3_pos=ladder[user3_pos]   
        return (user_pos,bot_pos,user3_pos)
    elif(prince==4):
        if user_pos in ladder:
            print("👤player_1 got a ladder 🪜")
            user_pos=ladder[user_pos]
        if bot_pos in ladder:
            print("😛player_2 got a ladder 🪜")
            bot_pos=ladder[bot_pos]
        if user3_pos in ladder:
            print("😁player_3 got a ladder 🪜")
            user3_pos=ladder[user3_pos]
        if user4_pos in ladder: 
            print("😆player_4 got a ladder 🪜")
            user4_pos=ladder[user4_pos]
        return(user_pos,bot_pos,user3_pos,user4_pos)          
            


