import random

def get_numbers_ticket(min,max,quantity):
    if min>=1 and max <=1000 and quantity>=1 and quantity<=1000:
        try:
            numbers=[]
   
            for number in range(min-1,max):
                number+=1
                numbers.append(number)

            sets=random.sample(numbers,k=quantity)
            sets.sort()
            return print(sets)
        except:
            print("datasets isnt correct")
    else:
        print("dont work")
        
    
get_numbers_ticket(1,36,6)