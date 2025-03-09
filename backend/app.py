from google import genai

client = genai.Client(api_key="AIzaSyCbGxGVYLoq1_zl8XJ7R0N7TAvEeMCh_H0")

#response = client.models.generate_content(
#model="gemini-2.0-flash",  # Or another model
  #  contents="Name the Capitals of African Country")
#print(response.text)

from flask import Flask, request, send_file, jsonify
from flask_cors import CORS  # 🚀 Allow React to call Flask
import os

# ✅ Initialize Flask app
app = Flask(__name__, static_folder="build", static_url_path="/")
CORS(app)  # ✅ Enables communication with React

### 📌 Serve React Frontend ###
@app.route('/')
@app.route('/<path:path>')
def serve_react():
    return send_file(os.path.join(app.static_folder, "index.html"))





CORS(app) 
### 📌 PAGE 1: DOWNLOAD HISTORICAL DATA ###
@app.route('/download/data', methods=['GET'])
def download_data():
    return send_file('historical_data.xlsx', as_attachment=True)

### 📌 PAGE 2: ANALYZE DATA WITH GEMINI ###
@app.route('/analyze/data', methods=['POST'])
def analyze_data():
    data = request.json.get("data", "")
    response = client.models.generate_content(f"Summarize this data: {data}")
    return jsonify({"summary": response.text})

### 📌 PAGE 3: DOWNLOAD IMAGE ###
@app.route('/download/image', methods=['GET'])
def download_image():
    return send_file('sample_photo.jpg', as_attachment=True)

### 📌 PAGE 4: IMAGE ANALYSIS WITH GEMINI AI ###
@app.route('/analyze/image', methods=['POST'])
def analyze_image():
    file = request.files['image']
    image_path = "temp.jpg"
    file.save(image_path)


    response = client.models.generate_content([
        "Analyze this product image and determine its likelihood of being returned in a store. Provide recommendations and Assign a Return Score based on how likely it is to be returned.", 
        open(image_path, "rb")
    ])
    
    return jsonify({"analysis": response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # 🌎 Make Flask accessible on network
