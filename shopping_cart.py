class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self.items.append({'item':name, 'price':price})
            self.total +=price
        return self.total
        
    def mean_item_price(self):
        item_count = len(self.items)
        return self.total/item_count

    def median_item_price(self):
        prices_list = []
        for i in list(range(len(self.items))):
            prices_list.append(self.items[i]['price'])
        sort_prices = sorted(prices_list)
        if len(prices_list)%2 == 0:
            med1 = sort_prices[int(len(prices_list)/2)]
            med2 = sort_prices[int(len(prices_list)/2) - 1]
            return (med1 + med2)/2
        else:
            return sort_prices[int(len(prices_list)/2)]

    def apply_discount(self):
        if self.employee_discount:
            return self.total*(1-(self.employee_discount/100))
        else:
            return 'Sorry, there is no discount to apply to your cart :('

    def void_last_item(self):
        if self.items:
            void_item = self.items.pop()
            self.total -= void_item['price']
            return self.total
        else:
            return "There are no items in your cart!"