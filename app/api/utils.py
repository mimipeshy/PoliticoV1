from urllib.parse import urlparse
from app.api.responses import Responses
from flask import jsonify


class Validations:

    @staticmethod
    def verify_political_details(name,hqAddress, logoUrl):
        """check that political party details are valid"""
        if len(name.strip()) == 0:
            return Responses.bad_request("Party Name cannot be empty"),400
        if len(hqAddress.strip()) == 0:
            return Responses.bad_request("hqAddress name cannot be empty"), 400
        else:
            if len(logoUrl.strip()) == 0:
                return Responses.bad_request("LogoUrl cannot be empty"), 400

