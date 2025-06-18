# Pizza Restaurant API

SIMPLE SETUP 

1. Install dependencies

pip install flask flask-sqlalchemy flask-migrate

2.Initialize database 

export FLASK_APP=server/app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python server/seed.py

3.Run the server
flask run

PROJECT STRUCTURE
pizza-code-challenge/
├── .venv/ # Virtual environment
├── instance/ # Database instance
├── migrations/ # Database migrations
│
├── server/ # Main application
│ ├── controllers/ # Route handlers
│ │ ├── pizza_controller.py
│ │ ├── restaurant_controller.py
│ │ └── restaurant_pizza_controller.py
│ │
│ ├── models/ # Database models
│ │ ├── pizza.py
│ │ ├── restaurant.py
│ │ └── restaurant_pizza.py
│ │
│ ├── init.py # App initialization
│ ├── app.py # Main app file
│ └── config.py # Configuration
│
├── challenge-1-pizzas.postman_collection.json # Postman tests
├── requirements.txt # Python dependencies
├── seed.py # Database seeder
└── README.md # This file

API ENDPOINTS
Endpoint	        Method	 Description
/restaurants	    GET      List all restaurants
/restaurants/<id>	GET	     Get restaurant details
/restaurants/<id>	DELETE	 Delete restaurant
/pizzas	            GET	     List all pizzas
/restaurant_pizzas	POST	 Create pizza association
