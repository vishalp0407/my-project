import os

print("**********Welcom to Silent Auction Program**********")
Auction_data = []


def name_Price(name, price):
    data = {}
    data["Name"] = name
    data["Price"] = price
    Auction_data.append(data)


def winner():
    local_price = 0
    for i in Auction_data:
        if i["Price"] > local_price:
            local_price = i["Price"]
        else:
            local_price
    print(f" the winner is {i['Name']}  with bid_price: {local_price}")


# Name=input("What is your name?: ")
# bid_price=int(input("What is you bid Price?: "))
# name_Price(name=Name,price=bid_price)
flag = False
while not flag:
    Name = input("What is your name?: ")
    bid_price = int(input("What is you bid Price?: "))
    name_Price(name=Name, price=bid_price)
    str1 = input("Are there any other bidders yes or no\n").lower()
    if str1 == 'no':
        flag = True
        winner()
    elif str == 'yes':
        os.system('cls')

# print(Auction_data)