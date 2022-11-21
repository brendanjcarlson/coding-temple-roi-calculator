import time


class Owner:
    def __init__(self, name):
        self.name = name
        self.properties = []

    @classmethod
    def create(cls):
        error = f"\nTry entering a number.\n"
        user_name = input("Your name: ").title()
        new_owner = cls(user_name)
        return new_owner

    def add_property(self, prop):
        self.properties.append(prop)

    @property
    def monthly_cash_flow(self):
        return self.monthly_income - self.monthly_expenses

    @property
    def annual_cash_flow(self):
        return self.monthly_cash_flow * 12

    @property
    def monthly_income(self):
        return sum([prop.monthly_income for prop in self.properties])

    @property
    def annual_income(self):
        return self.monthly_income * 12

    @property
    def monthly_expenses(self):
        return sum([prop.monthly_expenses for prop in self.properties])

    @property
    def annual_expenses(self):
        return self.monthly_expenses * 12

    @property
    def total_investment(self):
        return sum([prop.initial_investment for prop in self.properties])

    @property
    def annual_return_on_investment(self):
        return f"{self.annual_cash_flow / self.total_investment * 100}%"


class Property:
    def __init__(self, name, total_cost, down_payment, closing_costs, initial_repairs, mortgage):
        self.name = name
        self.total_cost = total_cost
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.initial_repairs = initial_repairs
        self.mortgage = mortgage
        self.units = []

    @classmethod
    def create(cls):
        error = f"\nTry entering a number.\n"
        user_name = input("Property name: ")
        while True:
            user_cost = input("Property cost: $")
            try:
                user_cost = int(user_cost)
                break
            except:
                print(error)
        while True:
            user_down = input("Down payment: $")
            try:
                user_down = int(user_down)
                break
            except:
                print(error)
        while True:
            user_closing = input("Closing costs: $")
            try:
                user_closing = int(user_closing)
                break
            except:
                print(error)
        while True:
            user_repairs = input("Initial repairs cost: $")
            try:
                user_repairs = int(user_repairs)
                break
            except:
                print(error)
        while True:
            user_mortgage = input("Monthly mortgage payment: $")
            try:
                user_mortgage = int(user_mortgage)
                break
            except:
                print(error)
        new_property = cls(user_name, user_cost, user_down, user_closing,
                           user_repairs, user_mortgage)
        return new_property

    def add_unit(self, unit, num=1):
        for _ in range(num):
            self.units.append(unit)

    @property
    def initial_investment(self):
        return self.down_payment + self.closing_costs + self.initial_repairs

    @property
    def monthly_cash_flow(self):
        return self.monthly_income - self.monthly_expenses

    @property
    def annual_cash_flow(self):
        return self.monthly_cash_flow * 12

    @property
    def monthly_income(self):
        return sum([unit.monthly_income for unit in self.units])

    @property
    def annual_income(self):
        return self.monthly_income * 12

    @property
    def monthly_expenses(self):
        return sum([unit.monthly_expenses for unit in self.units]) + self.mortgage

    @property
    def annual_expenses(self):
        return self.monthly_expenses * 12


class Unit:
    VACANCY_RATE = .05
    REPAIRS_RATE = .05
    TAX_RATE = .05
    INSURANCE_RATE = .075
    CAPITAL_EXP_RATE = .05
    PROP_MGMT_RATE = .05

    def __init__(self, name, rent, covered_parking=0, laundry=0, storage=0, misc=0, hoa_dues=0, water=0, electric=0, sewer=0, garbage=0, groundskeeping=0):
        # incomes
        self.name = name
        self.rent = rent
        self.covered_parking = covered_parking
        self.laundry = laundry
        self.storage = storage
        self.misc = misc
        # expenses
        self.hoa_dues = hoa_dues
        # optional expenses
        self.water = water
        self.electric = electric
        self.sewer = sewer
        self.garbage = garbage
        self.groundskeeping = groundskeeping
        # calculated expenses
        self.vacancy = rent * self.VACANCY_RATE
        self.taxes = rent * self.TAX_RATE
        self.insurance = rent * self.INSURANCE_RATE
        self.capital_exp = rent * self.CAPITAL_EXP_RATE
        self.prop_mgmt = rent * self.PROP_MGMT_RATE

    @classmethod
    def create(cls):
        error = f"\nTry entering a number.\n"
        user_name = input("Floorplan name: ")
        while True:
            user_rent = input("Monthly rent: $")
            try:
                user_rent = int(user_rent)
                break
            except:
                print(error)
        while True:
            user_covered_parking = input("Covered parking fee: $")
            try:
                user_covered_parking = int(user_covered_parking)
                break
            except:
                print(error)
        while True:
            user_laundry = input("Expected income from laundry services: $")
            try:
                user_laundry = int(user_laundry)
                break
            except:
                print(error)
        while True:
            user_storage = input("Expected income from storage services: $")
            try:
                user_storage = int(user_storage)
                break
            except:
                print(error)
        while True:
            user_misc = input("Expected income from other services: $")
            try:
                user_misc = int(user_misc)
                break
            except:
                print(error)
        while True:
            user_hoa_dues = input("Expected cost of HOA dues per month: $")
            try:
                user_hoa_dues = int(user_hoa_dues)
                break
            except:
                print(error)
        while True:
            user_options = ['y', 'yes', 'n', 'no']
            user_tenant_utils = input(
                "\nWill the tenant be paying for utilities? (Y)es | (N)o\n").lower()
            if user_tenant_utils not in user_options:
                print(f"{user_tenant_utils} is not a valid input.")
            elif user_tenant_utils == 'y' or user_tenant_utils == 'yes':
                new_unit = cls(name=user_name, rent=user_rent, laundry=user_laundry,
                               storage=user_storage, misc=user_misc, hoa_dues=user_hoa_dues)
                return new_unit
            elif user_tenant_utils == 'n' or user_tenant_utils == 'no':
                while True:
                    user_water = input("Expected cost of water per month: $")
                    try:
                        user_water = int(user_water)
                        break
                    except:
                        print(error)
                while True:
                    user_electric = input(
                        "Expected cost of electricity per month: $")
                    try:
                        user_electric = int(user_electric)
                        break
                    except:
                        print(error)
                while True:
                    user_sewer = input(
                        "Expected cost of sewer services per month: $")
                    try:
                        user_sewer = int(user_sewer)
                        break
                    except:
                        print(error)
                while True:
                    user_garbage = input(
                        "Expected cost of garbage services per month: $")
                    try:
                        user_garbage = int(user_garbage)
                        break
                    except:
                        print(error)
                while True:
                    user_groundkeeping = input(
                        "Expected cost of groundkeeping services per month: $")
                    try:
                        user_groundkeeping = int(user_groundkeeping)
                        break
                    except:
                        print(error)
                new_unit = cls(name=user_name, rent=user_rent, covered_parking=user_covered_parking, laundry=user_laundry,
                               storage=user_storage, misc=user_misc, hoa_dues=user_hoa_dues, water=user_water, electric=user_electric, sewer=user_sewer, garbage=user_garbage, groundskeeping=user_groundkeeping)
                return new_unit

    @property
    def monthly_cash_flow(self):
        return self.monthly_income - self.monthly_expenses

    @property
    def annual_cash_flow(self):
        return self.monthly_cash_flow * 12

    @property
    def monthly_income(self):
        return self.rent + self.covered_parking + self.laundry + self.storage + self.misc

    @property
    def annual_income(self):
        return self.monthly_income * 12

    @property
    def monthly_expenses(self):
        return self.monthly_utilities + self.monthly_savings

    @property
    def annual_expenses(self):
        return self.monthly_expenses * 12

    @property
    def monthly_utilities(self):
        return self.water + self.electric + self.sewer + self.garbage + self.groundskeeping

    @property
    def monthly_savings(self):
        return self.vacancy + self.taxes + self.insurance + self.capital_exp + self.prop_mgmt + self.hoa_dues


