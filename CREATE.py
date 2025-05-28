#create

#citations: https://www.cheesies.com/ , https://www.pizzametro.com/ ,
# https://order.portillos.com/menu/portillos-hot-dogs-chicago/ , http://pupuseriachicago.com/ ,
# https://www.mccbchicago.com/gallery?lightbox=dataItem-j6lcpe9x3 ,
#  https://macarthursrestaurant.com/menu/ ,https://el-cubanito.cuba-cafe.com/#menu ,
#  https://lacocospizza.hungerrush.com/Order/Menu/1#wingsandtenders ,
# https://chicago-pizza-and-oven-grinder-company.pops-cafe.com/#menu

import random
from PIL import Image
import requests
from io import BytesIO
food = 0

restaurants = ["Cheesies" , "Pizza Metro" , "Portillos" , "Pupuseria" , "MCCP Chicago",
               "MacArthur's","cubanitos", "Lacoco's", "Oven Grinder"]
               
pics = ["https://www.cheesies.com/wp-content/uploads/2023/08/IMG_0138.jpeg" ,
        "https://www.pizzametro.com/wp-content/uploads/2024/10/pizza-2-1024x625-500x305.jpg" ,
          "https://tinyurl.com/2z455jj7"
            , "https://th.bing.com/th/id/OLC.I97Ja3Dt2JaNKg480x360?&rs=1&pid=ImgDetMain" ,
            "https://tinyurl.com/4f5ea66w" ,
            "https://th.bing.com/th?id=OLC./e3pHehl502Kew480x360&rs=1&pid=ImgDetMain",
            "https://el-cubanito.cuba-cafe.com/public/media/el-cubanito/photo-1.jpg",
            "https://tinyurl.com/uvfy2ajs",
            "https://tinyurl.com/29wwt2y9"]
menu = ["grilled cheese", "pizza" , "hotdogs", "pupusas", "friedrice" , "FriedChicken" , "cubansandwich" ,
        "wings" , "medeterrainianbread"]
address = ["6544 W Archer Ave, Chicago, IL 60638, United States", "1707 W Division St, Chicago, IL 60622",
        "520 W. Taylor St., Chicago, IL 60607" , "6533 W 63rd St, Chicago, IL 60638" ,
        "2138 S ARCHER AVE CHICAGO, IL 60616" , "5412 W Madison St, Chicago, IL 60644-4029",
        "2555 N Pulaski Rd, Chicago, IL 60639" , "3350 W 47th St, Chicago, IL 60632" ,
        "2121 N Clark St, Chicago, IL 60614"]
fitlist = []

def open_image(url):    #opens the links
    response = requests.get(url) #HTTP Request
    img = Image.open(BytesIO(response.content)) #makes image an object
    img.show() #shows in window

def kind_of(k):  #gives a resturant based on the kind of food
    for i in range(len(menu)):
        if k in menu[i]:
            fitlist.append(restaurants[i])
    print(fitlist)
    fitlist.clear()

def picture_of(p):   #Shows a picture of the resturant's food
     global food
     if p in restaurants:
          for i in range(len(restaurants)):
               food = restaurants.index(p)
     else:
          print("Sorry resturant is not in list. Try writing it exacly like the list.")
          return None
     print(restaurants[food])
     open_image(pics[food])

def address_of(a):   #this goes through the list of resturants and addresses in order to put out the address of a resturant
    for i in range(len(restaurants)):
        if a in restaurants[i]:
            fitlist.append(address[i])
    if a not in restaurants:
        print("Try spelling the name of the resturant as it is listed")
        return "no"
    print(fitlist)
    fitlist.clear()
    return "yes"




def resturantrec():  #main where all the codes are together in a program
    print("Welcome to resturant recommender! We have 9 resturant options to recommend!")
    while True:
        t = int(input("What would you like to do today? (enter a number)\n1. Get a reccomendation based on how youre feeling\n2. See a photo of some food\n3. Get the address of a resturant\n4. Have a resturant randomly generated\n5. Quit "))
        if t == 1:
            print(menu)
            kind_of(input("What kind of food are you in the mood for? "))
        if t == 2:
            print(restaurants)
            picture_of(input("Enter a restaurant to see a picture of the food on a menu. "))
        if t == 3:
            print(restaurants)
            while True:
                x = address_of(input("Which resturant would you like the address to? "))
                if x == "yes":
                    break
        if t == 4:
            print(random.choice(restaurants))
        if t == 5:
            break





resturantrec()
