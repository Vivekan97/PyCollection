def main():
    

    import math

    class Account:

        def __init__(self, bank, name):
            self.name = name
            self.bank = bank
            self.amount = 0
            self.balance = 0
            self.lumpamount = 0
            if self.balance < 0:
                self.balance = 0
            self.emi_per_month = 0
            self.emi_period = 0
            if self.emi_per_month > self.balance:
                self.emi_per_month = self.balance
                self.emi_period = 1

        def loan(self, p, n, roi):
            p, n, roi = float(p), float(n), float(roi / 100)
            interest = (roi * p * n)
            self.amount = interest + p
            self.balance = self.amount
            emi = self.amount / (n * 12)
            self.emi_per_month = math.ceil(emi)
            self.emi_period = math.ceil(self.balance / self.emi_per_month)

        def lump_payment(self, lump, nos):
            paid_amount = float(nos) * self.emi_per_month
            self.lumpamount = lump
            self.balance = self.balance - paid_amount
            self.balance = self.balance - float(lump)
            self.emi_period = math.ceil(self.balance / self.emi_per_month)

        def remaining_balance(self, nos):
            amount_paid = self.emi_per_month*nos+self.lumpamount
            pending = (self.amount - amount_paid)/self.emi_per_month
            print(f'{self.bank} {self.name} {round(amount_paid)} {math.ceil(pending)}')


    # Codeblock to capture the inputs
    print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)

    # Sending the users data into a list
    final = []
    for i in range(len(contents)):
        final.append(contents[i].split(" "))

    # To capture the bank and name details for easy access
    users = {}
    for z in final:
        users[z[1]] = z[2]

    # To create the instances and storing it
    user_methods = {}
    for i in users.items():
        user_methods[i[1]] = Account(i[0], i[1])

    # For unique usernames their corresponding instances are stored into user variable
    for j in final:
        user = user_methods[j[2]]
        # Processing the loan method
        if j[0].lower() == 'loan':
            user.loan(int(j[3]), int(j[4]), int(j[5]))
        # Processing the payment method
        elif j[0].lower() == 'payment':
            user.lump_payment(float(j[3]), float(j[4]))
        # Processing the balance method
        elif j[0].lower() == 'balance':
            user.remaining_balance(float(j[3]))


if __name__ == "__main__":
    main()