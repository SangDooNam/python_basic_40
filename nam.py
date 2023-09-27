"""Task 1"""

# def isOdd(num):
    
#     if num % 2 != 0:
        
#         return True
#     else:
#         return False




# def isEven(num):
    
#     if num % 2 == 0:
        
#         return True
#     else:
#         return False
    
# print(isOdd(1), isEven(1))
# print(isOdd(657842), isEven(657842))
# print(isOdd(0), isEven(0))


#----------------------------------------------------



"""Task 2"""

# def getParity(num, string):
    
#     if string == 'even':
#         return num % 2 == 0
#     elif string == 'odd':
#         return num % 2 != 0
#     else:
#         return f'Parity indicated is unknown'
    
# print(getParity(5, 'odd'))

#----------------------------------------------------

"""Task 3"""

# from datetime import datetime as dt, time as time


# def greet(name, date):
    
#     noon = time(12,0)
#     sixPM = time(18,0)
#     sixAM = time(6,0)
#     zerohour = time(0,00)
#     ninePM = time(21,0)
    
#     if sixAM < date.time() < noon:
        
#         return f'Good Morning, {name}!'
    
#     elif sixPM > date.time() > noon:
        
#         return f'Good Afternoon, {name}!'
    
#     elif ninePM > date.time() > sixPM:
        
#         return f'Good Evening, {name}!'
#     else:
#         return f'Good Night, {name}!'


# print(greet(
#     name="John",
#     date=dt(2021, 5, 7, 6, 59, 59)
#     ))
# print(greet(
#     date=dt(2021, 5, 7, 12, 0, 1),
#     name="John"
#     ))


#----------------------------------------------------

"""Task 4"""


# test1 = [[0, 2, 4, 5]]
# test2 = [
#     [0, 2, 4, 5],
#     [6],
#     [0, 2, 4, 5, 1, 4, 3, 2]
# ]
# test3 = [1, 2, 3, [4, 5, 6], 7, [8, 9]]

# def sumAll(*lst):
    
#     print(lst)
    
# sumAll(*test1, *test2, *test3)

# sumAll(*test3)

# for i in test1:
#     print('here is first level--------')
#     print(i)
#     print('here is second level--------')
#     for e in i:
        
#         print(e)
        
        
            
# print('---------')

# for i in test2:
#     print('here is first level--------')
#     print(i)
#     print('here is second level--------')
#     for e in i:
        
#         print(e)
        


# def sumAll(*lst):
#     total = 0
#     for i in lst:
#         for e in i:
#             total += e
#     return total


# print(sumAll(*test1))
# print(sumAll(*test2))

#------------------------------------------------

# def sumAll(*lst):
    
#     total = 0
    
#     for i in lst:
        
#         if isinstance(i, (int, float)):
            
#             total += i
        
#         elif isinstance(i, (list)):
            
#             for e in i:
                
#                 if isinstance(e, (int, float)):
                    
#                     total += e
                
#                 # elif isinstance(e, (list)):
                    
#                 #     for f in e:
                        
#                 #         total += f
                    
#     return total


# print(sumAll(*test1))
# print(sumAll(*test2))



"""Task 5"""

test1_data = ["Word", "Apple"]
test1_config = {}

test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oy"}

test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}


def pig_latin(*strings, suffix = 'ay', single = False):
    
    vowels = ['a','e','i','o','A','E','I','O']
    
    container = []
    
    for i in strings:
        
        if i[0] in vowels:
            
            addition = i + suffix
            # container += [addition2.capitalize()]
            
        else:
            
            reform = i[1:] + i[0]
            addition = reform + suffix
            # container += [addition.capitalize()]
            
        container.append(addition.capitalize())
            
    if single == True:
        
        return (' '.join(container)).capitalize()
    else:
        
        return container


print(pig_latin(*test1_data)) 
print(pig_latin(*test2_data, **test2_config))  
print(pig_latin(*test3_data, **test3_config))  
