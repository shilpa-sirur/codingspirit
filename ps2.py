x = float(raw_input ("Enter the outstanding balance on the ctredit card : ") )
y = float(raw_input ("Enter the annual interest rate as a decimal : "))
interest_paid = round(y/12.0,2)

balance = x
interest_paid = y/12
min_mon_payment = 0
new_balance = balance
while new_balance > 0:
	min_mon_payment += 10
	new_balance = balance
	month = 1
	while month <= 12 and new_balance > 0:
#		new_balance -= min_mon_payment
#		new_balance += (interest_paid * new_balance)
		new_balance =  new_balance * (1 + interest_paid) - min_mon_payment
		month += 1    
print 'Min Monthly Payment :',min_mon_payment
print 'Total months required :',month-1
print 'Balance :',round(new_balance,2)
