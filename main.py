def party_invoice():
    
    base_price = 100
    
    # input each addon as a string with the quantity and type
    # seperate each addon with a comma
    addons = input("What are the party addons?")
    print(addons_list)
    
    # use the "split" method to convert the addons to a list
    addons_list = addons.split(",")
    print(addons_list)
    
    for addon in addons_list:
        
        item = addon[-1]
        count = addon[:-1]
        print("item: ", item, "count: ", count)
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    party_invoice()
