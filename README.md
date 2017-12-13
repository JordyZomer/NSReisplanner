# NSReisplanner
A script used to check if planned train departure matches actual train departure using the NS API.

I personally run the script in a cronjob that e-mails me the results every morning.

# Usage 

You need python 3 and the following libraries to run the script.

- argparse
- requests
- bs4 

You can run the script with the following arguments:

    python3.6 ns.py --fromStation zwolle --toStation enschede --user NS_API_USER --password NS_API_PASS --departure true
    
Have fun using it.

The I don't give a fuck license applies to this.
