def dist_two_points(loc1,loc2):
    from geopy.distance import great_circle
    loc_1 = (zip_code_details(loc1)['lat'], zip_code_details(loc1)['long'])
    print(loc_1)
    # delhi = (28.7041, 77.1025)
    loc_2 =  (zip_code_details(loc2)['lat'], zip_code_details(loc2)['long'])
    print(loc_2)
 
    return {"distance" :great_circle(loc_1, loc_2).km}