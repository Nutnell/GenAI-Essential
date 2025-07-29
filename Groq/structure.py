import os
from pydantic import BaseModel, Field
from typing import List
from groq import Groq
import instructor
import dotenv
dotenv.load_dotenv()

class Character(BaseModel):
    name: str
    fact: List[str] = Field(..., description="A list of facts about the subject")

client = Groq(
    api_key=os.environ.get('GROQ_API_KEY'),
)

# Change the mode here:
client = instructor.from_groq(client, mode=instructor.Mode.JSON)
# OR:
# client = instructor.from_groq(client, mode=instructor.Mode.JSON_SCHEMA)


resp: List[Character] = client.chat.completions.create(
    model="qwen/qwen3-32b",
    messages=[
        {
            "role": "user",
            "content": "Tell me about the company Tesla",
        }
    ],
    response_model=List[Character],
)

# Print using json.dumps for the list
import json
print(json.dumps([char.model_dump() for char in resp], indent=2))