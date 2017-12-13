#!/usr/bin/python
import argparse
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Script om reistijden van NS te matchen met actuele vertrektijden')
parser.add_argument('--fromStation', type=str, help='De code (afkorting) of korte naam of middellange naam of volledige naam of synoniem van vertrekstation')
parser.add_argument('--toStation', type=str, help='De code (afkorting) of korte naam of middellange naam of volledige naam of synoniem van het aankomststation')
parser.add_argument('--departure', type=str, help='Boolean (true of false) die aangeeft of de dateTime parameters de gewenste vertrektijd (=true en de default) dan wel de aankomsttijd is (=false)')
parser.add_argument('--user', type=str, help='NS API Username')
parser.add_argument('--password', type=str, help="NS API Password")
args = parser.parse_args()

fromStation = args.fromStation
toStation = args.toStation

Departure = args.departure
username = args.user
password = args.password

requestURL = 'https://webservices.ns.nl/ns-api-treinplanner?fromStation=%s&toStation=%s&Departure=%s' % (fromStation, toStation, Departure)


resp = requests.get(requestURL, auth=HTTPBasicAuth(username, password))
soup = BeautifulSoup(resp.text, 'xml')

gepland = str(soup.select_one('GeplandeVertrekTijd').contents)
actueel = str(soup.select_one('ActueleVertrekTijd').contents)


if gepland != actueel:
    print("De geplande vertrek tijd %s komt niet overeen met de actuele vertrek tijd %s") % (gepland, actueel)


else:
    print("De vertrektijden komen overeen!")