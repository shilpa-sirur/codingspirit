def prob1():
	x=float(raw_input('Enter the outstanding_balance on your credit card:'))
	y=float(raw_input('Enter the annual_credit_card_interest_rate as a decimal:'))
	z=float(raw_input('Enter the minimum_monthly_payment_rate as a decimal:'))

	months = 1
	Total_min_mon_payment = 0
	while months <= 12 :
		min_mon_payment = round(z*x,2)
		interest_paid = (y/12 * x)
		principal_paid = round(min_mon_payment - interest_paid,2)
		Remaining_Balance = round(x - principal_paid,2)
		print ' Month:', months
		print'minimum_monthly_payment :', min_mon_payment
		print 'Principle Paid :', principal_paid
		print 'Remaining Balance :', Remaining_Balance
		Total_min_mon_payment = Total_min_mon_payment + min_mon_payment 
		months +=1
		x = Remaining_Balance
	print 'RESULT'
	print 'Total amount Paid :', Total_min_mon_payment
	print 'Remaining Balance :', Remaining_Balance
		

