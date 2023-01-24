class Roi():  
    def __init__(self):
        self.income_list = {}
        self.expenses_list = {}
        self.t_income = None
        self.t_expenses = None
        self.investment = None
        self.roi = None

    def set_num(self):
        u_i = int(input("Investment: "))
        self.investment = u_i
        while True:
            print("Enter all the income sources one by one / 'done' when finished ")
            u_i1 = input("Name: ").lower().strip()
            if u_i1 != 'done':
                u_i2 = int(input("amount: "))
                self.income_list[u_i1] = u_i2
            elif u_i1 == 'done':
                break
        self.t_income = sum(self.income_list.values())
        while True:
            print(" Enter all the expenses one by one /Enter 'done' when finished ")
            u_i1 = input("Name: ").lower().strip()
            if u_i1 != 'done':
                u_i2 = int(input("amount: "))
                self.expenses_list[u_i1] = u_i2
            elif u_i1 == 'done':
                break
        self.t_expenses = sum(self.expenses_list.values())
        self.clc()

    def clc(self):
        cashflow = self.t_income - self.t_expenses
        self.roi = int((cashflow / self.investment)*12 * 100)

    def __repr__(self):
        return f"    {self.t_income}$       {self.t_expenses}$       {self.investment}$       {self.roi}%/year"



class User_data():
    def __init__(self):
        self.data = {}
    
    def add_user(self):
        u_i= input("Enter the user name: ").lower().strip()
        if u_i not in self.data:
            self.data[u_i] = {}
        else:
            print(f"{u_i} alrady exist")

    def del_user(self):
        u_i= input("Enter the user name: ").lower().strip()
        if u_i in self.data:
            del self.data[u_i]
        else:
            print(f"{u_i} dose not exist")

    def add_property(self, u_name):
        p_name = input("Property name: ").lower().strip()
        if p_name not in self.data[u_name]:
            self.data[u_name][p_name] = u_name+p_name
            self.data[u_name][p_name] = Roi()
        else:
            print(f"{p_name} alrady in your list")
    
    def manage_property(self, u_name):
        p_name = input("property id: ").lower().strip()
        if p_name not in self.data[u_name]:
            print(f"{p_name} not in your list")
        else:
            self.data[u_name][p_name].set_num()
    
    def print(self,u_name ,p = 'all'):
        if p == 'account':
            for i in self.data:
                print(i)
        elif p == 'property':
            for i, v in self.data[u_name].items():
                print(i, v)
        elif p == 'all':
            for i in self.data:
                print(str(i)+"    Income,    Expenses,    Investment,    ROI")
                print("------------------------------------------------------")
                for j, v in self.data[i].items():
                    print(j, v)
                print()
        elif p == 'd':
            u_i = input("property name: ")
            if u_i in self.data[u_name]:
                print('Income', self.data[u_name][u_i].income_list)
                print('Expenses',self.data[u_name][u_i].expenses_list)
            else:
                print("{u_i} not found")
                
    def acount_acess(self, name):
        if name in self.data:
            return name
        else:
            print(f"{name} dose not exist")

    def run(self):
        while True:
            u_i = input(
""" 
Enter option number
[1] Manage accounts
[2] Acount login
[3] Print full list 
[4] Exit
""").lower().strip()
            if u_i == '1':
                while True:
                    u_i = input(
    """ 
    Enter option number:
    [1] Add account
    [2] Del account
    [3] Print accounts list 
    [4] Back to main menu
    """).lower().strip()
                    if u_i == '1':
                        self.add_user()
                    elif u_i == '2':
                        self.del_user()
                    elif u_i == '3':
                        self.print(None, 'account')
                    elif u_i == '4':
                        break
                    else:
                        print("invalid")
            elif u_i == '2':
                while True:
                    u_i = input(
    """ 
    Enter option number:
        Enter user name 
    [2] Back to main menu
    """).lower().strip()        
                    if u_i == '2':
                        break
                    else:
                        username = u_i
                        self.acount_acess(username)
                        while True:
                            u_i = input(
    """ 
    Enter option number:
    [1] Add property
    [2] Manage property
    [3] print 
    [4] Print list of property
    [5] Back
    """).lower().strip()   
                            if u_i == '1':
                                self.add_property(username)
                            elif u_i == '2':
                                self.manage_property(username)
                            elif u_i == '3':
                                self.print(username, 'd')
                            elif u_i == '4':
                                self.print(username, 'property')
                            elif u_i == '5':
                                break
                            else:
                                print("invalid")
            elif u_i == '3':
                self.print(None)
            elif u_i == '4':
                break
            else:
                print("invalid")

user = User_data()
user.run()
