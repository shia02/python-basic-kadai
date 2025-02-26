def add_tax(price: int, tax: int):
    return price + price * (tax / 100)

tax_add_price = add_tax(110, 10)
print(tax_add_price)