

from datetime import datetime



def headline_stringer():
    day = datetime.today().weekday()
    if day % 2 == 0:
        n = 1
    elif day == 1:
        n = 2
    else: 
        n = 0
    print ( "the index is ", n, " Today is code ", day)
    
    #automating the call 
  

    headline = ["Big Apple. ", "School of Steve Jobs! ", "half off on membership coming soon "]
    return str(headline[n])



