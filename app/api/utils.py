class Validations:

    @staticmethod
    def verify_political_details(party_name, location, description):
        """check that political party details are valid"""
        if len(party_name.strip()) == 0:
            return {"message": "Party name cannot be empty"}, 200
        else:
            if len(location.strip()) == 0:
                return {"message": "Location cannot be empty"}, 200
            else:
                if len(description.strip()) == 0:
                    return {"message": "Please enter a description"}, 200
