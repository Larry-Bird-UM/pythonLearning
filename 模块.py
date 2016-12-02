import sys

print 'The command line arguments are:'
for i in sys.argv:
    print i

print '\n\nThe PYTHONPATH is',sys.path, '\n'

def main():
    print "We are in %s"%__name__
if __name__ == '__main__':
    main()

print dir(sys)