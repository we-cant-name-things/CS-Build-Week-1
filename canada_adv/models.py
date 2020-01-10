from django.db import models


# Create your models here.


class Player(models.Model):
    email = models.EmailField()
    food = models.IntegerField()
    water = models.IntegerField()
    state = models.CharField(max_length=30, blank=False)
    city = models.CharField(max_length=30, blank=False)
    location = models.CharField(max_length=30, blank=False)
    food_available = models.IntegerField(blank=False)
    water_available = models.IntegerField(blank=False)
    location_2 = models.CharField(max_length=30, blank=False)
    food_available_2 = models.IntegerField(blank=False)
    water_available_2 = models.IntegerField(blank=False)

    def __str__(self):
        return "Player email:" + self.email + ", Current City:" + self.city + " Current State:" + self.state


class City:
    def __init__(self, state, city):
        self.state = state
        self.city = city
        self.left = None
        self.right = None
        self.previous = None


class Map:
    def __init__(self):
        self.start = City("Florida", "Miami")

    def search_map(self, city_name):
        data = []
        queue = []
        queue.append(self.start)
        while len(queue) != 0:
            city_viewed = queue.pop(0)
            data.append(city_viewed.city)
            if city_viewed.city.lower() == city_name.lower():
                return city_viewed
            if city_viewed.left:
                queue.append(city_viewed.left)
            if city_viewed.right: queue.append(city_viewed.right)
        return -1

    def insert_left_at(self, current_city, new_state, new_city):
        current_city = self.search_map(current_city)
        if current_city == -1:
            return "City not Found"
        elif current_city != -1:
            if current_city.left:
                return "this city already has a left"
            else:
                new_city = City(new_state, new_city)
                current_city.left = new_city
                new_city.previous = current_city
                return "Success!"

    def insert_right_at(self, current_city, new_state, new_city):
        current_city = self.search_map(current_city)
        if current_city == -1:
            return "City not Found"
        elif current_city != -1:
            if current_city.right:
                return "this city already has a right"
            else:
                new_city = City(new_state, new_city)

                current_city.right = new_city
                new_city.previous = current_city
                return "Success!"

    def to_dict(self, current_city):
        if current_city == None: return
        data = {}
        data['city'] = current_city.city
        data['left'] = self.to_dict(current_city.left)
        data['right'] = self.to_dict(current_city.right)

        return data

    # def to_dict(self, current_city):


map = Map()
# where u at,   where you going: state, city.
map.insert_left_at("Miami", "Florida", "Jacksonville")
map.insert_right_at("Miami", 'Florida', 'Tallahassee')

map.insert_left_at("Jacksonville", "Georgia", "Macon")
map.insert_left_at("Macon", "Georgia", "Atlanta")
map.insert_right_at("Macon", "Georgia", "Augusta")

map.insert_left_at('Tallahassee', 'Alabama', 'Birmingham')
map.insert_left_at('Birmingham', 'Alabama', 'Huntsville')
map.insert_left_at('Huntsville', 'Tennessee', 'Selmer')

map.insert_left_at('Atlanta', 'Tennessee', 'Chattanooga')
map.insert_left_at('Augusta', 'South_Carolina', 'Columbia')
map.insert_left_at('Chattanooga', 'Tennessee', 'Nashville')
map.insert_right_at('Chattanooga', 'Tennessee', 'Knoxville')
map.insert_left_at('Nashville', 'Kentucky', 'Bowling_Green')
map.insert_left_at('Knoxville', 'Virginia', 'Abingdon')

map.insert_left_at('Selmer', 'Tennessee', 'Memphis')
map.insert_left_at('Memphis', 'Missouri', 'Springfield')
map.insert_left_at('Springfield', 'Missouri', 'St_Louis')
map.insert_right_at('Springfield', 'Missouri', 'Kansas_City')

map.insert_left_at('St_Louis', 'Illinois', 'Champaign')
map.insert_left_at('Champaign', 'Illinois', 'Chicago')
map.insert_left_at('Chicago', 'Michigan', 'Grand_Rapids')
map.insert_left_at('Grand_Rapids', 'Michigan', 'Port_Huron')
map.insert_left_at('Port_Huron', 'Canada', 'Canada_2')

map.insert_left_at('Kansas_City', 'Iowa', 'Des_Moines')
map.insert_left_at('Des_Moines', 'Iowa', 'Mason_City')
map.insert_left_at('Mason_City', 'Minnesota', 'Minneapolis')
map.insert_left_at('Minneapolis', 'Minnesota', 'International_Falls')
map.insert_left_at('International_Falls', 'Canada', 'Canada_1')

