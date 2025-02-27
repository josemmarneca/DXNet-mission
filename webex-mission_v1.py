import json
import sys
import requests

#MISSION: FILL IN THE REQUESTED DETAILS
ACCESS_TOKEN = "" #Replace None with your access token between quotes.
BOT_ID = ""  #Replace   with your Bot is between quotes.


#sets the header to be used for authentication and data format to be sent.
def getWebexTeamsHeader():
    accessToken_hdr = 'Bearer ' + ACCESS_TOKEN
    webex_teams_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
    return (webex_teams_header)


#check if the room already exists. If so return the space id
def findRoom(headers, room_name):
    roomId=None
    uri = 'https://api.ciscospark.com/v1/rooms'
    resp = requests.get(uri, headers=headers)
    resp = resp.json()
    print('resp', resp)
    for room in resp["items"]:
        if room["title"] == room_name:
            print()
            print("findRoom JSON: ", room)

            roomId=room['id']
            break
    return(roomId)

# checks if the room already exists and if true returns that room ID. If not creates a new room and returns the space id.
def createRoom(headers, room_name):
    roomId=findRoom(headers, room_name)
    if roomId==None:
        roomInfo = {"title":room_name}
        uri = 'https://api.ciscospark.com/v1/rooms'
        resp = requests.post(uri, json=roomInfo, headers=headers)
        var = resp.json()
        print()
        print("createRoom JSON: ", var)
        print("createRoom JSON: ", var['id'])

        roomId=var['id']
    return(roomId)

# adds a new member to the space. Member e-mail is test@test.com
def addDxnetBot(headers, roomId):
    member = {"roomId":roomId,"personEmail": "dxnet-labs@webex.bot", "isModerator": False}
    uri = 'https://api.ciscospark.com/v1/memberships'
    resp = requests.post(uri, json=member, headers=headers)
    resp_json = resp.json()
    print("addMembers JSON: ", resp_json)
    return resp_json

# posts a message to the space
def sendMsgToPerson(headers, personId, message):
    message = {"toPersonId":personId,"text":message}
    uri = 'https://api.ciscospark.com/v1/messages'
    resp = requests.post(uri, json=message, headers=headers)
    print()
    print("postMsg JSON: ", resp.json())

# posts a message to the space
def sendMsgToRoom(headers, roomId, message):
        message = {"roomId": roomId, "text": message}
        uri = 'https://api.ciscospark.com/v1/messages'
        resp = requests.post(uri, json=message, headers=headers)
        resp_json = resp.json()
        print()
        print("sendMsgToRoom JSON: ", resp_json)
        return resp_json

def getMyOwnDetails(headers):
    uri = 'https://api.ciscospark.com/v1/people/me'
    resp = requests.get(uri, headers=headers)
    resp_json =  resp.json()
    print("getMyOwnDetails JSON: ", resp_json)
    return resp_json

def getPersonDetails(headers, personId):
    uri = 'https://api.ciscospark.com/v1/people/' + personId
    resp = requests.get(uri, headers=headers)
    resp_json =  resp.json()
    print("getMyOwnDetails JSON: ", resp_json)
    return resp_json

def getDirectMessages(headers, personId):
    uri = 'https://api.ciscospark.com/v1/messages/direct'
    queryParams = {'personId': personId}

    resp = requests.get(uri, headers=headers, params=queryParams)
    resp_json = resp.json()
    print("getMyOwnDetails JSON: ", resp_json)
    return resp_json

# MISSION: WRITE CODE TO RETRIEVE AND DISPLAY DETAILS ABOUT THE ROOM.
def getRoomInfo(headers, roomId):
    print("In function getRoomInfo")
    #MISSION: Replace None in the URI variable with the Webex Teams REST API call
    uri = None
    if uri == None:
        sys.exit("Please add the URI call to get room details. See the Webex Teams API Ref Guide")
    resp = requests.get(uri, headers=headers)
    print("Room Info: ",resp.text)
    resp = resp.json()

    print(resp)

    # MISSION: WRITE CODE TO RETRIEVE AND DISPLAY DETAILS ABOUT THE ROOM.

def postUserInMainRoomEvent(email):
    message = {"email": email}
    uri = 'https://dxnet-webex-api.herokuapp.com/postUserInRoom'
    resp = requests.post(uri, json=message)
    resp_json = resp.json()
    print()
    print("sendMsgToRoom JSON: ", resp_json)
    return resp_json


if __name__ == '__main__':
    # TODO: Pre requirements and set the ACCESS_TOKEN see(https://developer.webex.com/docs/api/getting-started) in right panel "Accounts and Authentication" see Your Personal Access Token
    if ACCESS_TOKEN==None :
        sys.exit("Please check that variables ACCESS_TOKEN, have values assigned.")

    #TODO: Add user in main room event with "your email" from webex account and save ROOM_ID response

    #TODO: ASK BOT OW TO WIN (send message to person with your bot id (BOT_ID)
    
    message = 'bot, can you give me the code to win?'
    #TODO: GO TO YOUR WEBEX APP. IN A CONVERSATION WITH THE DXNET-LABS 'BOT' COPY THE WINNER CODE

    #TODO: IN WEBEX APP GO TO MAIN ROOM EVENT (DXNET Jornadas Informática) and paste the winner code.

