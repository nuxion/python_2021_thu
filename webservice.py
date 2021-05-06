import json

from flask import Flask, jsonify, request
from werkzeug.exceptions import BadRequest, MethodNotAllowed, NotFound


app = Flask(__name__)
students = {}
fields = ("name", "courses")


def response(request, status=200, **kwargs):
    """
    Build the response body as JSON and set the proper content-type
    header.
    """
    return jsonify(kwargs) if kwargs else "", status


def getStudentOr404(studentID):
    try:
        return students[studentID]
    except KeyError:
        raise NotFound


def getStudentFromRequest(request, complete=True):
    """
    Read a student from the request body in JSON format and retrieve
    a dictionary. If `complete` is `False`, a 400 Bad Request error
    will be raised if the read student is missing some of the
    `fields` elements.
    """
    try:
        student = request.get_json(force=True)
    except BadRequest:
        raise BadRequest("Could not decode body as JSON")
    # Every key must be a valid field name.
    for key in student:
        if key not in fields:
            raise BadRequest(f"Unknown field: {key}")
    if complete:
        for field in fields:
            if field not in student:
                raise BadRequest(f"Missing field: {field}")
    return student


@app.errorhandler(NotFound)
def notFoundHandler(e):
    """
    Called when a 404 not found is raised.
    """
    return response(request, status=404)


@app.errorhandler(MethodNotAllowed)
def methodNotAllowedHandler(e):
    """
    Called when a 405 is raised.
    """
    return response(request, status=405)


@app.errorhandler(BadRequest)
def badRequestHandler(e):
    """
    Called when a 400 is raised. Get the exception description and
    move it to the response's `reason` key in JSON format.
    """
    return response(request, status=400, reason=e.description)


@app.route(
    "/student",
    methods=["GET", "POST"],
    defaults={"studentID": None}
)
@app.route(
    "/student/<int:studentID>",
    methods=["GET", "PUT", "DELETE"]
)
def student(studentID):
    if request.method == "POST":
        student = getStudentFromRequest(request)
        try:
            newID = max(students.keys()) + 1
        except ValueError:
            newID = 1
        students[newID] = student
        return response(request, status=201, id=newID)
    
    elif request.method == "GET":
        if studentID is None:
            return response(
                request,
                students=[{"id": k, **v} for k, v in students.items()]
            )
        return response(
            request,
            student=getStudentOr404(studentID)
        )
    
    elif request.method == "PUT":
        student = getStudentOr404(studentID)
        newData = getStudentFromRequest(request, complete=False)
        student.update(newData)
        return response(request, status=204)
    
    elif request.method == "DELETE":
        try:
            del students[studentID]
        except KeyError:
            raise NotFound
        return response(request, status=204)


app.run("localhost", 7001, debug=True)
