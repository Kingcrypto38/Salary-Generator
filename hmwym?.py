print('Money Calculator')
y = float(input('How much money per hour? '))
numbers = []
while len(numbers) < 25:
    number = float(input('How many hours per day? '))
    if not 1 <= number <= 24:
        print('only numbers between 1 and 24 are acceptable')
    else:
        z = float(input('How many days per year? '))
        a = float(input('Taxes are how much percent of your income? '))
        answer = (a/100)
        result = (number * y * z)
        mpy = ('Dollars')
        print(result - answer * result, mpy)
        exit()
        
