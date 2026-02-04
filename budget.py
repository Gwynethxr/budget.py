class Category:
    def __init__(self,name):
        pass
        self.name = name
        self.ledger =[]
        self.balance = 0
    def deposit(self,amount,description=""):
        self.ledger.append({
            'amount':amount,
            'description':description
        })
        


    def get_balance(self):
        return sum(i['amount'] for i in self.ledger)

    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            pass
            self.ledger.append({
                'amount':-amount,
                'description':description
            })
            self.balance = self.get_balance()
            
            return True
        else:
            return False
    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.withdraw(amount,f"Transfer to {category.name}")
            category.deposit(amount,f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self,amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        pass
        title = self.name.center(30,"*")
        # body = "\n".join([desc['description'] for desc in self.ledger])
        # price = "\n".join(str(year['amount']) for year in self.ledger)
        descrip = ""
        for item in self.ledger:
            text ='initial'
            descrip += f"{item['description'][:23]:<23}{item['amount']:7.2f}\n"
        return f"{title}\n{descrip}Total:{self.balance}"
def create_spend_chart(categories):
    
    title_chart = "Percentage spent by Category\n"
    spending = [] # store category spending and name
    total_spending = 0 #to store spending total
    percentage = [] #store persentase dari total
    #find total spending and category spending and name
    for category in categories:
        category_spending = 0
        # print(category.ledger)
        for item in category.ledger:
            if item['amount'] < 0 :
                # print(item['amount'])
                category_spending -= item['amount']
                total_spending -= item['amount']
                spending.append((category_spending,category.name)) 
            
    # print(title_chart,spending,total_spending)
    
    for p in spending:
        new_p = p[0] / total_spending
        rounded = int(new_p*10) * 10
        percentage.append({"Percentage":(rounded),'Category':p[1]})
    # print(spending,"\n\n",percentage)
    chart = ''
    chart += title_chart
    print(chart)
    for i in range(100,-1,-10):
        line = f"{i:>3}|"
        for p in percentage:
            if i <= p['Percentage']:
                line += " o "
            else:
                line += "   "
        line +="\n"
        chart += line
    chart += "    " + "-" *(len(categories)* 3 + 1) + "\n"
    print(chart)

    length = 0
    for category in categories:
        if len(category.name) > length:
            length = len(category.name)
        print(category.name)
    for i in range(length):
        pass
        line = "     "
        print(i)
        for c in categories:
            if i < len(c.name):
                line += c.name[i] + "  "
            else:
                line += "   "
        chart += line.rstrip() + " \n"
    chart = chart.rstrip()
    print(chart)
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(250, 'groceries')

# print(food.ledger)

clothing = Category('Clothing')
clothing.deposit(500,"clothing")
clothing.withdraw(200,"clothing")

games = Category("Gaming")
games.deposit(1000,'deposit')
games.withdraw(500,'PS5')

travel = Category("Travel")
travel.deposit(650,'Deposit')
travel.withdraw(400,'Flight')
categories = [food,clothing,games,travel]

create_spend_chart(categories)

##percentage by category

##{100|:}