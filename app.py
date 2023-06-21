from flask import Flask, jsonify
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("testflaskkk-firebase-adminsdk-7wuez-fc224aea6f.json")
firebase_admin.initialize_app(cred)


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/update-sensor/<sensor_value>')
def update_sensor(sensor_value):
    db = firestore.client()
    doc_ref = db.collection('waktusolat').document("sensor_value")
    new_data = {"value": sensor_value}
    doc_ref.set(new_data, merge=True)
    print("Sensor value updated to: {}".format(sensor_value))
    return jsonify({"status": "OK"})



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
