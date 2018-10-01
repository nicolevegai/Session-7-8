# Suppose you can only do additions. Write a program that reads two positive,
# integer numbers a and b. It computes a ** b

Smax = -1000
S = 0
print ("enter exit to end" )
while True:

    num= input ("give me a number: ")

    try:
        num= int (num)

    except:
        print ("That is not an appropriate number, Only integers")
        break # get out of the infinite loop

    S= S + num
    if S > Smax:
        Smax = S

    print ("S max: ",Smax)

