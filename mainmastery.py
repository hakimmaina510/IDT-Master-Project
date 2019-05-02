'''
Name: Rohit Nachaloor
Date Submitted: 05/01/2019
Mastery Project
Period: 1
Cowart
'''

#importing modules
from masterymod1 import setup
from masterymod2 import place
from masterymod3 import review
from masterymod4 import final
from masterymod5 import view
from masterymod6 import test
from masterymod7 import mail
import sys

def main():
    print('Hi! This tool allows you to store your grades and find your average using those stored grades.')
    # options for the user
    print('Do you want to ...')
    print('a. Setup a new class')
    print('b. Insert grades into an existing class.')
    print('c. See all your assignments in a list')
    print('d. Find out your average')
    print('e. Test out how your grade will be affected by a regular grade.')
    print('f. Test out how your grade will be affected by a final exam grade.')
    print('g. Email your grades and your averages to an email address.')
    print('h. Quit Program')
    ans = input()
    #if statment tied to whatever option the user chooses. 
    if (ans == 'a'):
        setup()
        main()

    if (ans == 'b'):
        place()
        main()

    if (ans == 'c'):
        view()
        main()

    if (ans == 'd'):
        review()
        main()

    if (ans == 'e'):
        test()
        main()

    if (ans == 'f'):
        final()
        main()

    if (ans == 'g'):
        mail()
        main()

    #This allows the user to double check whether they want to quit or not.
    if (ans == 'h'):
        print('Are you sure you want to quit? (Y/N)')
        yn = input()
        if (yn == 'Y'):
            sys.exit()
        elif (yn == 'N'):
            main()
        else:
            print('Sorry, we did not understand your response.')
            main()

if (__name__ == '__main__'):
    main()
