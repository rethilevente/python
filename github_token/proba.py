import os
from dotenv import load_dotenv

load_dotenv()
n = os.environ.get("name")
print(n)