map.insert_left_at('Bowling_Green', 'Kentucky', 'Louisville')
map.insert_right_at('Bowling_Green', 'Kentucky', 'Lexington')
map.insert_left_at('Louisville', 'Indiana', 'Indianapolis')
map.insert_left_at('Indianapolis', 'Indiana', 'Fort_Wayne')
map.insert_left_at('Fort_Wayne', 'Michigan', 'Ann_Arbor')
map.insert_left_at('Ann_Arbor', 'Michigan', 'Detroit')
map.insert_left_at('Detroit', 'Canada', 'Canada')

map.insert_left_at('Lexington', 'Ohio', 'Cincinnati')
map.insert_left_at('Cincinnati', 'Ohio', 'Toledo')
map.insert_left_at('Toledo', 'Michigan', 'Detroit_2')
map.insert_left_at('Detroit_2', 'Canada', 'Canada_3')

map.insert_left_at('Columbia', 'South_Carolina', 'Florence')
map.insert_left_at('Florence', 'North_Carolina', 'Raleigh')
map.insert_left_at('Raleigh', 'Virginia', 'Richmond')
map.insert_left_at('Richmond', 'Virginia', 'Charlottesville')
map.insert_left_at('Charlottesville', 'West_Virginia', 'Green_Bank')
map.insert_left_at('Green_Bank', 'West_Virginia', 'Bridgeport')
map.insert_left_at('Bridgeport', 'Pennsylvania', 'Pittsburgh')
map.insert_left_at('Pittsburgh', 'Pennsylvania', 'Clarion')
map.insert_left_at('Clarion', 'New_York', 'Salamanca')
map.insert_left_at('Salamanca', 'New_York', 'Buffalo_2')
map.insert_left_at('Buffalo_2', 'Canada', 'Canada_5')

map.insert_right_at('Richmond', 'Virginia', 'Fredericksburg')
map.insert_left_at('Fredericksburg', 'Maryland', 'Baltimore')
map.insert_left_at('Baltimore', 'Maryland', 'Westminster')
map.insert_left_at('Westminster', 'Pennsylvania', 'Harrisburg')
map.insert_left_at('Harrisburg', 'Pennsylvania', 'Mansfield')
map.insert_left_at('Mansfield', 'New_York', 'Elmira')
map.insert_left_at('Elmira', 'Buffalo', 'Canada_4')

map.insert_left_at('Abingdon', 'Virginia', 'Roanoke')
map.insert_left_at('Roanoke', 'West_Virginia', 'Lewisburg')
map.insert_left_at('Lewisburg', 'West_Virginia', 'Charleston')
map.insert_left_at('Charleston', 'Ohio', 'Athens')
map.insert_left_at('Athens', 'Ohio', 'Akron')
map.insert_left_at('Akron', 'Pennsylvania', 'Erie')
map.insert_left_at('Erie', 'New_York', 'Buffalo-3')
map.insert_left_at('Buffalo-3', 'Canada', 'Canada_6')

# -----------------------------------------------------------------------------------------------------------------


# class City:
#     def __init__(self, state, city, left, right, previous):
#         self.state = state
#         self.city = city
#         self.left = left
#         self.right = right
#         self.previous = previous

# Miami = City('Florida', 'Miami', 'Tallahassee', 'Jacksonville', None)
# Jacksonville = City('Florida', 'Jacksonville', 'Macon', None, 'Miami')
# Tallahassee= City('Florida','Tallahassee', 'Birmingham', None, 'Miami')

# Macon = City('Georgia', 'Macon', 'Atlanta', 'Augusta', 'Jacksonville')
# Atlanta = City('Geogia', 'Atlanta', 'Chattanooga', None, 'Macon')
# Augusta = City('Georgia', 'Augusta', 'Columbia', None, 'Macon')

# Birmingham = City('Alabama', 'Birmingham', 'Huntsville', None, 'Tallahassee')
# Huntsville = City('Alabama', 'Huntsville', 'Selmer', None, 'Birmingham')

# Chattanooga = City('Tennessee', 'Chattanooga', 'Nashville', 'Knoxville', 'Atlanta')
# Knoxville = City('Tennessee', 'Knoxville', 'Abingdon', None, 'Chattanooga')
# Nashville = City('Tennessee', 'Nashville', 'Bowling_Green', None, 'Chattanooga')
# Selmer = City('Tennessee', 'Selmer', 'Memphis', None, 'Huntsville')
# Memphis = City('Tennessee', 'Memphis', 'Springfield', None, 'Selmer')

