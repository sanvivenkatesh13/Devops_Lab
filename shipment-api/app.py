from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/shipments/<shipment_id>', methods=['GET'])
def get_shipment(shipment_id):

    shipment = {
        "shipment_id": shipment_id,
        "customer": "Rahul",
        "source": "Bangalore",
        "destination": "Mumbai",
        "status": "Dispatched",
        "served_by": os.getenv("POD_NAME", "local")
    }

    return jsonify(shipment)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
