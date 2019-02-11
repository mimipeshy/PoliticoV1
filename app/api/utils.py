from urllib.parse import urlparse

from flask import jsonify


class Validations:

    @staticmethod
    def verify_political_details(party_name, logoUrl):
        """check that political party details are valid"""
        if len(party_name.strip()) == 0:
            return jsonify({"message": "Party name cannot be empty"}), 200
        else:
            if len(logoUrl.strip()) == 0:
                return jsonify({"message": "LogoUrl cannot be empty"}), 200

class ValidateLogo:
    @staticmethod
    def validate_logo(logoUrl):
        """this validates logoUrl format"""
        url = urlparse(logoUrl)
        if not url.scheme:
            return jsonify({"msg": "incorrect format, url should start with the format http or https"}), 403
        if not url.netloc:
            return jsonify({"msg": "url should have a valid body format eg www.twitter.com"}), 403
        if not url.path:
            return jsonify({"msg": "url should have a path format of /pic.jpg"}), 403
