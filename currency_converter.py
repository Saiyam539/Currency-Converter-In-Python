import datetime
class welcome:

    @staticmethod
    def greeting():
        print('''*****WELCOME TO THE SAIYAM'S CURRENCY CONVERTER*****\n''')
        name = input('Please enter your name here:-\n')
        hour = int(datetime.datetime.now().hour)
        if hour>0 and hour<=12:
            print(f'Good Morning {name}')
        elif hour>12 and hour<=17:
            print(f'Good Afternoon {name}')
        else:
            print(f'Good Evening {name}')
        
class currency_converter:

    @staticmethod
    def currency():
        amount = int(input('Enter the amount here:- '))

        convert_from = ''' Convert From:- 
        1. Indian rupee
        2. US dollor
        3.New Zealand dollar'''
        print(convert_from)
        input_of_from = int(input('Enter your choise here:- '))

        convert_to = '''Convert TO:- 
        1.Indian rupee
        2.US dollor
        3.New Zealand dollar'''
        print(convert_to)
        input_of_to = int(input('Enter your choise here:- '))

        if input_of_from==1 and input_of_to==2:
            print(f'The amount from Indian rupee to US dollar is {amount/73.21} USD')
        
        elif input_of_from==2 and input_of_to==1:
            print(f'The amount from US dollar to Indian rupee is {amount*73.21} rupee')
        
        elif input_of_from==1 and input_of_to==3:
            print(f'The amount from Indian rupee to New Zealand dollar is {amount/52.39} NZD')
        
        elif input_of_from==3 and input_of_to==1:
            print(f'The amount from New Zealand dollar to Indian rupee is {amount*52.39} rupee')
        
        elif input_of_from==2 and input_of_to==3:
            print(f'The amount from US dollar to New Zealand dollar is {amount*1.40} NZD')
        
        elif input_of_from==3 and input_of_to==2:
            print(f'The amount from NZD to USD is {amount/1.40} USD')

try:
    if __name__ == "__main__":

        welcome.greeting()

        while True:
            currency_converter.currency()

except Exception as e:
    print('Please enter a valid input.')