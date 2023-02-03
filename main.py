def party_invoice():
    
    base_price = 100
    
    # input each addon as a string with the quantity and type
    # seperate each addon with a comma
    addons = input("What are the party addons?")
    
    # use the "split" method to convert the addons to a list
    addons_list = addons.split(",")
    
    for addon in addons_list:
        
        item = addon[-1]
        count = addon[:-1]
        
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    party_invoice()
