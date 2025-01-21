from dotenv import load_dotenv
import os

load_dotenv()

class Auth0Config:
    AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
    API_IDENTIFIER = os.getenv("API_IDENTIFIER")

class AppConfig:
    APP_NAME = os.getenv("APP_NAME", "SyntaxSentinel")
    PORT = os.getenv("PORT", 5000)
    DEBUG = os.getenv("DEBUG", False)