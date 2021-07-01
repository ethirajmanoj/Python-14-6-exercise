
# -------- variables --------

x = 10
y = 10

# is the following  a valid python statement
# What do you think will be the values of x and y
# How would you correct it

x = y = 10 
x, y = 10
x, y = 10, 10

# -------- functions & List --------

INVALID_INPUT = "Invalid Input" 

def area_of_square(passs):
    if type(passs) != int:
        return INVALID_INPUT
    else:
        length = passs * passs
        return length

    # takes `length` as input
    # returns area of square
    # return INVALID_INPUT :: for improper input
    #pass
passs = 25
output = area_of_square(passs)
print(output)


#def calculate_area_of_square_with_list():
    mn = []
def calculate_area_of_square_with_list(lengths):
     if type(lengths) != int:
        return INVALID_INPUT
     else:
        output = lengths * lengths
        return output
pass
lengths = [15,30,35]
for y in lengths:
    z = calculate_area_of_square_with_list(y)
    mn.append(z)
print(mn)
    # add func param `lengths`
    # Loop through `lenghts`, find area and return a list 
    # Modify the code to get `lengths` as a param
    #pass



def area():
    def area(shp,lgn):
    if sq == "square":
        if type(lgn) != int:
            return INVALID_INPUT
        else:
            output = lgn * lgn
            return output
    elif sq == "circle":
        if type(lgn) != int:
            return INVALID_INPUT
        else:
            output = 3.14 * lgn * lgn
            return output

    # modify this function which takes two params `(shape, length)` and returns area of the shape. 
    # possible values for shape is square & circle alone
    # return INVALID_INPUT :: for improper input
    # think if you can re-use a function from before
    pass
x = "square"
r = 10
z1 = area(x,r)
print("Shape: " + x)
print("Input: " + str(r))
print("Area: " + x + " : " + str(z1))
x = "circle"
r = 20
z1 = area(x,r)
print("Shape : " + x)
print("Input : " + str(r))
print("Area :" + x + " : " + str(z1))





def calculate_area_with_list():
    if sq == "square":
        if type(len) != int:
            return INVALID_INPUT
        else:
            output = len * len
            return output
    elif sq == "circle" :
        if type(len) != int:
            return INVALID_INPUT
        else:
            output = 3.14 * len * len
            return output
    
    # get an input param `shapes` with list of [(`shape_type, length`)] 
    # Loop through find area and return a list 
    # Modify the code to get `shapes` as a param
    # return INVALID_INPUT :: for improper input
    pass
sq = []
shapes = ['square', 'circle']
r = 20
for x in shapes:
    z1 = area(x, r)
    sq.append("Shape:" + x)
    sq.append("Input:" + str(r))
    sq.append("Area :" + x + " is " + str(z1))
    print(sq)
    pass


# ------- Function + String  --------


#def profile(name, email, designation):
    # check name and email cannot be empty, if empty return INVALID_INPUT
    # return a string which combines the above parameters one line after another
    #pass
name = 'Manoj'
email='met-in@flsmidth.com'
designation='Process Automation Specialist'
def profile(name, email, designation):

    if not name or not email:
        print("Name or email is: " + INVALID_INPUT)
    else:
        print('Name: ' + name + '\n' + 'Email: ' + email + '\n' +'Designation: '+ designation)
pass
Output = profile(name, email, designation)


# ------- Function + Dict  --------

def profile_with_dict(profile_dict):
    # read name, email, designation, about_you from profile_dict 
    # return a string which combines the above parameters one line after another
    # What happens if one of the element is not available
    # add a check to ensure that the name should be in all caps
    # change the name to all caps even if the input is not
    # return INVALID_INPUT :: for improper input
    pass
name = 'Manoj'
email='met-in@flsmidth.com'
designation='Process Automation Specialist'

profile_dict = {'about_you':{'Name':name,
        'Email':email, 'Designation':designation}}
def profile_with_dict(profile_dict):
    for a in profile_dict:
        if not name or not email or not designation: 
                print ( INVALID_INPUT)
                exit()
        else:
            print(a)
        for b in profile_dict[a]:      
            
                if b == 'Name':
                    if  (profile_dict[a][b].isupper()) == True:
                         print (b,':',profile_dict[a][b])
                    else:                   
                        print (b,':', profile_dict[a][b].upper())
                else:
                    print (b,':',profile_dict[a][b])              



# try calling profile(**profile_dict) -> Did it work? How?

# ----------- More Lists -----------
# Write a function called `middle` that takes a list 
# returns a new list that contains all but the first and last elements
#pass
#Output = profile_with_dict(profile_dict)
num = ([1,2,3,4])
   
def midl(num):
    mid = num[:]
    del mid[0]
    del mid[len(mid)-1]
    return mid
pass
print(midl(num))



# ------------ Functions ------------

# Write a function that reads the input repeats it(prints the same) until it recieves `end` or `stop`
# HINT :: Think Recursion
name = 'Manoj'
def numb(name):
  i = 1
  while i < 11:
    print(name)
    if i == 11:
        break
    i += 1
output = numb(name)




#  ----- Test cases -------
# comment out the part you are working with 


# assert x == 10 
# assert y == 10



# assert area_of_square(4) == 16
# assert area_of_square(0) == 0
# assert area_of_square("abs") == INVALID_INPUT
# assert calculate_area_of_square_with_list([4, 0, "abs", None]) == [16, 0, INVALID_INPUT, INVALID_INPUT]


# assert area("square", 4) == 16
# assert area("circle", 4) == 50 # just use int
# assert area("rectangle", 4) == INVALID_INPUT
# assert area("rectangle", 0) == INVALID_INPUT

# shapes = [
#     ("square", 4),
#     ("circle", 4),
#     ("rectangle", 4),
#     ("square", 0),
#     ("sqaure", None)
# ]
# assert calculate_area_with_list(shapes) == [16, 50, INVALID_INPUT, 0, INVALID_INPUT]

# params = {
#     "name": "Bhavani",
#     "email": "example@eg.com",
#     "designation": ""
# }

# result = f"{params['name']}\n{params['email']}\n{params['designation']}"

# assert profile(**params) == result

# assert profile_with_dict(params) == result


# print ("All good...")