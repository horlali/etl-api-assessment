from flask import Flask, jsonify
from src.models.database import db
from src.blueprint.etl import etl_bp



def create_app(config_object="src.config.settings"):

    api = Flask(__name__)
    api.config.from_object(config_object)
    db.init_app(api)

    api.register_blueprint(blueprint=etl_bp, url_prefix = "/api/v1")

    @api.get("/")
    def welcome():
        return jsonify({"detail":"Hello World, Welcome Here"})


    @api.errorhandler(404)
    def handle_404(e):
        return jsonify({"error": "Not Found"}), 404

    
    @api.errorhandler(500)
    def hande_500(e):
        return jsonify({"error": "I'm on a coffee break, I will comeback right quick"})

    return api


