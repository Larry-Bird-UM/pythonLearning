#!/usr/bin/python

def func(x):
    print 'x is ', x
    x = 2
    print 'changed local x to', x

x = 50
func(x)

print 'x is still', x


def say(message,times=2):
    print message * times
    return times
say('Hello')
say('World',5)
print say('fuck',10)

def func(a,b=10,c=15):
    print 'a is', a,'and b is',b,'and c is',c
func(3,7)
func(25,c=24)
func(c=5,a=100)

def printMax(x,y):
    '''Prints the maximum of two numbers.

    The two values must be integer.'''
    x = int(x)
    y = int(y)

    if x>y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

printMax(3,5)
print printMax.__doc__

