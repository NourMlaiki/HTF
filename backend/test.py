from google import genai

# ✅ Replace with your actual API key
client = genai.Client(api_key="AIzaSyCbGxGVYLoq1_zl8XJ7R0N7TAvEeMCh_H0")



# ✅ Path to the image you want to analyze
image_path = "sample_photo.jpg"  # Make sure this file is in the same directory as this script


try:
    # ✅ Open and read the image file
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    # ✅ Use a supported vision model
    response = client.models.generate_content(
        model="gemini-1.5-flash",  # Use the correct model
        contents=[
            {"role": "user", "parts": [
                {"text": "Analyze this product image and determine its likelihood of being returned in a store. Provide recommendations and assign a Return Score."},
                {"inline_data": {"mime_type": "image/jpeg", "data": image_data}}
            ]}
        ]
    )

    # ✅ Print Gemini's analysis response
    print("✅ Gemini Image Analysis Response:", response.text)

except Exception as e:
    print("❌ Gemini API Error:", str(e))

