import subprocess
print "----------- Welcome to the EtherSec Tool-Master -----------"
print "               ..."
print "             ;::::;                 ~NSP/xTreatyz          "
print "           ;::::; :;"
print "         ;:::::'   :;"
print "        ;:::::;     ;."
print "       ,:::::'       ;           OOO0"
print "       ::::::;       ;          OOOOO0"
print "       ;:::::;       ;         OOOOOOOO"
print "      ,;::::::;     ;'         / OOOOOOO"
print "    ;:::::::::`. ,,,;.        /  / DOOOOOO"
print "  .';:::::::::::::::::;,     /  /     DOOOO"
print " ,::::::;::::::;;;;::::;,   /  /        DOOO"
print ";`::::::`'::::::;;;::::: ,#/  /          DOOO"
print ":`:::::::`;::::::;;::: ;::#  /            DOOO"
print "::`:::::::`;:::::::: ;::::# /              DOO"
print "`:`:::::::`;:::::: ;::::::#/               DOO"
print " :::`:::::::`;; ;:::::::::##                OO"
print " ::::`:::::::`;::::::::;:::#                OO"
print " `:::::`::::::::::::;'`:;::#                O"
print "  `:::::`::::::::;' /  / `:#"
print "   ::::::`:::::;'  /  /   `#"
print "-----------------------------------------------------------"
print "\r\n"
print "Choose your options: (1-2)"
print "[1] ScreenLogger Builder"
print "[2] LoginServer Builder"
Option = raw_input('Option: ')
print "\r\n"
if Option == '1':
    subprocess.call("ScreenLogger.py", shell=True)
if Option == '2':
    subprocess.call("LoginServer.py", shell=True)
