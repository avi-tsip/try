from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

# Initializing flask object
app = Flask(__name__)
api = Api(app)

# Creating a DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
db = SQLAlchemy(app)

# Creating the model
class EmployeeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    title = db.Column(db.String(100))

    def __repr__(self):
        return f'Video (first name = {firstName}, last name = {lastName}, age = {age}, title = {title})'

# Create the db once
# db.create_all()

# Parsing the put requests for the employee class
employee_put_args = reqparse.RequestParser()
employee_put_args.add_argument('age', type=int, help='enter the age of the employee', required=True)
employee_put_args.add_argument('firstName', type=str, help='enter the first name of the employee', required=True)
employee_put_args.add_argument('lastName', type=str, help='enter the last name of the employee', required=True)
employee_put_args.add_argument('title', type=str, help='enter the title of the employee', required=True)

# Parsing the patch requests for the employee class
employee_update_args = reqparse.RequestParser()
employee_update_args.add_argument('age', type=int, help='enter the age of the employee')
employee_update_args.add_argument('firstName', type=str, help='enter the first name of the employee')
employee_update_args.add_argument('lastName', type=str, help='enter the last name of the employee')
employee_update_args.add_argument('title', type=str, help='enter the title of the employee')

# Define how object is serialized
resource_fields = {
    'id': fields.Integer,
    'firstName': fields.String,
    'lastName': fields.String,
    'age': fields.Integer,
    'title': fields.String
}

# Handle bad get request - not in use any more
# def abort_if_employee_doesnt_exist(employee_id):
#     if employee_id not in employee:
#         abort(404, message=f"employee number {employee_id} doesn't exist")

# def abort_if_employee_exist(employee_id):
#     if employee_id in employee:
#         abort(409, message=f"employee number {employee_id} already exist")

# Basic api get request
class HealthCheck(Resource):

    def get(self):
        return {"version": '2020.02.02'}

class Employee(Resource):

    # Api request with params
    # def get(self, name, id):
    #     return {"name": name, "id": id}

    @marshal_with(resource_fields)
    def get(self, employee_id):

        result = EmployeeModel.query.filter_by(id=employee_id).first()
        if not result:
            abort(404, message="Could not find employee with this id")
        return result

    @marshal_with(resource_fields)
    def put(self, employee_id):

        args = employee_put_args.parse_args()
        result = EmployeeModel.query.filter_by(id=employee_id).first()
        if result:
            abort(409, message="User with this id already taken")
        employee = EmployeeModel(id=employee_id, firstName=args['firstName'], lastName=args['lastName'], age=args['age'], title=args['title'])
        db.session.add(employee)
        db.session.commit()
        return employee, 201

    @marshal_with(resource_fields)   
    def patch(self, employee_id):
        args = employee_update_args.parse_args()
        result = EmployeeModel.query.filter_by(id=employee_id).first()
        if not result:
            abort(404, message="Employee doesn\'t exist, can\'t update")

        if args['lastName']:
            result.lastName = args['lastName']
        if args['firstName']:
            result.firstName = args['firstName']
        if args['age']:
            result.age = args['age']
        if args['title']:
            result.title = args['title']

        db.session.commit()
        return result

    def delete(self, employee_id):
        try:
            EmployeeModel.query.filter_by(id=employee_id).delete()
        except:
            abort(404, message="Employee doesn\'t exist, can\'t delete")
        db.session.commit()
        return employee_id, 201

api.add_resource(HealthCheck, "/health")
api.add_resource(Employee, '/employee/<int:employee_id>')

# Part of the example of the api request with params
# api.add_resource(Employee, '/employee/<string:name>/<int:id>')

if __name__ == "__main__":
    app.run(port="80", debug=True)