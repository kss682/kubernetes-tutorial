import os
from flask import  jsonify, request, Flask  
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("db_root_password")
app.config["MYSQL_DATABASE_DB"] = os.getenv("db_name")
app.config["MYSQL_DATABASE_HOST"] = os.getenv("MYSQL_SERVICE_PORT").split(":")[1].strip("//")
app.config["MYSQL_DATABASE_PORT"] = int(os.getenv("MYSQL_SERVICE_PORT").split(":")[2])
mysql.init_app(app)


@app.route("/employee", methods=["GET"])
def get_employee():
    try:
        data_list = []
        connection = mysql.connect()
        cursor = connection.cursor()
        cursor.execute("select * from employee")
        for i in cursor.fetchall():
            data_list.append(
                {
                    "id": i[0],
                    "name": i[1],
                    "role": i[2]
                }
            )
        resp = jsonify(data_list)
        resp.status_code = 200
        return resp
    except Exception as e:
        return e


@app.route("/employee/add", methods=["POST"])
def add_employee():
    json = request.json
    id = json["id"]
    name = json["name"]
    role = json["role"]
    try:
        if request.method == "POST" and (id is not None or name is not None or role is not None):
            query = "insert into employee values (%s, %s, %s)"
            data = (id, name, role)

            connection = mysql.connect()
            cursor = connection.cursor()
            cursor.execute(query, data)
            connection.commit()
            cursor.close()
            connection.close()
            response = jsonify("Employee added successfully")
            response.status_code = 200
            return response
        else:
            response = jsonify("Invalid request method or empty fields in json")
            response.status_code = 401
            return response
    except Exception as e:
        response = jsonify(e)
        response.status_code = 500
        return response


@app.route("/employee/<id>", methods=["GET"])
def get_employee_by_id(id):
    try:
        connection = mysql.connect()
        cursor = connection.cursor()
        cursor.execute("select * from employee where id=%s", id)
        data = cursor.fetchone()
        response = jsonify({
            "id": data[0],
            "name": data[1],
            "role": data[2]
        })
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify(str(e))
        response.status_code = 400
        return response


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)