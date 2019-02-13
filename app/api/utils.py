from app.api.responses import Responses


class Validations:

    @staticmethod
    def verify_political_details(name, hqAddress, logoUrl):
        """check that political party details are valid"""
        if len(name.strip()) == 0:
            return Responses.bad_request("Party Name cannot be empty"), 400
        if len(hqAddress.strip()) == 0:
            return Responses.bad_request("hqAddress name cannot be empty"), 400
        else:
            if len(logoUrl.strip()) == 0:
                return Responses.bad_request("LogoUrl cannot be empty"), 400

    @staticmethod
    def validate_strings(input):
        if isinstance(input, str):
            return Responses.bad_request("Only Strings are allowed for this method"), 400
