import sys


def main():
    input_file = sys.argv[1]
    import math

    class Account:

        def __init__(self, bank, name):
            self.user_name = name
            self.bank_name = bank
            self.total_amount = 0
            self.account_balance = 0
            if self.account_balance < 0:
                self.account_balance = 0
            self.lump_amount = 0
            self.lump_amount_time = 0
            self.emi_per_month = 0
            self.emi_period = 0

        def loan(self, p, n, roi):
            principal, no_of_years, rate_of_interest = float(p), float(n), float(roi / 100)
            interest = (rate_of_interest * principal * no_of_years)
            self.total_amount = interest + principal
            self.account_balance = self.total_amount
            emi = self.total_amount / (no_of_years * 12)
            self.emi_per_month = math.ceil(emi)
            self.emi_period = math.ceil(self.account_balance / self.emi_per_month)

        def lump_payment(self, lump, no_of_months):
            paid_amount = float(no_of_months) * self.emi_per_month
            self.lump_amount = lump
            self.lump_amount_time = no_of_months
            self.account_balance = self.account_balance - paid_amount
            self.account_balance = self.account_balance - float(lump)
            self.emi_period = math.ceil(self.account_balance / self.emi_per_month)

        def remaining_balance(self, no_of_months):
            if no_of_months < self.lump_amount_time:
                amount_paid = self.emi_per_month * no_of_months
                if self.emi_per_month * no_of_months > self.total_amount-self.lump_amount:
                    amount_paid = self.account_balance+self.lump_amount
            else:
                amount_paid = self.emi_per_month*no_of_months+self.lump_amount
                if self.emi_per_month*no_of_months > self.total_amount-self.lump_amount:
                    amount_paid = self.account_balance+self.lump_amount
            pending = (self.total_amount - amount_paid)/self.emi_per_month
            print(f'{self.bank_name} {self.user_name} {round(amount_paid)} {math.ceil(pending)}')

    # Capturing the input from the input file
    initial_input = open(input_file)
    content = [initial_input.read()]
    contents = content[0].split('\n')

    user_inputs = []
    for i in range(len(contents)):
        user_inputs.append(contents[i].split(" "))

    # Capturing the bank and name details and storing it in user_attributes for further steps
    user_attributes = {}
    for user_input in user_inputs:
        user_attributes[user_input[1]] = user_input[2]

    # Storing the instances with their corresponding key values in dict user_methods
    user_methods = {}
    for i in user_attributes.items():
        user_methods[i[0]+i[1]] = Account(i[0], i[1])

    # For unique username+bankname their corresponding instances are stored into user variable below
    for user_input in user_inputs:
        user = user_methods[user_input[1]+user_input[2]]

        # Processing the loan method
        if user_input[0].lower() == 'loan':
            user.loan(int(user_input[3]), int(user_input[4]), int(user_input[5]))

        # Processing the payment method
        elif user_input[0].lower() == 'payment':
            user.lump_payment(float(user_input[3]), float(user_input[4]))

        # Processing the balance method
        elif user_input[0].lower() == 'balance':
            user.remaining_balance(float(user_input[3]))


if __name__ == "__main__":
    main()
