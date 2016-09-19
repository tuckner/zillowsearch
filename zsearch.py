import zillow
import pprint
import sys
import googlemaps
import configparser
from datetime import datetime

api = zillow.ValuationApi()
config = configparser.ConfigParser()
config.read('api.txt')
key = config.get('apikeys', 'zkey')
coords = []

def findloc(*args):
		
	coords = []
	del coords[:]
	for zpid in args:
		detail_data = api.GetZEstimate(key, zpid)
		datadict = (detail_data.get_dict())
		lat = datadict['full_address']['latitude']
		lng = datadict['full_address']['longitude']
		coords.append(lat + "," + lng)
		print coords
	return coords

