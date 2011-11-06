guess = input("type the password,hint:it is a six digit number")
key = 200217
if guess != key:

    print"wrong!wrong!wrong!!!!"
else:
    print"the password will let you play my luck game."
    print"you have a chance to live in igloos,mansions,10 houses or units"
    
    place = raw_input("do you like the \na.north,\nb.expensive,\nc.cheap or \nd.crowded.\nenter your choice: ")
    if place == "a":
            print"enjoy living in an igloo."
    elif place == "b":
            print"enjoy living in a mansions."
    elif place == "c":
            print"enjoy living in 10 houses."
    elif place == "d":
            print"enjoy living in a unit."
        