# Columbia = City('South_Carolina', 'Columbia', 'Florence', None, 'Augusta')
# Florence = City('South_Carolina', 'Florence', 'Fayetteville', None, 'Columbia')

# Fayetteville = City('North_Carolina', 'Fayetteville', 'Raleigh', None, 'Florence' )
# Raleigh = City('North_Carolina', 'Raleigh', 'Richmond', None, 'Fayetteville')

# Springfield = City('Missouri', 'Springfield', 'St_Louis', 'Kansas_City', 'Memphis')
# St_Louis = City('Missouri', 'St_Louis', 'Champaign', None, 'Springfield')
# Kansas_City = City('Missouri', 'Kansas_City', 'Des_Moines', None, 'Springfield')

# Champaign = City('Illinois', 'Champaign', 'Chicago', None, 'St_Louis')
# Chicago = City('Illinois', 'Chicago', 'Grand_Rapids', None, 'Champaign')

# Des_Moines = City('Iowa', 'Des_Moines', 'Mason_City', None, 'Kansas_City')
# Mason_City = City('Iowa', 'Mason_City', 'Minneapolis', None, 'Des_Moines')

# Minneapolis = City('Minnesota', 'Minneapolis', 'International_Falls', None, 'Mason_City')
# International_Falls= City('Minnesota', 'International_Falls', 'Canada_1', None, 'Minneapolis')

# Bowling_Green = City('Kentucky', 'Bowling_Green', 'Louisville', 'Lexington', 'Nashville')
# Louisville = City('Kentucky', 'Louisville', 'Indianapolis', None, 'Bowling_Green')
# Lexington = City('Kentucky', 'Lexington', 'Cincinnati', None, 'Bowling_Green')

# Indianapolis = City('Indiana', 'Indianapolis', 'Fort_Wayne', None, 'Louisville')
# Fort_Wayne = City('Indiana', 'Fort_Wayne', 'Ann_Arbor', None, 'Indianapolis')

# Richmond = City('Virginia', 'Richmond', 'Charlottesville', 'Fredericksburg', 'Raleigh')
# Charlottesville = City('Virginia', 'Charlottesville', 'Green_Bank', None, 'Richmond')
# Fredericksburg = City('Virginia', 'Fredericksburg', 'Baltimore', None, 'Richmond')
# Abingdon = City('Virginia', 'Abingdon', 'Roanoke', None, 'Knoxville')
# Roanoke = City('Virginia', 'Roanoke', 'Lewisburg', None, 'Abington')

# Baltimore = City('Maryland', 'Baltimore', 'Westminster', None, 'Fredericksburg')
# Westminster = City('Maryland', 'Westminster', 'Harrisburg', None, 'Baltimore')

# Green_Bank = City('West_Virginia', 'Green_Bank', 'Bridgeport', None, 'Charlottesville')
# Bridgeport = City('West_Virginia', 'Bridgeport', 'Pittsburgh', None, 'Green_Bank')
# Lewisburg = City('West_Virginia', 'Lewisburg', 'Charleston', None, 'Roanoke')
# Charleston = City('West_Virginia', 'Charleston', 'Athens', None, 'Lewisburg')

# Harrisburg = City('Pennsylvania', 'Harrisburg', 'Mansfield', None, 'Westminster')
# Mansfield = City('Pennsylvania', 'Mansfield', 'Elmira', None, 'Harrisburg' )
# Pittsburgh = City('Pennsylvania', 'Pittsburgh', 'Clarion', None, 'Bridgeport')
# Clarion = City('Pennsylvania', 'Clarion', 'Salamanca', None, 'Pittsburgh')
# Erie = City('Pennsylvania', 'Erie', 'Buffalo-3', None, 'Akron')

# Athens = City('Ohio', 'Athens', 'Akron', None, 'Charleston')
# Akron = City('Ohio', 'Akron', 'Erie', None, 'Athens')
# Cincinnati = City('Ohio', 'Cincinnati', 'Toledo', None, 'Lexington')
# Toledo = City('Ohio', 'Toledo', 'Detroit_2', None, 'Cincinnati')

# Grand_Rapids = City('Michigan', 'Grand_Rapids', 'Port_Huron', None, 'Chicago')
# Port_Huron = City('Michigan', 'Port_Huron', 'Canada_2', None, 'Grand_Rapids')
# Ann_Arbor = City('Michigan', 'Ann_Arbor', 'Detroit', None, 'Fort_Wayne')
# Detroit = City('Michigan', 'Detroit', 'Canada', None, 'Ann_Arbor')
# Detroit_2 = City('Michigan', 'Detroit_2', 'Canada_3', None, 'Toledo')

