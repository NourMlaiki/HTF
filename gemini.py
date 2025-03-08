from google import genai

client = genai.Client(api_key="AIzaSyCbGxGVYLoq1_zl8XJ7R0N7TAvEeMCh_H0")

response = client.models.generate_content(
    model="gemini-2.0-flash",  # Or another model
    contents="Name the Capitals of African Country"
)
print(response.text)