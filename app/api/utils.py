import re

from flask import request, jsonify

from app.api.responses import Responses

from urllib.parse import urlparse


class Validations:

    @staticmethod
    def verify_political_details():
        """check that political party details are valid"""
        data = request.get_json()
        name = data['name'].strip()
        hqAddress = data['hqAddress'].strip()
        logoUrl = data['logoUrl'].strip()

        if len(name) == 0:
            return Responses.bad_request("Party Name cannot be empty"), 400
        if len(hqAddress) == 0:
            return Responses.bad_request("hqAddress name cannot be empty"), 400
        if len(logoUrl) == 0:
            return Responses.bad_request("LogoUrl cannot be empty"), 400

    @staticmethod
    def validate_characters():
        "this validates a party details"

        data = request.get_json()
        name = data['name'].strip()
        hqAddress = data['hqAddress'].strip()
        is_valid_name = r'[a-z]+'
        if len(name) < 6:
            return Responses.bad_request("Name should have more than 6 charcaters"), 404
        if len(hqAddress) < 6:
            return Responses.bad_request("hqAddress should have more than 6 charcaters"), 404
        if len(name) > 12:
            return Responses.bad_request("Name should have not more than 12 charcaters"), 404
        if len(hqAddress) > 12:
            return Responses.bad_request("hqAddress should have not more than 12 charcaters"), 404
        # if bool(re.match(name, is_valid_name)):
        #     return name
        # return Responses.bad_request("Name can only contain characters from A-Z"),404

    @staticmethod
    def validate_logo():
        """this validates logoUrl format"""
        data = request.get_json()
        url = urlparse(data['logoUrl'])
        if not url.scheme:
            return Responses.bad_request("incorrect format, url should start with the format http or https"), 403
        if not url.netloc:
            return Responses.bad_request("url should have a valid body format eg www.twitter.com"), 403
        if not url.path:
            return Responses.bad_request("url should have a path format of /pic.jpg"), 403

    @staticmethod
    def validate_strings(data):
        """ this ensures that all inputs are in the correct format"""
        if not isinstance(data['name'], str) or not isinstance(data['hqAddress'], str) or not isinstance(
                data['logoUrl'], str):
            return Responses.bad_request('Ensure that all inputs are strings'), 400

    @staticmethod
    def validate_json_inputs():
        """this check that json keys are not missing"""
        data = request.get_json()
        if not data:
            return Responses.bad_request("Empty inputs in Json"), 400
        if 'name' not in data:
            return Responses.bad_request("Name input is missing"), 400
        if 'hqAddress' not in data:
            return Responses.bad_request("hqAddress input is missing"), 400
        if 'logoUrl' not in data:
            return Responses.bad_request("logoUrl input is missing"), 400

    @staticmethod
    def validate_extra_fields(data):
        """this checks for extra keys in json format"""
        required_fields = ['name', 'hqAddress', 'logoUrl']
        if len(required_fields) < len(data.keys()):
            for key in data:
                if key not in required_fields:
                    return Responses.bad_request("{} is not a valid key".format(key)), 400


