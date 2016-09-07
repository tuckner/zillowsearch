import googlemaps
import datetime
import pprint
import zsearch
import configparser

config = configparser.ConfigParser()
config.read('api.txt')
key = config.get('apikeys', 'gkey')
gmaps = googlemaps.Client(key=key)

def genroute(*args):
	listcoords = zsearch.findloc(args)
	formatcoords = "[\"" + listcoords[0] + "\", \"" + listcoords[1] + "\", \"" + listcoords[2] + "\"]" 
	print formatcoords
	route = gmaps.directions("38.9838505,-94.6218913", "38.9838505,-94.6218913", waypoints=listcoords, optimize_waypoints=True)

	routes = []
	del routes[:]
	for i, val in enumerate(route[0]['legs']): 
		lat = val['end_location']['lat']
		lng = val['end_location']['lng']
		cords = str(lat) + "," + str(lng)
		routes.append(cords)

	routelink = "https://www.google.com/maps/dir/38.9838505,-94.6218913/" + routes[0] + "/" + routes[1] + "/" + routes[2] + "/" + routes[3]
	maplink = "https://google.com/maps/embed/v1/directions?key=" + key + "&origin=38.9838505,-94.6218913&destination=38.9838505,-94.6218913&waypoints=" + routes[0] + "|" + routes[1] + "|" + routes[2]

	return routelink, maplink

