import os
from werkzeug.utils import secure_filename
import boto3, botocore

from src.config.settings import S3_KEY, S3_SECRET


ALLOWED_EXTENSIONS = {"csv"}

def allowed_file(filename):
        return "." in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




s3 = boto3.client(
    "s3",
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET
)


def upload_file_to_s3(file, acl="public-read"):
    filename = secure_filename(file.filename)
    try:
        s3.upload_fileobj(
            file,
            os.getenv("AWS_BUCKET_NAME"),
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e
    
    return file.filename