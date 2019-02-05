# Politico       [![Build Status](https://travis-ci.org/mimipeshy/PoliticoV1.svg?branch=develop)](https://travis-ci.org/mimipeshy/PoliticoV1)   [![Maintainability](https://api.codeclimate.com/v1/badges/10436f3ef6f9d5bc5d88/maintainability)](https://codeclimate.com/github/mimipeshy/PoliticoV1/maintainability)

Politico enables citizens give their mandate to politicians running for different government offices
while building trust in the process through transparency.

## Getting Started

1) Clone the repository by doing: `git clone https://github.com/mimipeshy/PoliticoV1.git`

2)Git checkout develop

3) Create a virtual environment: `virtualenv env`

4) Activate the virtual environment: `source venv/bin/activate` on Linux/Mac  or `source venv/Scripts/activate` on windows.

5) Install the requirements : `pip install -r requirements.txt`


## Running tests
Use pytest to run: `pytest --cov=app` 

### Prerequisites
-   python 3.6
-   virtual environment


## Running it on machine
- Create a .env file to store your environment variables: `touch .venv`
- In the `.venv` file add this line: `export SECRET=<your-secret-key-here`
- On terminal do: `source .venv`
- Run the application: `python run`
- The api endpoints can be consumed using postman.

## Endpoints
| Endpoint                                   | FUNCTIONALITY                      |
| ----------------------------------------   |:----------------------------------:|
| POST  /api/v1/party                        | CREATE political party             |


## Built With
* [Flask-Api](http://flask.pocoo.org/docs/1.0/api/) -  The web framework used
* [Pip](https://pypi.python.org/pypi/pip) -  Dependency Management

## Authors
* **Peris Ndanu** 

## License

This project is licensed under the MIT License