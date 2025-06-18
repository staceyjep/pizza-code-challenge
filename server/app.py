from server import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def home():
    return {
        "message": "Pizza Restaurant API",
        "endpoints": {
            "restaurants": "/restaurants",
            "pizzas": "/pizzas"
        }
    }