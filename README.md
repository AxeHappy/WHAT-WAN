# WHAT-WAN

I created this particularly because of ISP's changing their WAN for residents every so often. If you're like me you host something at your residence
that you need access to. This script will save a log file of your current IP and when ran, if the IP is different it will replace the log file with
the new WAN IP. 

Myself, I have a crontab setup to run. I plan on adding a secure starttls() or ssl for encrypted email so I can have it sent to me if I'm not home.

####
To run: python3 whatwan.py
