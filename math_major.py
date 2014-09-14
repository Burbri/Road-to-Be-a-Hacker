#math_major.py

def what_major()-> None:
    major = input('What major are you?').lower()
    m = 0
    a = 0
    t = 0
    h = 0
    for i in major:
        if i == 'm':
            m+= 1
        elif i == 'a':
            a+= 1
        elif i == 't':
            t+= 1
        elif i == 'h':
            h+= 1
    value = m+a+t+h
        
    if value>= 4:
        print('You must be a math major')
    else:
        print('You must be a humanities major')

if __name__ =='__main__':
    what_major()
