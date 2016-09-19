import googlemaps
import configparser
import pprint

config = configparser.ConfigParser()
config.read('api.txt')
key = config.get('apikeys', 'gkey')
gmaps = googlemaps.Client(key=key)

def teststa(startloc):
	teststart = gmaps.geocode(startloc)
	if not teststart:
		return "Error"
	else:
                lat = teststart[0]['geometry']['location']['lat']
                lng = teststart[0]['geometry']['location']['lng']

                endcoords = str(lat) + "," + str(lng)

		return endcoords

def testend(endloc):
	testend = gmaps.geocode(endloc)
	if not testend:
		return "Error"
	else:
                lat = testend[0]['geometry']['location']['lat']
                lng = testend[0]['geometry']['location']['lng']

                endcoords = str(lat) + "," + str(lng)

                return endcoords

