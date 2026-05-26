from flask import Flask, request, jsonify
import logging

import homeassistant_club_dashboard_api.__main__ as main
import homeassistant_club_dashboard_api.db as db
from homeassistant_club_dashboard_api.middleware import Middleware as auth

def checkAccess():
    try:
        isAuthorized = auth.validateAccessToken(request.authorization)
        if(isAuthorized):
            return "Success",200
        else:
            return {"message": "Unauthorized"},401
    except Exception as e:
        return {"Error": str(e)}, 501   
    
# need
def getDoors(ok_cloud_access_token, back_end_url, club_id, facility_id):
    try:
        isAuthorized = auth.validateAccessToken(request.authorization)

        if(isAuthorized):
            result = db.getDoors(ok_cloud_access_token, back_end_url, club_id, facility_id)
            response = result
            logging.info(response)
            logging.info(type(response))
            return response 
        else:
            response = {"message": "Unauthorized"}
            logging.info(response)
            return response, 401
    except Exception as e:
        return {"Error in fetinf doors from db.getDoors()": str(e)}, 501

# need
def getLights(ok_cloud_access_token,back_end_url, club_uuid, club_id, facility_id, integrated_club_string,integrated_club_type):
    try:
        integrated_club = integrated_club_string == 'true'
        isAuthorized = auth.validateAccessToken(request.authorization)

        if(isAuthorized):
            result = db.getLights(ok_cloud_access_token,back_end_url, club_uuid, club_id, facility_id, integrated_club,integrated_club_type)
            response = result
            print(response)
            print(type(response))
            return response
        else:
            response = {"message": "Unauthorized"}
            return response, 401

    except Exception as e:
        return {"Error": str(e)}, 501

def getConfig():
    try:
        isAuthorized = auth.validateAccessToken(request.authorization)

        if(isAuthorized):
            result = db.getConfiguration()
            response = result
            return response
        else:
            response = {"message": "Unauthorized"}
            return response, 401

    except Exception as e:
        return {"Error": str(e)}, 501

def updateConfig():
    try:
        isAuthorized = auth.validateAccessToken(request.authorization)

        if(isAuthorized):
            body = request.get_json(force=True)
            result = db.updateConfig(body.get('value'), body.get('key'))
            response = {"result": "Successfully configuration updated"}
            return response
        else:
            response = {"message": "Unauthorized"}
            return response, 401
        
    except Exception as e:
        return {"Error": str(e)}, 501



def addDoor():
    try:
        isAuthorized = auth.validateAccessToken(request.authorization)

        if(isAuthorized):
            body = request.get_json(force=True)
            result = db.addDoor(body.get('id'), body.get('door_id'),body.get('entity_id'), body.get('friendly_name'))
            response = {"result": "Door was created successfully"}

            # main.addDoorToHa(body.get('entity_id'),body.get('friendly_name'))

            return response 
        else:
            response = {"message": "Unauthorized"}
            return response, 401
        
    except Exception as e:
        return {"Error": str(e)}, 501

def deleteDoor():
    try:
        isAuthorized = auth.validateAccessToken(request.authorization)

        if(isAuthorized):
            body = request.get_json(force=True)
            # get door details with id
            door = db.getDoorById(body.get('id'))
            entity_id = door[2]

            try:
                main.deleteDoorFromHa(entity_id)
            except:
                logging.info("Door not found in HA")


            result = db.deleteDoor(body.get('id'))
            response = {"result": "Door was delete successfully"}


            return response
        else:
            response = {"message": "Unauthorized"}
            return response, 401
        
    except Exception as e:
        return {"Error": str(e)}, 501

def updateDoorId():
    try:
        isAuthorized = auth.validateAccessToken(request.authorization)

        if(isAuthorized):
            body = request.get_json(force=True)
            
            # get door details with id
            door = db.getDoorById(body.get('id'))
            logging.info('Get Doors with ID')
            logging.info(body.get('id'))
            logging.info(door)
            logging.info(door[2])


        
            # get current state
            try:
                door_details = main.getDoorStateByEntityId(door[2])
                state = "off" if door[2] == "" else door_details['state']
                logging.info(state)
            except:
                state = "off"
                logging.info("Door not found in HA")
            logging.info('Pervious door state')

            # (id, door_id, entity_id, friendly_name, autometic_mode)
            try:
                main.deleteDoorFromHa(door[2]) #token error here
            except:
                logging.info("Door not found in HA")

            # get friendly name from db
            name = door[3]
            logging.info('Pervious door entity deleted')

            # add new door to HA with new entity/door id
            new_entity_id = 'door'+body.get('door_id')
            main.addDoorToHa(new_entity_id,state,name)      
            logging.info('New door entity added')

            result = db.updateDoorId(body.get('id'), body.get('door_id'))
            response = {"result": "Successfully door ID updated"}
            # entiy_id = 'door'+body.get('door_id')
            # main.addDoorToHa(entiy_id)


            return response
        else:
            response = {"message": "Unauthorized"}
            return response, 401
        
    except Exception as e:
        return {"Error": str(e)}, 501

