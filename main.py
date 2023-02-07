def party_invoice():
    
    base_price = 100
    
    #create a price dictionary
    price_dict = {
        
        # Key: value,
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
        "H": "Bouncy House",
        "S": "Slip & Slide",
        "Y": "Yard Sign",
        "p": "Pizza",
        "b": "Burger",
        "s": "Soda",
        "C": "Cake",
        "c": "Cupcake",
    }
    
    # print("t john is cool and awsome")
    # input each addon as a string with the quantity and type
    # seperate each addon with a comma
    addons = input("What are the party addons? ")
    # print(addons)
    
    # use the "split" method to convert the addons to a list
    addons_list = addons.split(",")
    # print(addons_list)
    
    itemized_prices = "Thank you for being a faithful customer! We've found you've ordered the following:\n"
    
    for addon in addons_list:
        
        
        item = addon[-1]
        count = int(addon[:-1])
        price = price_dict.get(item, 0) * count
        item_name = addons_dict.get(item, 0)
        
        # print("item: ", item_name, "count: ", count)
        
        base_price += price
        
        itemized = f"\n{item_name}, {count} and ${'{:.2f}'.format(price)}"
        itemized_prices += itemized


    itemized_prices += "\n\nBase Price, $100.00"
    itemized_prices += f"\nTotal, ${base_price}"
    print(itemized_prices)   
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    party_invoice()
