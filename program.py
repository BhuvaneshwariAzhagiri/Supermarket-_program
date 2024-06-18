import smtplib
from datetime import datetime

def cooking_ingredients():
    product = {
        "sombu": 12, "cumin": 15, "mustard_seed": 13, "black_pepper": 85, 
        "venthayam": 35, "ulunthu": 190, "payir": 91, "rice": 1500, 
        "noodles": 12, "chicken masala": 10, "mutton masala": 10
    }
    row_name = "Cooking Ingredients"
    return row_name, product

def household_and_cleaning():
    product = {
        "paste": 20, "brush": 15, "soap": 35, "hand wash": 80, 
        "lizol": 100, "mop cleaner": 300, "vessel washing liquid": 30, 
        "shampoo": 40, "bottle": 40, "snacks box": 50, "surf excel": 100, 
        "harpic": 40, "mat": 60, "comfort": 30
    }
    row_name = "Household & Cleaning Products"
    return row_name, product

def snacks_items():
    product = {
        "dairy milk": 20, "marie gold": 10, "bourbon": 20, "oreo": 10, 
        "milk powder": 10, "kitkat": 10, "5star": 5, "snickers": 20, 
        "lays": 10, "nabati": 10, "chips": 20, "chachos chips": 20, 
        "chocolates": 25, "munch": 10
    }
    row_name = "Snacks Items"
    return row_name, product

def dairy_product():
    product = {
        "milk": 10, "butter": 50, "cheese": 80, "ice cream": 20, 
        "curd": 10, "ghee": 100, "ice pop": 25, "custard milk": 60, 
        "soft cheese": 100, "pudding": 70
    }
    row_name = "Dairy Products"
    return row_name, product

def beauty_product():
    product = {
        "fair&lovely": 20, "vico turmeric": 40, "vico w3x": 50, "vaseline": 50, 
        "body lotion": 60, "himalaya": 50, "sunscreen": 70
    }
    row_name = "Beauty Products"
    return row_name, product

def choose_items():
    sections = [
        cooking_ingredients(), household_and_cleaning(), snacks_items(), 
        dairy_product(), beauty_product()
    ]
    selected_items = []
    total_bill = 0

    for row_name, product in sections:
        items = {}
        print(f"Available {row_name.lower()} and their prices are below:")
        for name, price in product.items():
            print(f"{name}: ${price}")

        while True:
            item = input(f"Enter the product name you want from {row_name} (or type 'done'): ").lower()
            if item == 'done':
                break
            if item in product:
                try:
                    quantity = int(input(f"Enter the quantity for {item}: "))
                    items[item] = product[item] * quantity
                except ValueError:
                    print("Please enter a number for quantity.")
            else:
                print(f"Sorry, {item} is not available.")
        
        if items:
            selected_items.append((row_name, items))
            total_bill += sum(items.values())
    
    return selected_items, total_bill

def generate_bill(chosen_items, total_cost):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bill_content = f"Superarket Bill:\nDateandtime{current_datetime}\n\n"
    for section_name, section_items in chosen_items:
        bill_content += f"{section_name}:\n"
        for item, price in section_items.items():
            bill_content += f"  {item}: Rs.{price}\n"
    bill_content += f"\nTotal amount for all items: Rs.{total_cost}\n"
    
    with open("bill_sm.txt", "w") as f:
        f.write(bill_content)
    
    print("Bill generated and saved as 'bill_sm.txt'.")
    return bill_content

def send_email(bill_content):
    recipient_email = input("Please enter your Gmail ID: ")
    sender_email = "bhuvaneshwarial48@gmail.com"
    sender_password = "your_password"
    
    subject = "Super Market Bill"
    body = bill_content
    email_text = f"Subject: {subject}\n\n{body}"
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, email_text)
        server.quit()
        print("Email sent successfully!")
    except:
        print(f"Mail failed....")

def main():
    chosen_items, total_cost = choose_items()
    bill_content = generate_bill(chosen_items, total_cost)
    send_email(bill_content)
main()