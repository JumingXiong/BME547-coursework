from flask import Flask, request, jsonify

db ={}

app = Flask(__name__)

def add_patient_to_db(id, name, blood_type):
    new_patient = {
        "id":id,
        "name":name,
        "blood_type":blood_type,
        "test":[]
    }
    db[id] = new_patient
    print(db)

def add_test_to_db(id, test_name, test_value):


@app.route("/new_patient",methods = ["POST"])
def post_new_patient():
    in_data = request.get_json()
    answer, status_code =  new_patient_driver(in_data)
    return jsonify(answer), status_code



def new_patient_driver(in_data):
    validation = validate_input_data(in_data)
    if validation is not True:
        return validation, 400
    add_patient_to_db(in_data["id"],in_data["name"],in_data["blood_type"])
    return "patient successfully added", 200

def validate_input_data(in_data):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect type".format(key)
    return True


def validate_input_data_add_test(in_data):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    expected_keys = ["id", "test_name", "key_result"]
    expected_types = [int, str, int]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect type".format(key)
    return True


# @app.route("/add_test",methods = ["POST"])
# def post_new_patient():
#     in_data = request.get_json()
#     answer, status_code =  new_patient_driver(in_data)
#     return jsonify(answer), status_code

def does_patient_exist_in_db(id):
    if 


if __name__ == "__main__":
    app.run()