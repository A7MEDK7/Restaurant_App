# Restaurant Program --> A7MED

available_items = {
    "pizzas": {"Margherita": 100, "Pepperoni": 120,  "Meat Lovers": 150, "Chicken": 130},
    "burgers": {"Beef": 100, "Chicken": 80, "Bacon": 120},
    "drinks": {"Coke": 30, "Sprite": 25, "Fanta": 25, "Pepsi": 30},
    "soups": {"Chicken Soup": 50, "Beef Soup": 60,  "Mushroom Soup": 40},
    "desserts": {"Ice Cream": 50, "Chocolate Cake": 60,  "Cheese Cake": 70}
}

dict_order = {}
user_total = []

# Display the menu
print("Welcome to A7K Restaurant")
while True :
  print("-"*30)
  print("Our Menu : ")
  for index,type in enumerate(available_items,1) :
    print(f"{index}. {type}")
  print("6. View Your Order")
  print("7. Exit")
  # Get the user's choice
  user_choice = int(input("Choice a number of the item you want : "))
  print("-"*30)

  # Check the user's choice
  match(user_choice) :

    case 1 :
      while True :
        # Display the menu
        print("Our Pizzas : ")
        for index,(item,price) in enumerate(available_items["pizzas"].items(),1) :
          print(f"{index}. {item} : {price}")
        print("-"*30)
        user_input = int(input("Choice a number of the item you want :\n(press 0 to return to the previous menu) " ))
        # Check the user's choice , if the user press 0 return to the previous menu
        if user_input == 0 : 
          break
        # Make Sure the user enter a number between 1 and 4
        elif user_input not in [1,2,3,4] :
          # if the user enter a number not in the range , display an error message 
          print("Please enter a valid number")
          print("-"*30)
          continue
        else :
          # Get the item`s quantity 
          quantity = int(input("Enter the quantity : "))
          # Make Sure the user enter a quantity greater than 0
          if quantity <= 0 :
            print("Please enter a valid quantity")
            print("-"*30)
            continue
          else :  
            print("-"*30)
            # Get the item`s name,price from the dictionary
            price = available_items["pizzas"].get(list(available_items["pizzas"].keys())[user_input-1])
            item = list(available_items["pizzas"].keys())[user_input-1]
            total_pricee = price * quantity
            # Add the item`s price to the total price list
            user_total.append(total_pricee)
            # Add the item to the new dictionary 
            user_order = {
              "Pizza name" : item ,
              "Pizza price" : price ,
              "Quantity" : quantity ,
            }
            # update the order dictionary to add the new item 
            dict_order.update({len(dict_order)+1 : user_order})
            print("Item added successfully")
            print("-"*30)
            continue


    case 2 :
      while True :
        # Display the menu
        print("Our Burgers : ")
        for index,(item,price) in enumerate(available_items["burgers"].items(),1) :
          print(f"{index}. {item} : {price}")
        print("-"*30)
        user_input = int(input("Choice a number of the item you want :\n(press 0 to return to the previous menu) " ))
        # Check the user's choice , if the user press 0 return to the previous menu
        if user_input == 0 : 
          break
        # Make Sure the user enter a number between 1 and 3 
        elif user_input not in [1,2,3] :
          # if the user enter a number not in the range , display an error message 
          print("Please enter a valid number")
          print("-"*30)
          continue
        else :
          # Get the item`s quantity 
          quantity = int(input("Enter the quantity : "))
          # Make Sure the user enter a quantity greater than 0
          if quantity <= 0 :
            print("Please enter a valid quantity")
            print("-"*30)
            continue
          else :  
            print("-"*30)
            # Get the item`s name,price from the dictionary
            price = available_items["burgers"].get(list(available_items["burgers"].keys())[user_input-1])
            item = list(available_items["burgers"].keys())[user_input-1]
            total_pricee = price * quantity
            # Add the item`s price to the total price list
            user_total.append(total_pricee)
            # Add the item to the new dictionary 
            user_order = {
              "burgers name" : item ,
              "burgers price" : price ,
              "Quantity" : quantity ,
            }
            # update the order dictionary to add the new item
            dict_order.update({len(dict_order)+1 : user_order})
            print("Item added successfully")
            print("-"*30)
            continue
    
    case 3 :
      while True :
        print("Our Drinks : ")    
        # Display the menu
        for index,(item,price) in enumerate(available_items["drinks"].items(),1) :
          print(f"{index}. {item} : {price}")
        print("-"*30)
        user_input = int(input("Choice a number of the item you want :\n(press 0 to return to the previous menu) " ))
        # Check the user's choice , if the user press 0 return to the previous menu
        if user_input == 0 : 
          break
        # Make Sure the user enter a number between 1 and 4
        elif user_input not in [1,2,3,4] :
        # if the user enter a number not in the range , display an error message 
          print("Please enter a valid number")
          print("-"*30)
          continue
        else :
          # Get the item`s quantity 
          quantity = int(input("Enter the quantity : "))
          # Make Sure the user enter a quantity greater than 0
          if quantity <= 0 :
            print("Please enter a valid quantity")
            print("-"*30)
            continue
          else :   
            print("-"*30)
            # Get the item`s name,price from the dictionary
            price = available_items["drinks"].get(list(available_items["drinks"].keys())[user_input-1])
            item = list(available_items["drinks"].keys())[user_input-1]
            total_pricee = price * quantity
            # Add the item`s price to the total price list
            user_total.append(total_pricee)
            # Add the item to the new dictionary 
            user_order = {
              "drink name" : item ,
              "drink price" : price ,
              "Quantity" : quantity ,
            }
            # update the order dictionary to add the new item
            dict_order.update({len(dict_order)+1 : user_order})
            print("Item added successfully")
            print("-"*30)
            continue

    case 4 :
      while True :
        # Display the menu
        print("Our Soups : ")
        for index,(item,price) in enumerate(available_items["soups"].items(),1) :
          print(f"{index}. {item} : {price}")
        print("-"*30)
        user_input = int(input("Choice a number of the item you want :\n(press 0 to return to the previous menu) " ))
        # Check the user's choice , if the user press 0 return to the previous menu
        if user_input == 0 : 
          break
        # Make Sure the user enter a number between 1 and 3
        elif user_input not in [1,2,3] :
          # if the user enter a number not in the range , display an error message 
          print("Please enter a valid number")
          print("-"*30)
          continue
        else :
          # Get the item`s quantity 
          quantity = int(input("Enter the quantity : "))
          # Make Sure the user enter a quantity greater than 0
          if quantity <= 0 :
            print("Please enter a valid quantity")
            print("-"*30)
            continue
          else :  
            print("-"*30)
            # Get the item`s name,price from the dictionary
            price = available_items["soups"].get(list(available_items["soups"].keys())[user_input-1])
            item = list(available_items["soups"].keys())[user_input-1]
            total_pricee = price * quantity
            # Add the item`s price to the total price list
            user_total.append(total_pricee)
            # Add the item to the new dictionary 
            user_order = {
              "soup name" : item ,
              "soup price" : price ,
              "Quantity" : quantity ,
            }
            # update the order dictionary to add the new item
            dict_order.update({len(dict_order)+1 : user_order})
            print("Item added successfully")
            print("-"*30)
            continue

    case 5 :
      while True :
        # Display the menu
        print("Our Desserts : ")
        for index,(item,price) in enumerate(available_items["desserts"].items(),1) :
          print(f"{index}. {item} : {price}")
        print("-"*30)
        user_input = int(input("Choice a number of the item you want :\n(press 0 to return to the previous menu) " ))
        # Check the user's choice , if the user press 0 return to the previous menu
        if user_input == 0 : 
          break
        # Make Sure the user enter a number between 1 and 3
        elif user_input not in [1,2,3] :
          # if the user enter a number not in the range , display an error message 
          print("Please enter a valid number")
          print("-"*30)
          continue
        else :
          # Get the item`s quantity 
          quantity = int(input("Enter the quantity : "))
          # Make Sure the user enter a quantity greater than 0
          if quantity <= 0 :
            print("Please enter a valid quantity")
            print("-"*30)
            continue
          else :  
            print("-"*30)
            # Get the item`s name,price from the dictionary
            price = available_items["desserts"].get(list(available_items["desserts"].keys())[user_input-1])
            item = list(available_items["desserts"].keys())[user_input-1]
            total_pricee = price * quantity
            # Add the item`s price to the total price list
            user_total.append(total_pricee)
            # Add the item to the new dictionary 
            user_order = {
              "dessert name" : item ,
              "dessert price" : price ,
              "Quantity" : quantity ,
            }
            # update the order dictionary to add the new item
            dict_order.update({len(dict_order)+1 : user_order})
            print("Item added successfully")
            print("-"*30)
            continue

    case 6 :
      # Check if the user has ordered anything
      if len(dict_order) == 0 :
        # if the user has not ordered anything , display The Following message and Exit 
        print("Your Order is Empty")
        # Make Sure To end the Program When The User Press --> 2. No,Finish
        select = int(input(f"Do you want to order again ?\n1. Yes\n2. No,Finish\n---> "))
        # if user press 1 , continue the program and Dispaly The Menu
        if select == 1 :
          continue
        # if user press 2 , break the program and Exit  
        else :
          print("Thank you for choosing A7K Restaurant")
          break
      else :
        print("Your Order : ")
        print("-"*20)
        # Display The Index Of The Order
        for index in dict_order :
          # Dispaly the Order by name,pirce and quantity
          for key,value in dict_order[index].items():
            print(f"{key} : {value}")
          print("-"*20)
        # Display The Total Price by Using sum() Function in user_total List  
        print(f"Your Total Order : {sum(user_total)}")
        print("-"*20)
        # Make Sure To end the Program When The User Press --> 2. No,Finish
        select = int(input(f"Do you want to order again ?\n1. Yes\n2. No,Finish\n---> "))
        # if user press 1 , continue the program and Dispaly The Menu
        if select == 1 :
          continue
        # if user press 2 , break the program and Exit  
        else :
          print("Thank you for choosing A7K Restaurant")
          break

    case 7 :
      # Check if the user has ordered anything
      if len(dict_order) == 0 :
        # if the user has not ordered anything , display The Following message and Exit 
        print("Your Order is Empty")
      else :  
        # if the user has ordered anything , display His Order
        for index in dict_order :
          for key,value in dict_order[index].items():
            print(f"{key} : {value}")
          print("-"*20)
        print(f"Your Total Order : {sum(user_total)}")
        print("-"*20)
      print("Thank you for choosing A7K Restaurant")
      break
