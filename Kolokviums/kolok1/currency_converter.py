# def currency_converter():
#     amount = float(input("Enter amount in original currency: "))
#     course = float(input("Enter course of convertation: "))
#     converted_ammount = amount * course
#     print(f"converted amount: {converted_ammount}")

# currency_converter()

print('Welcome to CurrensyConverter, we convert USD, EUR and AZN')
your_money=int(input('Enter amount: '))
your_currency=input('Enter currency: ')
convert_to=input('Enter currency to convert to: ').upper()
if convert_to not in ['USD','EUR','GBP']:
    print('Invalid currency')
    exit()
if your_currency=='USD' and convert_to=='EUR':
    converted_money=your_money*0.85
elif your_currency=='EUR' and convert_to=='USD':
    converted_money=your_money*1.18
elif your_currency=='AZN' and convert_to=='USD':
    converted_money=your_money*0.59 
elif your_currency=='AZN' and convert_to=='EUR':
    converted_money=your_money*0.51
elif your_currency=='USD' and convert_to=='AZN':
    converted_money=your_money*1.69
elif your_currency=='EUR' and convert_to=='AZN':
    converted_money=your_money*1.96
else:
    converted_money=your_money

print(f'{your_money} {your_currency} is {converted_money} {convert_to}')