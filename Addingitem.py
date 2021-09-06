import json

item_list={
    "1100":{"Name":"Pepsi","Expiry_date":"25/08/2027","Price":10,"Quantity":60,"Vegan":True},
    "1101":{"Name":"CocaCola","Expiry_date":"23/08/2027","Price":10,"Quantity":30,"Vegan":True},
    "1102":{"Name":"Lays","Expiry_date":"17/06/2027","Price":20,"Quantity":110,"Vegan":True},
    "1103":{"Name":"Perk","Expiry_date":"25/10/2027","Price":30,"Quantity":600,"Vegan":True},
    "1104":{"Name":"Cheese","Expiry_date":"31/08/27","Price":60,"Quantity":200,"Vegan":False},
    "1105":{"Name":"Cadberry","Expiry_date":"10/08/2026","Price":50,"Quantity":70,"Vegan":True},
    "1106":{"Name":"Dettol","Expiry_date":"07/08/2026","Price":30,"Quantity":700,"Vegan":True},
    "1107":{"Name":"Oreo","Expiry_date":"10/05/2026","Price":100,"Quantity":65,"Vegan":False}
}

num=int(input("Enter the no of products you wanna add\n"))
for i in range(num):
    prod_id1=input("Enter product ID : ")
    Name1=input("Enter Name : ")
    Expiry_date1=input("Enter Expiry_date : ")
    Price1=input("Enter Price : ")
    Quantity1=input("Enter Quantity : ")
    Vegan1=input("State True if its vegan and state False if it's not Vegan : ")
    item_list[prod_id1]={"Name":Name1,"Expiry_date":Expiry_date1,"Price":Price1,"Quantity":Quantity1,"Vegan":Vegan1}


temp1=json.dumps(item_list)



f=open("record.txt","w")
f.write(temp1)
f.close()

print("\nItems added in record.txt\n")




