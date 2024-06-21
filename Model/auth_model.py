import pymongo
from pymongo import MongoClient
from Model.mongo_connect import client
from Model.mongo_connect import ConcordiaEventManagementDB

# Create a collection
Users = ConcordiaEventManagementDB['Users']

def create_user(user):
    user = {
        "userName": user['userName'],
        "userEmail": user['userEmail'],
        "userPassword": user['userPassword'],
        "userPhoneNumber": user['userPhoneNumber']
    }
    # Insert a document into the collection
    Users.insert_one(user)

# Table 1 - Event Table (Each event has 1 or more organizers)
'''
- EventID
- EventName
- EventDescription
- EventLocation
- EventDate
- EventTime
'''

# Table 2 - Event Organizers:
'''
- EventOrganizerName
- EventOrganizerID
'''

# Table 3 - Event Attendents:
'''
- EventAttendentName
- EventAttendentID
'''

# Table 4 - Users (General Users of the Website)
'''
- UserName
- UserEmail
- UserPassword
- UserPhoneNumber
'''

# Table - Relationship Between Event and Event Organizers:
'''
- EventID
- EventOrganizerID
'''

# Table - Relationship between Event and Event Attendents:
'''
- EventID
- EventAttendentID
'''

# Table - Relationship Between Event Organizers and Event Attendents:
'''
- EventOrganizerID
- EventAttendentID
'''