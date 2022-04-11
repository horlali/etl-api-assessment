from os import environ

JSON_SORT_KEYS = False
SECRET_KEY = environ.get("SECRET_KEY")
UPLOAD_FOLDER = fr'{environ.get("UPLOAD_FOLDER")}'

DB_USER = environ.get("DB_USER")
DB_NAME = environ.get('DB_NAME')
DB_PASSWORD = environ.get('DB_PASSWORD')
MONGO_URI = f"mongodb+srv://{DB_USER}:{DB_NAME}@cluster0.oatfb.mongodb.net/{DB_PASSWORD}?retryWrites = true&w = majority"

S3_BUCKET = "S3_LOCATION"
S3_KEY = "AWS_ACCESS_KEY"
S3_SECRET = "AWS_ACCESS_SECRET"
S3_LOCATION = f"http://{S3_BUCKET}.s3.amazonaws.com/"

