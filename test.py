#!/usr/bin/python
import platform
print platform.uname()
print platform.release()
num = 1
print id(num)
num = 2
print id(num)
name = "Jerry"
print name[1]
print name[0:3]
print name[0:4:2]

name = "Jerry"
test = "Jerry"
print name is test

print type(name) is type(test)

a = raw_input("plz enter a number:")
