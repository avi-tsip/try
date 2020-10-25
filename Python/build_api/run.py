from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

# Initializing flask object
app = Flask(__name__)
api = Api(app)

# Parsing the put requests for the employee class
employee_put_args = reqparse.RequestParser()
employee_put_args.add_argument('age', type=int, help='enter the age of the employee', required=True)
employee_put_args.add_argument('firstName', type=str, help='enter the first name of the employee', required=True)
employee_put_args.add_argument('lastName', type=str, help='enter the last name of the employee', required=True)
employee_put_args.add_argument('title', type=str, help='enter the title of the employee', required=True)

# Creating an employee dict
employee = {}

# Handle bad get request
def abort_if_employee_doesnt_exist(employee_id):
    if employee_id not in employee:
        abort(404, message=f"employee number {employee_id} doesn't exist")

def abort_if_employee_exist(employee_id):
    if employee_id in employee:
        abort(409, message=f"employee number {employee_id} already exist")

# Basic api get request
class HealthCheck(Resource):

    def get(self):
        return {"version": '2020.02.02'}

class Employee(Resource):

    # Api request with params
    # def get(self, name, id):
    #     return {"name": name, "id": id}

    def get(self, employee_id):
        abort_if_employee_doesnt_exist(employee_id)
        return employee[employee_id]

    def post(self, employee_id):
        abort_if_employee_exist(employee_id)
        args = employee_put_args.parse_args()
        employee[employee_id] = args
        return employee[employee_id], 201

    def delet(self, employee_id):
        abort_if_employee_doesnt_exist(employee_id)
        del employee[employee_id]
        return '', 204

api.add_resource(HealthCheck, "/health")
api.add_resource(Employee, '/employee/<int:employee_id>')

# Part of the example of the api request with params
# api.add_resource(Employee, '/employee/<string:name>/<int:id>')

if __name__ == "__main__":
    app.run(port="80", debug=True)