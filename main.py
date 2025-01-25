from dotenv import load_dotenv
import os
load_dotenv()

username = os.getenv("EMAIL")
password = os.getenv("PASSWORD")