def updateDoorEntityId():
    try:
        isAuthorized = auth.validateAccessToken(request.authorization)

        if(isAuthorized):
            body = request.get_json(force=True)
            result = db.updateDoorEntityId(body.get('id'), body.get('entity_id'))
            response = {"result": "Successfully door entity ID updated"}
            return response
        else:
            response = {"message": "Unauthorized"}
            return response, 401
        
    except Exception as e:
        return {"Error": str(e)}, 501

def updateDoorName():
    try:
        isAuthorized = auth.validateAccessToken(request.authorization)

        if(isAuthorized):
            body = request.get_json(force=True)
            result = db.updateDoorName(body.get('id'), body.get('friendly_name'))

            door = db.getDoorById(body.get('id'))

            entity_id = door[2]
            name = body.get('friendly_name')
            door_details = main.getDoorStateByEntityId(entity_id)
            state = "off" if door[2] == "" else door_details['state']

            # update door in HA
            main.addDoorToHa(entity_id,state,name)      

            response = {"result": "Successfully door friendly name updated"}
            return response
        else:
            response = {"message": "Unauthorized"}
            return response, 401
        
    except Exception as e:
        return {"Error": str(e)}, 501

# need
def updateDoorMode(ok_cloud_access_token,back_end_url, club_id):
    try:
        isAuthorized = auth.validateAccessToken(request.authorization)

        if(isAuthorized):
            body = request.get_json(force=True)
            result = db.updateDoorMode(body.get('id'), body.get('automatic_mode'),ok_cloud_access_token,back_end_url, club_id)
            response = {"result": "Successfully door mode updated"}
            return response
        else:
            response = {"message": "Unauthorized"}
            return response, 401
        
    except Exception as e:
        return {"Error": str(e)}, 501

# need
def updateLightMode(ok_cloud_access_token,back_end_url, club_id):
    try:
        isAuthorized = auth.validateAccessToken(request.authorization)

        if(isAuthorized):
            body = request.get_json(force=True)
            result = db.updateLightMode(body.get('id'), body.get('automatic_mode'),ok_cloud_access_token,back_end_url, club_id)
            logging.info(f"updateLightMode: {result.status_code}")
            logging.info(result.json())
            response = {"result": "Successfully light mode updated"}
            return response
        else:
            response = {"message": "Unauthorized"}
            return response, 401
    except Exception as e:
        return {"Error": str(e)}, 501
    

def updateLightLimitedOption(ok_cloud_access_token, back_end_url, club_id):
    try:
        isAuthorized = auth.validateAccessToken(request.authorization)

        if isAuthorized:
            body = request.get_json(force=True)
            logging.info(f"Request body: {body}")
            result = db.updateLightLimitedOption(
                body.get('id'),
                body.get('limited_option'),
                ok_cloud_access_token,
                back_end_url,
                club_id
            )

            logging.info(f"updateLightLimitedOption: {result.status_code}")
            logging.info(result.json())
            response = {"result": "Successfully updated limited_option"}
            return response
        else:
            return {"message": "Unauthorized"}, 401

    except Exception as e:
        return {"Error": str(e)}, 501

    
def updateMinLightLevel(ok_cloud_access_token,back_end_url, club_id):
    try:
        isAuthorized = auth.validateAccessToken(request.authorization)

        if(isAuthorized):
            body = request.get_json(force=True)
            result = db.updateMinLightLevel(
                body.get('id'), 
                body.get('min_level'),
                ok_cloud_access_token,
                back_end_url, 
                club_id
            )
            logging.info(f"updateMinLightLevel: {result.status_code}")
            logging.info(result.json())
            response = {"result": "Successfully min light level updated"}
            return response
        else:
            response = {"message": "Unauthorized"}
            return response, 401
    except Exception as e:
        return {"Error": str(e)}, 501

def updateMaxLightLevel(ok_cloud_access_token,back_end_url, club_id):
    try:
        isAuthorized = auth.validateAccessToken(request.authorization)

        if(isAuthorized):
            body = request.get_json(force=True)
            result = db.updateMaxLightLevel(
                body.get('id'), 
                body.get('max_level'),
                ok_cloud_access_token,
                back_end_url, 
                club_id
            )
            logging.info(f"updateMaxLightLevel: {result.status_code}")
            logging.info(result.json())
            response = {"result": "Successfully max light level updated"}
            return response
        else:
            response = {"message": "Unauthorized"}
            return response, 401
    except Exception as e:
        return {"Error": str(e)}, 501