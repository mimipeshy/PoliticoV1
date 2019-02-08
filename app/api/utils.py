class Validations:

    @staticmethod
    def verify_political_details(party_name, logoUrl):
        """check that political party details are valid"""
        if len(party_name.strip()) == 0:
            return {"message": "Party name cannot be empty"}, 200
        else:
            if len(logoUrl.strip()) == 0:
                return {"message": "LogoUrl cannot be empty"}, 200
