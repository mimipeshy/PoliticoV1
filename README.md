# Politico       [![Build Status](https://travis-ci.org/mimipeshy/PoliticoV1.svg?branch=develop)](https://travis-ci.org/mimipeshy/PoliticoV1)   [![Maintainability](https://api.codeclimate.com/v1/badges/10436f3ef6f9d5bc5d88/maintainability)](https://codeclimate.com/github/mimipeshy/PoliticoV1/maintainability)  [![Coverage Status](https://coveralls.io/repos/github/mimipeshy/PoliticoV1/badge.svg?branch=develop)](https://coveralls.io/github/mimipeshy/PoliticoV1?branch=develop)

Politico enables citizens give their mandate to politicians running for different government offices
while building trust in the process through transparency.

## Getting Started

1) Clone the repository by doing: `git clone https://github.com/mimipeshy/PoliticoV1.git`

2) Create a virtual environment: `virtualenv env`

3) Activate the virtual environment: `source venv/bin/activate` on Linux/Mac  or `source venv/Scripts/activate` on windows.

4) Install the requirements : `pip install -r requirements.txt`


## Running tests
Use pytest to run: `pytest --cov=app` 

### Prerequisites
-   python 3.6
-   virtual environment


## Running it on machine
- Create a .env file to store your environment variables: `touch .venv`
- On terminal do: `source venv/bin/activate` on Linux/Mac  or `source venv/Scripts/activate` on windows
- Run the application: `python run.py`
- The api endpoints can be consumed using postman.

## Endpoints
| Endpoint                                | FUNCTIONALITY                      | API ENDPOINTS               |
| ----------------------------------------|:----------------------------------:|:--------------------------: |                   
| POST  /api/v1/party                     | CREATE political party             |"name", "hqAddress, "logoUrl |
| GET  /api/v1/party                      | GET ALL political parties          |                             |             
| GET  /api/v1/party/<int:id>             | GET ONE political party            |                             |               
| DELETE  /api/v1/party                   | DELETE ONE political party         |                             |              
| PATCH /api/v1/party/<int:id>            | UPDATE ONE political party         |                             |               
| POST  /api/v1/office                    | CREATE government office           |"name", "type"               |               
| GET  /api/v1/office/<int:id>            | GET ONE government office          |                             |              
| GET  /api/v1/office                     | GET ALL government offices         |                             |               

# Heroku host

https://politicov1.herokuapp.com

## Built With
* [Flask-Api](http://flask.pocoo.org/docs/1.0/api/) -  The web framework used
* [Pip](https://pypi.python.org/pypi/pip) -  Dependency Management

## Authors
* **Peris Ndanu** 

## License

This project is licensed under the MIT License