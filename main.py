def party_invoice():
    
    base_price = 100
    
    # create a price dictionary
    price_dict = {
        
        #Key: value
        "H": 50,
        "S": 40,
        "Y": 35,
        "p": 10,
        "b": 2,
        "s": .50,
        "C": 15,
        "c": .25,
    }
    
    addons_dict = {
        
        #Key: value
        "H": "Bounce House",
        "S": "Slip & Slide",
        "Y": "Yard Sign",
        "p": "Pizza",
        "b": "Burgers",
        "s": "Soda",
        "C": "Cake",
        "c": "Cupcake",
    }
    
    # input each addon as a string with the quantity and type
    # seperate each addon with a comma
    addons = input("What are the party addons? ")
    print(addons)
    
    # use the "split" method to convert the addons to a list
    addons_list = addons.split(",")
    print(addons_list)
    
    for addon in addons_list:
        
        
        item = addon[-1]
        count = addon[:-1]
        
        item_name = addons_dict.get(item)
        print("item: ", item, "count: ", count)
        
        base_price += price_dict.get(item, 0) * count 
        
        items = item,count
        
        print(f"{base_price} is your total price faithful customer!")
        
    
    

    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    party_invoice()
