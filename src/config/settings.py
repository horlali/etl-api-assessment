from os import environ

JSON_SORT_KEYS = False
SECRET_KEY = environ.get("SECRET_KEY")
DB_NAME = environ.get('DATABASE_NAME')
DB_PASSWORD = environ.get('MONGO_PASSWORD')
MONGO_URI = f"mongodb+srv://horlali:{DB_NAME}@cluster0.oatfb.mongodb.net/{DB_PASSWORD}?retryWrites = true&w = majority"
UPLOAD_FOLDER = r"C:\Users\horlali\Desktop\superfuild\DATA"
S3_BUCKET = "S3_LOCATION"
S3_KEY = "AWS_ACCESS_KEY"
S3_SECRET = "AWS_ACCESS_SECRET"
S3_LOCATION = f"http://{S3_BUCKET}.s3.amazonaws.com/"

