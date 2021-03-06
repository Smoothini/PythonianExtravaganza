import math, datetime

#dictionary with neighbours
dicc = {1: [1,2,4,77],
        2: [2,1,13,14,77],
        3: [3,4,5,6,77],
        4: [4,2,3,5,13,14,16],
        5: [5,3,4,6,7,14,16,21,22],
        6: [6,3,4,5,7],
        7: [7,5,6,8,21,22,24],
        8: [8,7,22,24,28,32],
        9: [9,10,12,76],
        10: [10,9,11,12,15,17,76],
        11: [11,10,12,15],
        12: [12,10,11,13,14,15,16],
        13: [13,2,4,12,14],
        14: [14,4,5,12,13,15,16],
        15: [15,11,12,14,16,17,19,20],
        16: [16,4,5,11,12,14,15,20,21],
        17: [17,15,18,19,76],
        18: [18,17,19,25],
        19: [19,15,16,17,18,20,25],
        20: [20,15,16,19,21,22,23,25],
        21: [21,5,16,20,22],
        22: [22,5,7,20,21,23,24],
        23: [23,20,22,24,25,26,27,28],
        24: [24,7,8,22,23,27,28,32],
        25: [25,18,19,20,23,26],
        26: [26,23,25,27,29],
        27: [27,23,24,26,28,29],
        28: [28,8,23,24,27,29,30,31,32,33,34],
        29: [29,26,27,28,30,31],
        30: [30,28,29,31,56,57,58,59],
	31: [31,28,29,30,33,34,58,59,60],
	32: [32,8,28,33],
	33: [33,28,31,32,34,35],
	34: [34,28,31,33,35,37,38,61],
	35: [35,33,34,36,37,38],
	36: [36,35,38,39],
	37: [37,34,35,38,40,60,61,68],
	38: [38,34,35,36,37,39,40,41],
	39: [39,36,38,40,41],
	40: [40,37,38,39,41,42,68,69],
	41: [41,38,39,40,42],
	42: [42,40,41,43,69],
	43: [43,42,45,46,69],
	44: [44,45,47,49,50,71,73],
	45: [45,43,44,46,47,48,69],
	46: [46,43,45,48,51,52],
	47: [47,44,45,48,49,50,51],
	48: [48,44,45,46,47,50,51,52],
	49: [49,44,47,50,53,54],
	50: [50,44,47,48,49,51,53,54],
	51: [51,46,47,48,50,52,54,55],
	52: [52,46,48,51,55],
	53: [53,49,50,54,75],
	54: [54,49,50,51,53,55],
	55: [55,51,52,54],
	56: [56,30,57,62,64,65],
	57: [57,30,56,58,62,63],
	58: [58,30,31,57,59,61,62,63],
	59: [59,30,31,58,60,61],
	60: [60,31,34,37,59,61],
	61: [61,37,58,59,60,63,66,67,68],
	62: [62,56,57,58,63,64,65,66],
	63: [63,57,58,61,62,65,66,67],
	64: [64,56,62,65],
	65: [65,56,62,63,64,66,70],
	66: [66,62,63,65,67,70,71],
	67: [67,61,63,66,68,70,71],
	68: [68,37,40,61,67,69,71],
	69: [69,40,42,43,44,45,71],
	70: [70,65,66,67,71,72],
	71: [71,44,49,66,67,68,69,70,72,73],
	72: [72,70,71,73,74,75],
	73: [73,44,49,71,72,75],
	74: [74,72,75],
	75: [75,49,53,72,73,74],
	76: [76,9,10,17],
	77: [77,1,2,3,4]}

#returns the neighbour array
def get_neighbour(community):
    return dicc[community]


#haversine formula
#x is latitude, y is longitude
def get_distance(x1,y1,x2,y2):
    dx = deg2rad(x2-x1)
    dy = deg2rad(y2-y1)
    R = 6371
    a = math.sin(dx/2) * math.sin(dx/2) + math.cos(deg2rad(y1)) * math.cos(deg2rad(y2)) * math.sin(dy/2) * math.sin(dy/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d
#degrees to radians converter
def deg2rad(deg):
  return deg * (math.pi/180)


#count the number of taxis around a crime
def taxi_counter(crime):
    count = 0
    for neighbour in get_neighbour(crime["community"]):
        count = count + taxi_in_area(neigh)
    
#count the number of taxis in a community
#based on certain regulations
#community -> timestamp -> distance
def taxi_in_area(area):
    d = 1.5 #km
    count = 0
    #filter by community
    #
    #code here pls <3
        #filter result by time
        #taxis already ordered by time
        #for efficiency we could convert the time to epoch
        #and then subtract 1 jan 2013 from it datetime.datetime(2013,1,1).timestamp()
        #to see around what index to start lookin for taxis
        #
        #code here pls <3
            #last but not least check every left over taxi
            #if its in the 1.5km radius with get distance
            #this one last because its the most resources using one
            #I mean I think, not sure if this or time, will see
            #count = count + 1
            #
            #code also here pls <3


#random tested working distance from uc house to center, should be ~5.5
print(get_distance(57.044890, 9.914537, 57.006953, 9.882486))

