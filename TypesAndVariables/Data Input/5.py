price = float(input('Enter the price: '));
discount = input('Enter the discount: ');
price_with_discount = price * (1 - discount / 100);
reduction = price - price_with_discount;
print(f'Price: {price} \n Discount: {discount} \nPrice with discount: {price_with_discount} \nReduction: {reduction}');
