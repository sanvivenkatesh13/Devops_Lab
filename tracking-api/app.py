
from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

SHIPMENT_SERVICE_URL = os.getenv(
    "SHIPMENT_SERVICE_URL",
    "http://localhost:5001"
)

@app.route('/tracking/<shipment_id>', methods=['GET'])
def get_tracking(shipment_id):

    try:
        response = requests.get(
            f"{SHIPMENT_SERVICE_URL}/shipments/{shipment_id}",
            timeout=5
        )

        response.raise_for_status()
        shipment_data = response.json()

        tracking = {
            "tracking_id": "TRK-" + shipment_id,
            "shipment_id": shipment_id,
            "current_location": "Hyderabad",
            "delivery_status": "In Transit",
            "estimated_delivery": "Tomorrow",
            "shipment_details": shipment_data,
            "served_by": os.getenv("POD_NAME", "local")
        }

        return jsonify(tracking)

    except requests.RequestException as error:
        return jsonify({
            "error": "Unable to communicate with Shipment API",
            "details": str(error)
        }), 502

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
