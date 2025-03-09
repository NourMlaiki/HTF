from google import genai

client = genai.Client(api_key="AIzaSyCbGxGVYLoq1_zl8XJ7R0N7TAvEeMCh_H0")

#response = client.models.generate_content(
#model="gemini-2.0-flash",  # Or another model
  #  contents="Name the Capitals of African Country")
#print(response.text)

from flask import Flask, request, send_file, jsonify


app = Flask(__name__)

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
    # ✅ Check if an image is uploaded
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    image_path = "temp.jpg"  # ✅ Temporary file to store uploaded image
    file.save(image_path)

    try:
        # ✅ Read image data
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()

        # ✅ Send image to Gemini for analysis
        response = client.models.generate_content(
            model="gemini-1.5-flash",  # ✅ Use the correct model
            contents=[
                {"role": "user", "parts": [
                    {"text": "Analyze this product image and determine its likelihood of being returned in a store. Provide recommendations and assign a Return Score."},
                    {"inline_data": {"mime_type": "image/jpeg", "data": image_data}}
                ]}
            ]
        )

        # ✅ Return Gemini’s response as JSON
        return jsonify({"analysis": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
