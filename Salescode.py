import json

f= open("record.txt","r")
items=f.read()
f.close()

item_list=json.loads(items)


number_of_customers=int(input("Enter the no of Customers : \n"))

isitem_present=False

for i in range(number_of_customers):
    print("Available Items are the following.Please enter the name of a single item you wanna Buy\n")
    for j in item_list.keys():
        print(item_list[j]["Name"],end=" ")
    item_bought=input("\nEnter the Product name of the item : ")
    amount=int(input("Enter the quantity of that item you wanna buy : "))
    print("\n")
    for j in item_list.keys():
        if(item_list[j]["Name"]==item_bought):
            while(1):
                if(int(item_list[j]["Quantity"])<amount):
                    print(f"Entered amount is greater than current stock. Please enter a number less than or equal to {item_list[j]['Quantity']}\n")
                    amount=int(input())
                else:
                    item_list[j]["Quantity"]=int(item_list[j]["Quantity"])-amount
                    code1=j
                    temp2=f"Code = {j}, Name = {item_list[j]['Name']}, Expiry_Date = {item_list[j]['Expiry_date']}, Price = {item_list[j]['Price']}, Quantity of items sold = {amount},Vegan = {item_list[j]['Vegan']}\n "
                    isitem_present=True
                    break
            break
    if(isitem_present==False):
        print("No such Item present Enter another entry\n")  
    else:    

        

        wd=open("sales.txt","a")
        temp3=json.dumps(temp2)
        wd.write(temp3)
        wd.close()

        print("**************************************\n")
        print("Billing Amount : \n")
        print(f"Name of the item bought : {item_bought} \n Quantity Bought : {amount} \n Total Price : {amount*item_list[code1]['Price']} \n")
        print("**************************************")


        print("Items added in Sales.txt\n")
        isitem_present=False

        f=open("record.txt","w")
        temp4=json.dumps(item_list)
        f.write(temp4)
        f.close()