# Elmira = City('New_York', 'Elmira', 'Buffalo', None, 'Mansfield')
# Salamanca = City('New_York', 'Salamanca', 'Buffalo_2', None, 'Clarion')
# Buffalo = City('New_York', 'Buffalo', 'Canada_4', None, 'Elmira')
# Buffalo_2 = City('New_York', 'Buffalo_2', 'Canada_5', None, 'Salamanca')
# Buffalo_3 = City('New_York', 'Buffalo_3', 'Canada_6', None, 'Erie')

# Canada = City('Canada', 'Canada', None, None, 'Detroit')
# Canada_1 = City('Canada', 'Canada', None, None, 'International_Falls')
# Canada_2= City('Canada', 'Canada', None, None, 'Port_Huron')
# Canada_3 = City('Canada', 'Canada_3', None, None, 'Detroit_2')
# Canada_4 = City('Canada', 'Canada', None, None, 'Buffalo')
# Canada_5 = City('Canada', 'Canada', None, None, 'Buffalo_2')
# Canada_6 = City('Canada', 'Canada', None, None, 'Buffalo_3')


# -------------------------------------------------------------------------------------------------------------------
# locations = {
# 'Florida': {
#     'cities': {
#         'Miami': {
#             'left':'Jacksonville',
#             'right':'Tallahassee',
#             'previous': None
#         },
#         'Jacksonville': {
#             'left': 'Macon',  # to GA
#             'right': None,
#             'previous': 'Miami'
#         },
#         'Tallahassee': {
#             'left':'Birmingham',  # to AL
#             'right': None,
#             'previous': 'Miami'
#         },
#     }
# },

# 'Georgia': {
#     'cities': {
#         'Macon': {
#             'places': random_geneator_pick_2(places) # starting from FL
#         },
#         'Atlanta': {
#             'places': random_geneator_pick_2(places)(places) # to TN
#         },
#         'Augusta':{
#             'places': random_geneator_pick_2(places) # to SC
#         },

#     }
# },

# 'Alabama':{
#     'cities':{
#         'Birmingham': {
#             'places': random_geneator_pick_2(places) # starting from FL
#         },
#         'Huntsville': {
#             'places': random_geneator_pick_2(places) # to TN
#         }
#     }
# },

# 'Tennessee':{
#     'cities':{
#         'Chattanooga':{
#             'places': random_geneator_pick_2(places) # starting from GA
#         },
#         'Knoxville':{
#             'places': random_geneator_pick_2(places) # to VA
#         },
#         'Nashville':{
#             'places': random_geneator_pick_2(places) # to KY
#         },
#         'Selmer':{
#             'places': random_geneator_pick_2(places) # starting from AL
#         },
#         'Memphis':{
#             'places': random_geneator_pick_2(places) # to Missouri
#         }
#     }
# },

# 'South_Carolina':{
#     'cities':{
#         'Columbia':{
#             'places': random_geneator_pick_2(places) # starting from GA
#         },
#         'Florence':{
#             'places': random_geneator_pick_2(places) # to NC
#         }
#     },
# },

# 'North_Carolina':{
#     'cities':{
#         'Fayetteville':{
#              'places': random_geneator_pick_2(places) # starting from SC
#         },
#         'Raleigh':{
#             'places': random_geneator_pick_2(places) # to VA
#         }
#     }
# },


# 'Missouri':{
#     'cities':{
#         'Springfield':{
#             'places': random_geneator_pick_2(places)# starting from TN
#         },
#         'St_Louis':{
#             'places': random_geneator_pick_2(places)# to Illinois
#         },
#         'Kansas_City':{
#             'places': random_geneator_pick_2(places)# to Iowa
#         }
#     }
# },

# 'Illinois':{
#     'cities':{
#         'Champaign':{
#             'places': random_geneator_pick_2(places)# from Missouri
#         },
#         'Chicago':{
#             'places': random_geneator_pick_2(places)# to MI
#         }

#     }
# },

# 'Iowa':{
#     'cities':{
#         'Des_Moines':{
#             'places': random_geneator_pick_2(places) # from Missouri
#         },
#         'Mason_City':{
#             'places': random_geneator_pick_2(places) # to Minnesota
#         }

#     }
# },

