"""This is my first Python program, Enjoy! 
Sept 2016 @ca9lar"""

def forecast(x):
    from subprocess import call
    call(["curl", "wttr.in/" +x])
while True:
    print
    zip = raw_input('Enter the ZIP or City name for Forecast (Press q or Q to QUIT) :')
    if zip == 'q' or zip == 'Q':
        print 'Have a nice day!'
        break    
    frcst = forecast(zip)
print frcst
