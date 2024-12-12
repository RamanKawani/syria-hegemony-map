from flask import Flask, jsonify, render_template
from routes.mapRoutes import map_routes
app = Flask(__name__)

# Registering Routes
app.register_blueprint(map_routes)

@app.route('/')
def index():
    return render_template('index.html')  # Optionally, render an HTML page

if __name__ == '__main__':
    app.run(debug=True)
