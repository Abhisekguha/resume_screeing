from bardapi import Bard
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("BARD_API_KEY")

bard = Bard(token = token)

result = bard.get_answer("tell me a joke")
print(result)