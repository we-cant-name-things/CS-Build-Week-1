from django.db import models


# Create your models here.


class Place(models.Model):
    state = models.CharField(max_length=30, blank=False)
    city = models.CharField(max_length=30, blank=False)
    location = models.CharField(max_length=30, blank=False)
    food_available = models.IntegerField(blank=False)
    water_available = models.IntegerField(blank=False)

    def __str__(self):
        return "City:" + self.city + ", location:" + self.location


class Player(models.Model):
    email = models.EmailField()
    food = models.IntegerField()
    water = models.IntegerField()
    current_place = models.ForeignKey(Place, on_delete=models.PROTECT)

    def __str__(self):
        return "Player email:" + self.email


places = ('gas_station', 'hotel', 'fast_food', 'bank', 'store')

import random


def random_geneator_pick_2(tuple):
    random_place_1 = random.choice(tuple)
    random_place_2 = random.choice(tuple)

    return [random_place_1, random_place_2]








locations = {
    'Florida': {
        'cities': {
            'Miami': {
                'places': random_geneator_pick_2(places)  # starting
            },
            'Jacksonville': {
                'places': random_geneator_pick_2(places)  # to GA
            },
            'Tallahassee': {
                'places': random_geneator_pick_2(places)  # to AL
            },
        }
    },

    'Georgia': {
        'cities': {
            'Macon': {
                'places': random_geneator_pick_2(places)  # starting from FL
            },
            'Atlanta': {
                'places': random_geneator_pick_2(places)  # to TN
            },
            'Augusta': {
                'places': random_geneator_pick_2(places)  # to SC
            },

        }
    },

    'Alabama': {
        'cities': {
            'Birmingham': {
                'places': random_geneator_pick_2(places)  # starting from FL
            },
            'Huntsville': {
                'places': random_geneator_pick_2(places)  # to TN
            }
        }
    },

    'Tennessee': {
        'cities': {
            'Chattanooga': {
                'places': random_geneator_pick_2(places)  # starting from GA
            },
            'Knoxville': {
                'places': random_geneator_pick_2(places)  # to VA
            },
            'Nashville': {
                'places': random_geneator_pick_2(places)  # to KY
            },
            'Selmer': {
                'places': random_geneator_pick_2(places)  # starting from AL
            },
            'Memphis': {
                'places': random_geneator_pick_2(places)  # to Missouri
            }
        }
    },

    'South_Carolina': {
        'cities': {
            'Columbia': {
                'places': random_geneator_pick_2(places)  # starting from GA
            },
            'Florence': {
                'places': random_geneator_pick_2(places)  # to NC
            }
        },
    },

    'North_Carolina': {
        'cities': {
            'Fayetteville': {
                'places': random_geneator_pick_2(places)  # starting from SC
            },
            'Raleigh': {
                'places': random_geneator_pick_2(places)  # to VA
            }
        }
    },

    'Missouri': {
        'cities': {
            'Springfield': {
                'places': random_geneator_pick_2(places)  # starting from TN
            },
            'St_Louis': {
                'places': random_geneator_pick_2(places)  # to Illinois
            },
            'Kansas City': {
                'places': random_geneator_pick_2(places)  # to Iowa
            }
        }
    },

    'Illinois': {
        'cities': {
            'Champaign': {
                'places': random_geneator_pick_2(places)  # from Missouri
            },
            'Chicago': {
                'places': random_geneator_pick_2(places)  # to MI
            }

        }
    },

    'Iowa': {
        'cities': {
            'Des Moines': {
                'places': random_geneator_pick_2(places)  # from Missouri
            },
            'Mason_City': {
                'places': random_geneator_pick_2(places)  # to Minnesota
            }

        }
    },

    'Minnesota': {
        'cities': {
            'Minneapolis': {
                'places': random_geneator_pick_2(places)  # from Iowa
            },
            'International_Falls': {
                'places': random_geneator_pick_2(places)  # to Canada
            }
        }
    },

    'Michigan': {
        'cities': {
            'Detroit': {
                'places': random_geneator_pick_2(places)  # from XXXX to Canada
            },
            'Grand_Rapids': {
                'places': random_geneator_pick_2(places)  # from Chicago
            },
            'Port Huron': {
                'places': random_geneator_pick_2(places)  # from Grand_Rapid to Canada
            },
            'Ann_Arbor': {
                'places': random_geneator_pick_2(places)  # from Indiana
            },
            'Detroit-2': {
                'places': random_geneator_pick_2(places)  # from Ann_Arbor to Canada
            },
            'Detroit-3': {
                'places': random_geneator_pick_2(places)  # from Ohio to Canada
            }
        }
    },

    'Kentucky': {
        'cities': {
            'Bowling_Green': {
                'places': random_geneator_pick_2(places)  # from TN
            },
            'Lexington': {
                'places': random_geneator_pick_2(places)  # to Ohio
            },
            'Louisville': {
                'places': random_geneator_pick_2(places)  # to Indiana
            }
        }
    },

    'Indiana': {
        'cities': {
            'Indianapolis': {
                'places': random_geneator_pick_2(places)  # from KY
            },
            'Fort Wayne': {
                'places': random_geneator_pick_2(places)  # to MI
            }
        }
    },

    'Virginia': {
        'cities': {
            'Richmond': {
                'places': random_geneator_pick_2(places)  # starting from NC
            },
            'Fredericksburg': {
                'places': random_geneator_pick_2(places)  # to MD
            },
            'Charlottesville': {
                'places': random_geneator_pick_2(places)  # to WV-1
            },
            'Abingdon': {
                'places': random_geneator_pick_2(places)  # starting from TN
            },
            'Roanoke': {
                'places': random_geneator_pick_2(places)  # to WV-2
            }

        }
    },

    'Maryland': {
        'cities': {
            'Baltimore': {
                'places': random_geneator_pick_2(places)  # starting from VA
            },
            'Westminster': {
                'places': random_geneator_pick_2(places)  # to PA-1
            }
        }
    },

    'West_Virginia': {
        'cities': {
            'Green_Bank': {
                'places': random_geneator_pick_2(places)  # starting from VA-1
            },
            'Bridgeport': {
                'places': random_geneator_pick_2(places)  # to PA-2
            },
            'Lewisburg': {
                'places': random_geneator_pick_2(places)  # starting from VA-2
            },
            'Charleston': {
                'places': random_geneator_pick_2(places)  # to OH-1
            }
        }
    },

    'Pennsylvania': {
        'cities': {
            'Harrisburg': {
                'places': random_geneator_pick_2(places)  # starting from Maryland
            },
            'Mansfield': {
                'places': random_geneator_pick_2(places)  # from Harrisburg to NY-1
            },
            'Pittsburgh': {
                'places': random_geneator_pick_2(places)  # starting from WV
            },
            'Clarion': {
                'places': random_geneator_pick_2(places)  # from pittsburg to NY-2
            },
            'Erie': {
                'places': random_geneator_pick_2(places)  # from OH to NY-3
            }
        }
    },

    'New_York': {
        'cities': {
            'Elmira': {
                'places': random_geneator_pick_2(places)  # from PA-Mansfield
            },
            'Salamanca': {
                'places': random_geneator_pick_2(places)  # from PA-Clarion
            },
            'Buffalo-1': {
                'places': random_geneator_pick_2(places)  # from Elmira to Canada **
            },
            'Buffalo-2': {
                'places': random_geneator_pick_2(places)  # from Salamanca to Canada **
            },
            'Buffalo-3': {
                'places': random_geneator_pick_2(places)  # from PA-Erie
            }
        }
    },

    'Ohio': {
        'cities': {
            'Athens': {
                'places': random_geneator_pick_2(places)  # starting from WV
            },
            'Akron': {
                'places': random_geneator_pick_2(places)  # from Athens to PA
            },
            'Cincinnati': {
                'places': random_geneator_pick_2(places)  # starting from KY
            },
            'Toledo': {
                'places': random_geneator_pick_2(places)  # from Cincinnati to MI
            }
        }
    }

}
