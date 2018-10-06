# -- coding: utf-8 --

from geolocation.google_maps import GoogleMaps

address = 'New York City Wall Street 12'

google_maps = GoogleMaps(api_key = 'AIzaSyCqBaEO3JOEwpdTb31ImhXBU6t_7KBJWT8')

location_info = google_maps.query(location=address)

print location_info.all() # return list of all location.

location_info = location_info.first() # return only first location.

print location_info.city

print location_info.route

print location_info.street_number

print location_info.country

print location_info.lat

print location_info.lng
