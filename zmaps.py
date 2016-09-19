import googlemaps
import datetime
import pprint
import zsearch
import configparser
import zgeocode

config = configparser.ConfigParser()
config.read('api.txt')
key = config.get('apikeys', 'gkey')
gmaps = googlemaps.Client(key=key)

def genroute(*args):
	
	listcoords = zsearch.findloc(args[0], args[1], args[2])
	formatcoords = "[\"" + listcoords[0] + "\", \"" + listcoords[1] + "\", \"" + listcoords[2] + "\"]" 
	print formatcoords
	startloc = zgeocode.teststa(args[3])
	endloc = zgeocode.testend(args[4])
	
	route = gmaps.directions(startloc, endloc, waypoints=listcoords, optimize_waypoints=True)

	routes = []
	del routes[:]
	for i, val in enumerate(route[0]['legs']): 
		lat = val['end_location']['lat']
		lng = val['end_location']['lng']
		cords = str(lat) + "," + str(lng)
		routes.append(cords)

	routelink = "https://www.google.com/maps/dir/" + startloc + "/" + routes[0] + "/" + routes[1] + "/" + routes[2] + "/" + endloc 
	maplink = "https://google.com/maps/embed/v1/directions?key=" + key + "&origin=" + startloc + "&destination=" + endloc + "&waypoints=" + routes[0] + "|" + routes[1] + "|" + routes[2]

	return routelink, maplink

