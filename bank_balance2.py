sum = 0
print "*********************************"
print "Welcome to Ryan's Bank      "
print "Enter 0 to exit at any time.    "
print "to Deposit enter positive amount"
print "to Withdraw enter negative amount"
print "*********************************"
while 1:
    amt = float(raw_input("Enter amount to transact. $"))
    
    if amt >0:
        print "Please wait.... Depositing..."
    elif amt < 0:
        print "Please wait.... Withdrawing..."    
    else:
        break

    if sum + amt < 0:
        print "transaction cancelled.You don't have enough funds."
    else:
        sum += amt
        
    print "your current balance is $",sum,"."


print "*********************************"
print"Thank you for banking with us.Check out other programs."
