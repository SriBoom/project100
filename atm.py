class Atm(object):

  def __init__(self, withdrawl, credit):
    self.withdrawl = withdrawl
    self.credit = credit

  def withdrawl(self):
    print("Cash Withdrawed")

  def credit(self):
    print("Cash Credited")

atm = Atm("Withdrawed", 80)

print(atm.withdrawl())
