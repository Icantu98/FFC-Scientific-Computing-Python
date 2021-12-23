class Category:

    def __init__(self, category):
        self.name = category
        self.ledger = [] # Keeps ledger of stuff spend money on 
    
    def deposit(self, cash, desc = ''):
        # adds item to ledger above 
        self.ledger.append({'amount':cash, 'description':desc})

    def check_funds(self, cash):
        funds = 0   # Golabal funds set
        # Checks to see if at least this amount is in the balance/account
        for item in self.ledger:
            funds = funds + item['amount']
        if cash>funds:
            return False
        return True

    def withdraw (self, cash, desc = ''):
        # adding a negative number to ledger
        if self.check_funds(cash):
            self.ledger.append({'amount':-cash, 'description':desc}) # NOTICE '-amount' not 'amount'
            return True
        return False

    def transfer(self, cash, newledger):
        if self.withdraw(cash, "Transfer to "+newledger.name):
            newledger.deposit(cash, "Transfer from "+self.name)
            return True
        return False

    def get_balance(self):
        balance = 0 # Golbal balance set
        # Outputs current balance
        for item in self.ledger: # Looops through ledger to update
            balance = balance + item['amount'] # NOTICE a = a + 5 == a +=5 
        return balance

    def get_withdrawals(self):
        withdrawls = 0 # Golabl withdrawls set
        # Outputs all withdrawls done
        for item in self.ledger:
            if item['amount']<0:
                withdrawls = withdrawls -item['amount']
        return withdrawls
    
    def __str__(self): # returns the Table : title, list, total
        n = '\n'
        title = self.name.center(30,'*') + n # Centers title of category in '*'
        lisT = ''
        for item in self.ledger:
        # docs.python.org/2/library/string.html#format-examples
            lisT += '{:<23}'.format(item['description'])[:23]
            t = '{:.2f}'.format(item['amount'])
            t = '{:>7}'.format(t)[:7]
            lisT += t +  n
        total = 'Total: ' + str(self.get_balance())
        return title + lisT + total
    
def create_spend_chart(categories):
    # Outputs bar chart
    n = '\n'
    title = 'Percentage spent by category' + n

    sums = {}    # sums for each Category
    all_sums = 0 # sums of all Categories
    longest_name = 0 #
    for category in categories:
        if not category.name in sums:
            sums[category.name] = 0
        withdrawls = category.get_withdrawals()
        sums[category.name] = sums[category.name] + withdrawls
        if len(category.name)>longest_name:
            longest_name = len(category.name)
        all_sums = all_sums + withdrawls

    percentage = {}
    tuples = sums.items()
    for k,v in tuples:
        percentage[k] = int(v/all_sums * 10) *10
    
    lisT = ''
    for i in range(100,-10,-10):
        lisT = lisT + "{:>3}".format(str(i))+'| '
        for k,v in percentage.items():
            if i <= v:
                lisT = lisT + 'o  '
            else:
                lisT = lisT + '   '
        lisT = lisT + n
    
    seperate = ('    {:->'+str(4+2*len(categories))+'}').format('') + n

    legend = ''
    for i in range(longest_name):
        legend = legend + '   '
        for category in categories:
            if i < len(category.name):
                legend = legend + '  ' + category.name[i]
            else: 
                legend = legend + '   '
        legend = legend + '  ' + n
    return title + lisT + seperate + legend.rstrip() + '  '
