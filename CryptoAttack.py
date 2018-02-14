import time
import os
import sys

############################ COLORS ############################

yellow = "\033[1;33m"
green  = "\033[32;1m"
white  = "\033[0;1m "
blue   = "\033[34;1m"
red    = "\033[31;1m"

############################ LOGOS ############################

logo='''            .                                                      .
          .n                   .                 .                  n.
    .   .dP                  dP                   9b                 9b.    .
   4    qXb         .       dX                     Xb       .        dXp     t
  dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
  9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
   9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
    `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
      `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
          ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                          )b.  .dbo.dP'`v'`9b.odb.  .dX(
                        ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                       dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                      dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                      9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                       `'      9XXXXXX(   )XXXXXXP      `'
                                XXXX X.`v'.X XXXX  
                                XP^X'`b   d'`X^XX  
                                X. 9  `   '  P )X  
                                `b  `       '  d'
                                 `             ' '''
about = '''
                    \033[1;37m\033[41m[ Debian Linux v9.0 ][ By CryptoCrawll ]\033[0;0m
'''

optionmore = '''  \033[31;1m[\033[32;1m+\033[31;1m] '''
optionless = '''  \033[31;1m[\033[32;1m-\033[31;1m] '''
optionone  = '''  \033[31;1m[\033[32;1m1\033[31;1m] '''
optiontwo  = '''  \033[31;1m[\033[32;1m2\033[31;1m] '''
optiontree = '''  \033[31;1m[\033[32;1m3\033[31;1m] '''

############################ FUNTION LOGO ############################
def flogo():
    
    os.system("clear")
    print green + logo
    print about + "                      \033[1;37m\033[41m[ Start At", time.ctime() + " ]\033[0;0m"

############################ FUNTION MENU ############################

def menu():
    
    print "\n" + optionmore + white + "Do you want to encrypt, decrypt, or hide a file ?" + "\n"

    print optionone  + white + "Encrypt"
    print optiontwo  + white + "Decrypt"
    print optiontree + white + "Hide"

    option = raw_input("\n" + optionless + white + "Choose: ")

    if option == "1":
        
        print "1"

    if option == "2":
        
        print "2"

    if option == "3":
        
        print "3"

    if (option != "1") or (option != "2") or (option != "3"):
        
        print "\n" + optionless + red + "Choose incorrect, try again!"
        time.sleep(1.5)
        os.system("clear")
        flogo()
        menu()

############################ FUNTION MAIN ############################

def main():
    
    flogo()
    menu()

############################ START SCRIPT ############################

try:

    main()

except KeyboardInterrupt:

		print "\n\n" + optionless + white + "Saindo do programa..."
		time.sleep(1.2)
 		exit()
		
############################ 35.196.50.228 ############################
