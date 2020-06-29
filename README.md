# AFKChecker

AFKChecker is an application which will scrape codes for the game AFK arena from 
https://afk.guide/redemption-codes/ and track them, notifying a list of recipients 
via email whenever new codes are added. It sendsthe code, the rewards associated, 
and a link to the site when a new code is found.

Setup 
To make the app run it must be placed in a folder with another folder above it containing 
files devpass.txt with gmail login info and emaillist.txt containing a list of recipients.

You must have Python installed on your system with the libraries BeautifulSoup, requests,
and pandas.

First, run the InitAFK.py script to setup the proejct and create a current list of codes.
The CheckAFK.py script should then be scheduled to run however you see fit for your OS.
I used the task scheduler on Windows 10 to schedule the execution of the included batch file,
which executes the CheckAFK.py script. I set it to run every 6 hours.

Once this is done the project will be run automatically and send email notifications if 
a new code is released.
