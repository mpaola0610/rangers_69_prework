def hello_name(username):
     print('hello_' + username.upper() + '!')
    
hello_name('billie jon')    


odd_numbers = list(range(1,201,2))
print(odd_numbers)


def max_num_in_list(a_list):
     a_list.sort()
     print(a_list[-1])
   
list = [2, 4, 8, 17, 22]
max_num_in_list(list)

def is_leap_year(a_year):
     if a_year % 4 == 0:
          if a_year % 100 == 0:
               if a_year % 400 == 0:
                    return True
               else:
                   return False
          else: 
             return True
     else:
       return False

lucky = is_leap_year(2027)
print(lucky)

def is_consecutive(a_list):
    x = a_list
     for number in a_list:
          if number = x + 1:
               number = x
               return True 
          else:
            return False                               
          

     

  