# 'Minnesota':{
#     'cities':{
#         'Minneapolis':{
#             'places': random_geneator_pick_2(places) # from Iowa
#         },
#         'International_Falls':{
#             'places': random_geneator_pick_2(places) # to Canada
#         }
#     }
# },

# 'Michigan':{
#     'cities':{
#         'Grand_Rapids':{
#             'places': random_geneator_pick_2(places)# from Chicago
#         },
#         'Port_Huron':{
#             'places': random_geneator_pick_2(places)# from Grand_Rapid to Canada
#         },
#         'Ann_Arbor':{
#             'places': random_geneator_pick_2(places) # from Indiana
#         },
#         'Detroit':{
#             'places': random_geneator_pick_2(places) #from Ann_Arbor to Canada
#         },
#         'Detroit-2':{
#             'places': random_geneator_pick_2(places) # from Ohio to Canada
#         }
#     }
# },

# 'Kentucky':{
#     'cities':{
#         'Bowling_Green':{
#             'places': random_geneator_pick_2(places) #from TN
#         },
#         'Lexington':{
#             'places': random_geneator_pick_2(places) #to Ohio
#         },
#         'Louisville':{
#             'places': random_geneator_pick_2(places) # to Indiana
#         }
#     }
# },

# 'Indiana':{
#     'cities':{
#         'Indianapolis':{
#             'places': random_geneator_pick_2(places) #from KY
#         },
#         'Fort_Wayne':{
#             'places': random_geneator_pick_2(places) #to MI
#         }
#     }
# },

# 'Virginia':{
#     'cities':{
#         'Richmond':{
#             'places': random_geneator_pick_2(places) # starting from NC
#         },
#         'Fredericksburg':{
#             'places': random_geneator_pick_2(places) # to MD
#         },
#         'Charlottesville':{
#             'places': random_geneator_pick_2(places) # to WV-1
#         },
#         'Abingdon':{
#             'places': random_geneator_pick_2(places) # starting from TN
#         },
#         'Roanoke':{
#             'places': random_geneator_pick_2(places) # to WV-2
#         }

#     }
# },


# 'Maryland':{
#     'cities':{
#         'Baltimore':{
#             'places': random_geneator_pick_2(places) #starting from VA
#         },
#         'Westminster':{
#             'places': random_geneator_pick_2(places) #to PA-1
#         }
#     }
# },

# 'West_Virginia':{
#     'cities':{
#         'Green_Bank':{
#             'places': random_geneator_pick_2(places) #starting from VA-1
#         },
#         'Bridgeport':{
#             'places': random_geneator_pick_2(places) # to PA-2
#         },
#         'Lewisburg':{
#             'places': random_geneator_pick_2(places) #starting from VA-2
#         },
#         'Charleston':{
#             'places': random_geneator_pick_2(places) #to OH-1
#         }
#     }
# },

# 'Pennsylvania':{
#     'cities':{
#         'Harrisburg':{
#             'places': random_geneator_pick_2(places)# starting from Maryland
#         },
#         'Mansfield':{
#             'places': random_geneator_pick_2(places)# from Harrisburg to NY-1
#         },
#         'Pittsburgh':{
#             'places': random_geneator_pick_2(places)# starting from WV
#         },
#         'Clarion':{
#             'places': random_geneator_pick_2(places)# from pittsburg to NY-2
#         },
# 'Erie':{
#     'places': random_geneator_pick_2(places) #from OH to NY-3
# }
#     }
# },

# 'New_York':{
#     'cities':{
#         'Elmira':{
#             'places': random_geneator_pick_2(places) #from PA-Mansfield
#         },
#         'Salamanca':{
#             'places': random_geneator_pick_2(places) #from PA-Clarion
#         },
#         'Buffalo':{
#             'places': random_geneator_pick_2(places) #from Elmira to Canada **
#         },
#         'Buffalo_2':{
#             'places': random_geneator_pick_2(places) #from Salamanca to Canada **
#         },
#         'Buffalo_3':{
#             'places': random_geneator_pick_2(places) # from PA-Erie
#         }
#     }
# },

# 'Ohio':{
#     'cities':{
#         'Athens':{
#             'places': random_geneator_pick_2(places) # starting from WV
#         },
#         'Akron':{
#             'places': random_geneator_pick_2(places) # from Athens to PA
#         },
#         'Cincinnati':{
#             'places': random_geneator_pick_2(places) # starting from KY
#         },
#         'Toledo':{
#             'places': random_geneator_pick_2(places) # from Cincinnati to MI
#         }
#     }
# }
# }
