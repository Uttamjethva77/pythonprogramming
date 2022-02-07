for a in range(1,101):
    if a%3==0 and a%5==0:
        print ('foobar')
    elif a%5==0:
        print ('bar')
    elif a%3==0:
        print('foo')
    else:
        print(a)
        a=a+1
