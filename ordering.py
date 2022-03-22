from order import Order
from menu import Item


def get_items_dict():
    continues = True
    temp = []
    while continues:
        item_id = int(input('Enter id what you want : '))
        item_count = int(input('Enter count of your choose : '))
        result = {
            'item_id': item_id,
            'item_count': item_count
        }
        temp.append(result)
        print('Do you want more orders >?(Y/N) ')
        if input().lower() == 'n':
            continues = False
            print('Ok!! your items saved successfully!!!')
        else:
            continue
    return temp


def show_items_list():
    print('first : Our starters are :')
    for item in Item.Starter_list:
        print(f'* id : {item.item_id} , name : {item.name} , price : {item.price} ')

    print('first : Our foods are :')
    for item in Item.Food_list:
        print(f'* id : {item.item_id} , name : {item.name} , price : {item.price} ')

    print('first : Our beverages are :')
    for item in Item.Beverage_list:
        print(f'* id : {item.item_id} , name : {item.name} , price : {item.price} ')

    print('* #' * 30)


def pay_order():
    print("ok!! now you want to pay your order ... please enter your table number : ")
    number_table = int(input())
    bill = None
    for order in Order.order_list:
        if int(order.table.number) == number_table:
            bill = order.bill
    print('*' * 50)
    print(f'Here is details of your bill : \n'
          f'The money you should pay is : {bill.total_price}\n'
          f'The status of your payment is : {bill.payment.is_paid}\n'
          f'The type of your payment is : {bill.payment.payment_type}')
    print('#' * 50)
    if input('Ok ! Do you want to pay it ?(y)').lower() == 'y':
        bill.payment.is_paid = True
    print('Thanks for your paying ....')


def get_order():
    continues = True
    while continues:
        print('ok! lets create another order .....')
        print('*' * 80)
        print('Here is list of items you can select : ')
        show_items_list()
        print('So what do you want to eat ? ')
        selected_items = get_items_dict()
        order = Order.create_order(selected_items)
        print('Your order created successfully !! ')
        print('*' * 50)
        print('-' * 50)
        print('Please enter one item : \n'
              '1) Do you want to pay your order ?'
              '2) Do you want to create another order ?')
        if int(input()) == 2:
            continue
        else:
            pay_order()


def intro():
    print('Wellcome to our restuarant...')
    print('#' * 80)
    print('Please choose one item :')
    print('1) Are you admin ? \n2) Do you want to create an order ?')
    if int(input('your choose ?')) == 1:
        pass
    else:
        get_order()
