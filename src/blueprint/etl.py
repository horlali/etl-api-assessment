from os.path import join
from flask import Blueprint, jsonify, request
from werkzeug.utils import secure_filename
from src.config.settings import UPLOAD_FOLDER
from src.models.database import Etl, Data
from src.services.etl_process import ExtractTransformLoad
from src.utils.helpers import allowed_file


etl_bp = Blueprint(name="main",import_name=__name__)

@etl_bp.route("/upload-csv", methods=["POST"])
def upload_csv():

    if "csv_file" not in request.files:
        return jsonify({"Error":"KeyError [csv_file]"}), 400
    
    csv_files = request.files.getlist("csv_file")

    for csv in csv_files:
        if csv.filename == "":
            return jsonify({"Error": "file not selected"}), 400

    for csv in csv_files:
        if not allowed_file(csv.filename):
            return jsonify({"Error":"Invalid file mime-type, please upload a csv file"}), 400

        csv_file = join(UPLOAD_FOLDER, secure_filename(csv.filename))
        csv.save(csv_file)

        etl = ExtractTransformLoad(csv_file=csv_file)

        data = Etl(
            file_name = csv.filename,
            file_size = etl.file_size,
            number_of_rows = etl.number_of_rows,
            number_of_columns = etl.number_of_columns,
            data = Data(content = etl.content)
        )
        data.save()

    
    resp = {"status": "success","detail": "ETL Successfully","data": data.to_json()}

    return jsonify(resp)




