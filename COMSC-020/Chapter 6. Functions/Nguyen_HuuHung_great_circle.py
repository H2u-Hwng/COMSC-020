# Library
from math import radians, acos, sin, cos

# Constants for radius of earth and km to miles
RADIUS = 6371
KM_TO_MILES = 0.621371

# Constants for latitude and longitude of san jose in degrees
LAT_SJ = 37.33
LONG_SJ = -121.9

# Constants for latitude and longitude of chicago in degrees
LAT_CHI = 41.83
LONG_CHI = -87.68

# Constants for latitude and longitude of washington in degrees
LAT_WAS = 38.90
LONG_WAS = -77.02

# Define great circle dist function
def great_circle_dist(lat1, long1, lat2, long2):
    
    # Convert degrees to radians
    lat1 = radians(lat1)
    long1 = radians(long1)
    lat2 = radians(lat2)
    long2 = radians(long2)
    
    # Calculate central angle
    angle = \
acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(abs(long1 - long2)))
    
    # Calculate great circle dist
    distance = RADIUS * angle
    
    return distance

# Define km to miles function
def km_to_miles(distance):
    
    # Convert kms to miles
    distance = distance * KM_TO_MILES
    
    return distance
    
# Define main function
def main():
    
    # Get distance from san jose to chicago in kms and miles
    dist_kms_sj_chi = great_circle_dist(LAT_SJ, LONG_SJ, LAT_CHI, LONG_CHI)
    dist_miles_sj_chi = km_to_miles(dist_kms_sj_chi)
    
    # Get distance from chicago to washington in kms and miles
    dist_kms_chi_was = great_circle_dist(LAT_CHI, LONG_CHI, LAT_WAS, LONG_WAS)
    dist_miles_chi_was = km_to_miles(dist_kms_chi_was)
    
    # Print results
    print(f'The distance from San Jose to Chicago is \
{dist_kms_sj_chi:,.0f} kilometers or {dist_miles_sj_chi:,.0f} miles.')
    print(f'The distance from Chicago to Washington D.C. is \
{dist_kms_chi_was:,.0f} kilometers or {dist_miles_chi_was:,.0f} miles.')
    
# Call main function
main()