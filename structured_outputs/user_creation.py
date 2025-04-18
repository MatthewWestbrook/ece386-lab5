'''Passes a personal intro statement to an LLM.
The LLM produces valid JSON that could be ingested into a database to create a new user.

Modified from https://ollama.com/blog/structured-outputs
'''
from ollama import chat
from pydantic import BaseModel
import sys

class User(BaseModel):
 name: str
 age: int
 favorite_color: str | None
 favorite_sport: str | None

if len(sys.argv) < 2:
    print("Error, did not input content and you need to")
    sys.exit(1)

user_input = sys.argv[1]

class UserList(BaseModel):
 users: list[User]
response = chat(
 messages=[
   {
     'role': 'system',
     'content': 'You are trying to find out a lot of information about someone and you will store that as in JSON. You need to fill the fields: name, age, favorite_color, and favorite_sport'
   },
   {
     'role': 'user',
     'content': user_input,
   }
 ],
 model='gemma3:1b',
 format=UserList.model_json_schema(),
)
users = UserList.model_validate_json(response.message.content)
print(users)