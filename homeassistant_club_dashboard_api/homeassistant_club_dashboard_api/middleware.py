from flask import Flask, request, abort
import requests
import logging

class Middleware():
    def validateAccessToken(token):
        logging.info('Token-------------')
        logging.info(token)
        logging.info('Token-------------')
        try:
            url = "http://homeassistant.local:8123/api/"
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": str(token)
            }
            
            response = requests.get(url, headers=headers)
            print(response)

            if response.status_code == 200:
                return True

            else:
                return False

        except Exception as e:
            return {"Faild to validate access token": str(e)}, 401
