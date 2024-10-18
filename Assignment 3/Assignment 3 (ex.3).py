class Item:
    def __init__(self, barcode, name, price):
        self.barcode = barcode
        self.name = name
        self.price = price

inventory = {
    "111": Item("123", "cheese", 1.3),
    "222": Item("456", "rice", 2.6),
    "333": Item("789", "oil", 3.9),
    "444": Item("789", "flour", 4.0),
    "555": Item("789", "noura", 6.0)
}
    

def add_item_to_receipt(receipt, barcode, quantity):
    if barcode in inventory:
        item = inventory[barcode]
        total_cost = item.price * quantity
        receipt.append((item.name, quantity, item.price, total_cost))
    else:
        print("Item not found in inventory.")

def display_receipt(receipt):
    print("... Receipt ...")
    total_amount = 0
    for name, quantity, price, total_cost in receipt:
        print(f"{name}: {quantity} x ${price:.2f} = ${total_cost:.2f}")
        total_amount += total_cost
    print(f"Total Amount: ${total_amount:.2f}")
    print("....................")

def process_receipt():
    receipt = []
    while True:
        barcode = input("Enter item barcode: ")
        quantity = int(input("Enter quantity: "))
        add_item_to_receipt(receipt, barcode, quantity)

        another_item = input("Would you like to add another item? (yes/no): ").strip().lower()
        if another_item != "yes":
            break

    display_receipt(receipt)

def main():
    while True:
        start_receipt = input("Would you like to start a new receipt? (yes/no): ").strip().lower()
        if start_receipt == "yes":
            process_receipt()
        else:
            print("Exiting the POS system.")
            break

if __name__ == "__main__":
    main()