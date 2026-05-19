import os
from dotenv import load_dotenv 
from datetime import timedelta

load_dotenv()

class Config:

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USERNAME')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}/"
        f"{os.getenv('DB_NAME')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_SECRET_KEY = "myjwtsecretkey" 
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)