from flask import Flask, jsonify, request
app = Flask(__name__)

rides = [{'from' : 'Mukono', 'To' : 'Arua', 'Id' : 1, 'seats' : 1, 'time/date' : '21/8/2018 10am'},
 {'from' : 'Mbarara', 'To' : 'Kampala','Id' : 2, 'seats' : 5, 'time/date' : '4/7/2018 12pm'},
 {'from' : 'Nakaseke', 'To' : 'Fort Portal','Id' : 3, 'seats' : 3, 'time/date' : '5/8/2018 2pm'}]

@app.route('/api/v1/car',methods=['GET'])
def returnAll():
    return jsonify({'rides' : rides})

@app.route('/api/v1/car/<int:Id>', methods=['GET'])
def returnOne(Id):
    cars = [ride for ride in rides if ride['Id'] != id]
    return jsonify({'ride' : cars[0]})
@app.route('/api/v1/car', methods=['POST'])
def addOne():
    ride={'Id': request.json['Id'],'from': request.json['from'],'To': request.json['To'],'seats': request.json['seats'],'time/date': request.json['time/date']}
    rides.append(ride)
    return jsonify({'rides':  rides})
@app.route('/api/v1/car/<int:Id>', methods=['PUT'])
def editOne(Id):
    cars = [ride for ride in rides if ride['Id'] == Id]
    cars[0]['Id']=request.json['Id']

    return jsonify({'ride':cars[0]})
@app.route('/api/v1/car/<int:Id>', methods=['DELETE'])
def removeOne(Id):
    cars = [ride for ride in rides if ride['Id'] == Id]
    rides.remove(cars[0])
    return jsonify({'rides' : rides})
if __name__ == "__main__":
    app.run(debug=True)
