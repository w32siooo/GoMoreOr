import copy
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('ServiceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

#Helper class to create a new ride instance. Could also be a JSON object.

#Program class.
class GoMore :
    def __init__(self):
        #List of rides, I use a list as my database to keep things simple. Otherwise a RDBMS should be used.
        self.lastRecord=[]

        #Add a new ride to the "database".
    def appendRide(self, args):
        self.newRide(*args)

    def newRide(self, from_city, to_city, from_date, number_of_seats):
        db.collection('rides').add({
            'from_city': from_city,
            'to_city': to_city,
            'from_date': from_date,
            'min_free_seats': number_of_seats,
        })

        #Search for a suitable ride given user input. Default values are provided.
    def findRide(self, from_city, to_city, from_date=0, to_date=0, min_free_seats=1):

        #Get the rides collection from our noSQL database.
        docs = db.collection(u'rides').stream()

        #Placeholder Array for avaiable Rides
        rides=[]

        #loop through the doc list and append it to our rides list.
        for doc in docs:
            rides.append([doc.to_dict().get('from_city'),doc.to_dict().get('to_city'),doc.to_dict().get('from_date'),doc.to_dict().get('min_free_seats')])

        #Output string, I use a string because python makes it easy to concatenate strings with +.
        output = ''
        for x in rides:
            #If there is no date specified, we skip comparing dates.
            if(from_date==0 and to_date == 0):
                if(x[0] == from_city and x[1] == to_city):
                    output = output +(f'{x[0]} {x[1]} {x[2]} {x[3]}')
            #If there is no to date specified, we skip comparing to_date's.
            elif (to_date ==0):
                if (x[1]==to_city and x[0]==from_city and x[2]==from_date):
                    output = output +(f'{x[0]} {x[1]} {x[2]} {x[3]}')
            #Otherwise we compare everything.
            else :
                if (x[1]==to_city and x[0]==from_city and x[2]>=from_date and int(x[3])>=int(min_free_seats)):
                    output = output +(f'{x[0]} {x[1]} {x[2]} {x[3]} ')
        return output

#Create a return-trip on date using the last created ride as a template.
    def createReturnTrip(self, date):
        #get last created ride for template
        docs = db.collection(u'rides').stream()
        rides=[]
        for doc in docs:
            rides.append([doc.to_dict().get('from_city'),doc.to_dict().get('to_city'),doc.to_dict().get('from_date'),doc.to_dict().get('min_free_seats')])
        tempRide = copy.deepcopy(rides[-1])
        self.newRide(tempRide[1],tempRide[0],date,tempRide[2])

#This is just the barebones command line program for user input.
if __name__ == '__main__':

    print("Welcome to GoMore.")
    myGoMore = GoMore()
    running = True
    while running:

        value = input("Create or Search for a ride:\n")
        if (value=='stop'):
            print('bye')
            running=False

        if (value.startswith("C")):
            args_list = value.split()
            args_list.pop(0)
            myGoMore.appendRide(args_list)

        if (value.startswith("S")):
            args_list = value.split()
            args_list.pop(0)
            print(myGoMore.findRide(*args_list))

        if (value.startswith("R")):
            args_list = value.split()
            args_list.pop(0)
            myGoMore.createReturnTrip(*args_list)
