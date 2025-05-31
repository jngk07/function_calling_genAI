from dotenv import load_dotenv
import os
from openai import OpenAI

# Load .env
load_dotenv()

# Initialize client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# List models
models = client.models.list()

# Print all model IDs
print("Available models:")
for model in models.data:
    print(model.id)
