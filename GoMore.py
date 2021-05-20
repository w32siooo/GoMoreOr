import copy

#Helper class to create a new ride instance. Could also be a JSON object.
class newRide:
    def __init__(self, from_city, to_city, from_date, number_of_seats):
        self.from_city = from_city
        self.to_city = to_city
        self.from_date = from_date
        self.number_of_seats = number_of_seats

#Program class.
class GoMore :
    def __init__(self):
        #List of rides, I use a list as my database to keep things simple. Otherwise a RDBMS should be used.
        self.rides=[]

        #Add a new ride to the "database".
    def appendRide(self, args):
        self.rides.append(newRide(*args))
        return len(self.rides)

        #Search for a suitable ride given user input. Default values are provided.
    def findRide(self, from_city, to_city, from_date=0, to_date=0, min_free_seats=1):
        #Output string, I use a string because python makes it easy to concatenate strings with +.
        output = ''

        #Loop through our "database" only once to keep things efficient.
        for x in self.rides:
            #If there is no date specified, we skip comparing dates.
            if(from_date==0 and to_date == 0):
                if(x.from_city == from_city and x.to_city == to_city):
                    output = output +(f'{x.from_city} {x.to_city} {x.from_date} {x.number_of_seats}')
            #If there is no to date specified, we skip comparing to_date's.
            elif (to_date ==0):
                if (x.to_city==to_city and x.from_city==from_city and x.from_date==from_date):
                    output = output +(f'{x.from_city} {x.to_city} {x.from_date} {x.number_of_seats}')
            #Otherwise we compare everything.
            else :
                if (x.to_city==to_city and x.from_city==from_city and x.from_date>=from_date and int(x.number_of_seats)>=int(min_free_seats)):
                    output = output +(f'{x.from_city} {x.to_city} {x.from_date} {x.number_of_seats} ')
        return output

#Create a return-trip on date using the last created ride as a template.
    def createReturnTrip(self, date):
        #get last created ride for template
        tempRide = copy.deepcopy(self.rides[-1])

        #Use the append function to create a return ride, by switching the from city and the to city, and applying the new date from the function argument.
        self.appendRide([tempRide.to_city,tempRide.from_city,date,tempRide.number_of_seats])
        return len(self.rides)

#This is just the barebones command line program for user input.
if __name__ == '__main__':

    print("Welcome to GoMore.")
    myGoMore = GoMore()
    running = True
    while running:

        value = input("Please enter a string:\n")
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