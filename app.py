import subprocess
from flask import Flask, jsonify, request
import json
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)


@app.route("/run-tests")
def run_tests():
    module_name = request.args.get('module', type=str)
    scripts_path = f"{os.environ.get('HOME')}/AutoTest/test/TestScripts/{module_name}.sh"
    test_process = subprocess.Popen(["/bin/bash", scripts_path])
    return 'Executing...'

    
@app.route("/get-test-data", methods=["POST"])
def get_test_data():
    module_names = request.json.get('moduleParams', [])

    json_data = []
    for module_name in module_names:
        file_path =f"{os.environ.get('HOME')}/AutoTest/client/public/{module_name}.json"
        with open(file_path, "r") as f:
            json_data.append(json.load(f))
    return jsonify(json_data)
