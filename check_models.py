from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Create a .env file with this code:

# OpenAI API Configuration
# OPENAI_API_KEY=""



# Get your OpenAI API key at https://platform.openai.com/api-keys and save it as OPENAI_API_KEY in your .env file.

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

for model in client.models.list():
    print(model.id)