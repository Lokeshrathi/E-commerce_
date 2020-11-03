class Customer:
    #function to update the details of the customer
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.purchases = []
        
    #function to have a customer make a purchase
    def purchase(self,inventory, product):
        inventory_dict = inventory.inventory
        if product in inventory_dict:
            if inventory_dict[product] > 1:
                self.purchases.append(product)
                inventory_dict[product]-=1
            else:
                print('We are out of stock')
        else:
            print("We don't have the product")

    def print_purchases(self):
        print('The customer has purchased:')
        bill = 0
        for items in self.purchases:
            print(items.name + " $"+str(items.price))
            bill+=items.price
        print(customer.name +"'s Total Bill is $" + str(bill))
        
        

class Product:
    #function to add the name and price of the product
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self.inventory = {} #inventory is a Dictionary to hold the key and value of the product
    #funtion to add product to the inventory
    def add_product(self,product,quantity): 
        if product not in self.inventory:
            self.inventory[product] = quantity
        else:
            self.inventory[product]+=quantity 

    def print_inventory(self):
        print('Product: Quantity')
        for key,value in self.inventory.items():
            print(key.name + ": " + str(value))
        print()

customer = Customer('Joe Rogan','joe@gmail.com')
print('Name of the Customer: ')
print(customer.name)

apple_watch = Product('apple_watch',299)
mac = Product('mac',1999)
nike = Product('Nike',1500)
iphone = Product('IPhone',900)

inventory = Inventory()
inventory.add_product(apple_watch,500)
inventory.add_product(iphone,15)
inventory.add_product(mac,800)
inventory.add_product(nike,70)
print()
inventory.print_inventory()

#function to add the customers purchase
customer.purchase(inventory,apple_watch)
customer.purchase(inventory,iphone)
#printing the *Updated* inventory and the Customers purchase
inventory.print_inventory()
print()
customer.print_purchases()