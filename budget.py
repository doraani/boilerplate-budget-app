import math
class Category:
    def display_category(self):
        # 30 * characters with self.category centered
        # self.category.length / 2 should be 15th character
        display_text = ''
        line_len = 30
        half_line = round(line_len/2 - len(self.category) / 2)
        for i in range(0,half_line):
            display_text += '*'
        display_text += self.category
        for i in range(half_line + len(self.category), line_len):
            display_text += '*'
        return display_text + '\n'
    def __init__(self, category):
        self.ledger = []
        self.category = category
    def __repr__(self):
        return Category()
    def __str__(self):
        text = self.display_category()
        for i in self.ledger:
            text += i['description'][0:23].ljust(23)
            amount_str = "{:.2f}".format(i['amount'],2)[0:7]
            text += amount_str.rjust(7) + '\n'
        text += 'Total: ' + '{:.2f}'.format(self.get_balance(),2)
        return text
    def get_balance(self):
        # return sum of deposit and withdraw amount
        sum = 0
        for x in self.ledger:
            sum += x['amount']
        return sum
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else: return True
    def deposit(self, amount, description=''):
        self.ledger.append({'amount':amount, 'description':description})
    def withdraw(self, amount, description=''):
        # should use check_funds
        enough_founds = self.check_funds(amount)
        if enough_founds:
            self.ledger.append({'amount':-amount, 'description':description})
            return True
        else:
            return False
    def transfer(self, amount, transfer_target):
        # should use check_funds
        description = 'Transfer to %s' % transfer_target.category
        succesful_transfer = self.withdraw(amount,description)
        if succesful_transfer:
            description = 'Transfer from %s' % self.category
            transfer_target.deposit(amount,description)
        return succesful_transfer

def create_spend_chart(categories):
    chart = 'Percentage spent by category\n'
    line = '---' * len(categories) + '-'
    percentages = []
    for category in categories:
        spend = 0
        count = 0
        for withdraw in category.ledger:
            if withdraw["amount"] < 0:
                spend += withdraw["amount"]
                count += 1
        percentages.append(spend)
    # get the percentages first digit for printing the chart
    total = sum(percentages)
    for i in range(0,len(percentages)):
        percentages[i] = math.floor(percentages[i] / total*10)
    # draw chart
    for i in range(10,-1,-1):
        if i < 10 : # 90 to 0
            chart += ' '
        if i == 0: # extra space on 0
            chart += ' '
        chart += str(i)
        if i == 0: # single 0
            chart += '| '
        else:
            chart += '0| '
        for percentage in percentages:
            if percentage >= i:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'
    chart += '    '+ line + '\n'
    # get the longest category name
    longest_category_name = categories[0].category
    for category in categories:
        if len(category.category) > len(longest_category_name):
            longest_category_name = category.category
    # categories wrote down vertically
    chart += '     '
    for j in range(0 ,len(longest_category_name)):
        for category in categories:
            if j < len(category.category): # write a category character
                chart += category.category[j] + '  '    
            else: # 3 whitespaces when there is no category character to print
                chart += '   '
        if j < len(longest_category_name)-1: # do not print a new line after the last character
             chart += '\n     '
    return chart
