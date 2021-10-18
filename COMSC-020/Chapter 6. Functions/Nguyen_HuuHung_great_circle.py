# Huu Hung Nguyen
# 10/17/2021
# Nguyen_HuuHung_great_circle.py
# Constants for radius of earh in kilometers, 1 kilometer to miles, latitude,
# and longitude of 3 cities
# Program contains 2 functions calculating great circle distance,
# and converting kilometers to miles.
# It then displays distances in both kilometers and miles.

# Library
from math import radians, acos, sin, cos

# Constants for radius of earh in kilometers and 1 kilometer to miles
RADIUS = 6371
KM_TO_MILES = 0.621371

# Constants for latitudes of San Jose, Chicago, and Washington DC in degrees
LAT_SJ = 37.33
LAT_CHI = 41.83
LAT_WAS = 38.90

# Constants for longitudes of San Jose, Chicago, and Washington DC in degrees
LONG_SJ = -121.9
LONG_CHI = -87.68
LONG_WAS = -77.02

# Take latitude and longitude of 2 cities
# Convert degrees to radians, calculate central angle and distance
# Return distance in kilometers between 2 cities
def great_circle_distance(lat1, long1, lat2, long2):
    
    # Convert degrees to radians
    lat1_rad = radians(lat1)
    long1_rad = radians(long1)
    lat2_rad = radians(lat2)
    long2_rad = radians(long2)
    
    # Calculate central angle
    angle = acos(sin(lat1_rad) * sin(lat2_rad) + \
            cos(lat1_rad) * cos(lat2_rad) * cos(abs(long1_rad - long2_rad)))
    
    # Calculate distance in kilometers
    distance_kms = RADIUS * angle
    
    return distance_kms


# Take distance in kilometers
# Convert kilometers to miles and return distance in miles
def km_to_miles(distance_kms):
    
    # Convert kilometers to miles
    distance_miles = distance_kms * KM_TO_MILES
    
    return distance_miles
    
    
# Define main function
def main():
    
    # Obtain distance from San Jose to Chicago in kilometers and miles
    kms_sj_chi = great_circle_distance(LAT_SJ, LONG_SJ,
                                            LAT_CHI, LONG_CHI)
    miles_sj_chi = km_to_miles(kms_sj_chi)
    
    # Obtain distance from Chicago to Washington DC in kilometers and miles
    kms_chi_was = great_circle_distance(LAT_CHI, LONG_CHI,
                                             LAT_WAS, LONG_WAS)
    miles_chi_was = km_to_miles(kms_chi_was)
    
    # Display 2 distances in both kilometers and miles
    print('The distance from San Jose to Chicago is ', end = '')
    print(f'{kms_sj_chi :,.0f} kilometers or {miles_sj_chi :,.0f} miles.')
    
    print('The distance from Chicago to Washington D.C. is ', end = '') 
    print(f'{kms_chi_was :,.0f} kilometers or {miles_chi_was :,.0f} miles.')
    
# Call main function
main()