from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask,jsonify,request

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)

app = Flask(__name__)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

@app.route("/")
def home():
    return jsonify({
        "Message": "app v2 up and running successfully."
    })

@app.route("/reload",methods=["POST"])
def access():
    data = request.get_json()
    name = data.get("name", "dipto")
    server = data.get("server","server1")

    message = f"Reload {name} from server {server}"

    return jsonify({
        "Message": message
    })


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)