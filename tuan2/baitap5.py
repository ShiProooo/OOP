r = 5
V = 4/3 *3.14 * r**3

total_book_price = (24.95 - ((24.95 *40)/100)) * 60
total_shipping_cost = 3 + (0.75 *59)
total_price = total_book_price + total_shipping_cost

cell_size = 4
horiz = ('+'+'-' * cell_size) * 2 + '+'
vert = ('|' + ' ' * cell_size) * 2 + '|'

for r in range (2):
    print(horiz)
    for c in range (4):
        print(vert)
print(horiz)
cell_size = 4
horiz = ('+'+'-' * cell_size) * 3 + '+'
vert = ('|' + ' ' * cell_size) * 3 + '|'

for r in range (3):
    print(horiz)
    for c in range (4):
        print(vert)
print(horiz)
print(f"tong so tien sach la: {total_price: .2f}")
print(f"the tich hinh cau la:{V: .2f}")