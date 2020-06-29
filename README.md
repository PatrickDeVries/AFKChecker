# AFKChecker

AFKChecker is an application which will scrape codes for the game AFK arena from 
https://afk.guide/redemption-codes/ and track them, notifying a list of recipients 
via email whenever new codes are added. It sends the new code, the rewards associated, 
and a link to the site when a new code is found.

## Setup 
### Files
To make the app run it must be placed in a folder with another folder above it containing 
files devpass.txt with gmail login info and emaillist.txt containing a list of recipients.
devpass.txt should look like:

`email@gmail.com`

`Password123`

It is recommended you use a throwaway account for this since the account will need to have
less secure app access turned on.

emaillist.txt should look like:

`email1@email.com`

`email2@email.com
...`


### Python
You must have Python installed on your system with the libraries BeautifulSoup, requests,
and pandas.

### Initialization
First, run the InitAFK.py script to setup the proejct and create a current list of codes.

### Scheduling
The CheckAFK.py script should then be scheduled to run however you see fit for your OS.
I used the task scheduler on Windows 10 to schedule the execution of the included batch file,
which executes the CheckAFK.py script. I set it to run every 6 hours.

### Result
Once these steps are completed the project will be run automatically and send email notifications if 
a new code is released.