class App:
    @classmethod
    def run(self):
        time.sleep(1)
        print("\nWelcome to the Coding Temple ROI Calculator Service.")
        time.sleep(1)
        print("Let's start with some information about you...\n")
        time.sleep(1)
        new_owner = Owner.create()
        time.sleep(1)
        print(f"\nWelcome aboard {new_owner.name.title()}!\n")
        time.sleep(1)
        while len(new_owner.properties) == 0:
            print("Hmm...")
            time.sleep(2)
            print("I see that you don't have any properties on our books.")
            time.sleep(1)
            user_purchase = input(
                "Would you like to add a new one? (Y)es | (N)o\n").lower()
            user_options = ['y', 'yes', 'n', 'no']
            if user_purchase not in user_options:
                print(
                    "Hmm... I'm not sure what you mean. Try answering (y)es or (n)o.\n")
            if user_purchase == 'n' or user_purchase == 'no':
                print("\nThanks for stopping by. Come back another time!\n")
                break
            if user_purchase == 'y' or user_purchase == 'yes':
                time.sleep(1)
                print(
                    "\nGreat! Let's get some more information about that property.\n")
                time.sleep(1)
                new_property = Property.create()
                new_owner.add_property(new_property)
                time.sleep(1)
                print(
                    f"\nAwesome! Now that we have {new_property.name} on our books, we will need some more information about it.\n")
                time.sleep(1)
                print("\nLet's start with fleshing out what kind of units it has...\n")
                time.sleep(1)
                adding_units = True
                while adding_units:
                    while True:
                        new_unit = Unit.create()
                        user_unit_count = input(
                            f"\nHow many units will have this floorplan in {new_property.name}?\n")
                        try:
                            user_unit_count = int(user_unit_count)
                        except:
                            print(f"\nTry entering a number.\n")
                        new_property.add_unit(new_unit, user_unit_count)
                        user_more_units = input(
                            "\nWould you like to add more floorplans? (Y)es | (N)o\n").lower()
                        if user_more_units not in user_options:
                            print(
                                "Hmm... I'm not sure what you mean. Try answering (y)es or (n)o.\n")
                        elif user_more_units == 'n' or user_more_units == 'no':
                            adding_units = False
                            break
                print("\nAlrighty! Let's do some math!\n")
                time.sleep(1)
                print("\nCalculating...\n")
                time.sleep(2)
                print("\nStill calculating...\n")
                time.sleep(1)
                print("\nAha! There we are...\n")
                time.sleep(1)
                print(
                    f"\nYour total annual ROI is {new_owner.annual_return_on_investment}.\n")


App.run()

# brendan = Owner("Brendan", 1000000)
# cottages = Property("Cottages at Bell Station",
#                     250000, 50000, 6000, 12000, 3000)
# brendan.add_property(cottages)
# print(brendan.properties)

# a2 = Unit('A2', 1700, 30, 10, 25, 40, 0, 60, 90, 10, 25, 30)
# cottages.add_unit(a2, 6)

# domain = Property("The Domain", 400000, 80000, 10000, 15000, 8000)
# brendan.add_property(domain)
# print(brendan.properties)

# b1 = Unit('B1', 1300, 0, 0, 0, 20, 100, 100, 120, 60, 60, 120)
# domain.add_unit(b1, 12)


# print(brendan.annual_cash_flow)
# print(brendan.annual_return_on_investment)
# print(brendan.capital)
