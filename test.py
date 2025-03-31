def print_welcome(name: str, width: int=20):
    print(f'{"Hello, " + name + "!":^{width}}')

def print_shop_menu(item1Name:str, item1Price:float, item2Name:str, item2Price:float):
    price1_str = str(f"{item1Price:.2f}")
    price2_str = str(f"{item2Price:.2f}")
    print('/' + '-'*22 + '\\')
    print(f'| {item1Name:<12}{"$" + price1_str:>8} |')
    print(f'| {item2Name:<12}{"$" + price2_str:>8} |')
    print('\\' + '-' * 22 + '/')
    return "\n"


print_welcome("Catelyn")
print()
print_shop_menu("Wheat", 16.50, "Bread", 5.00)
print()
