import json

from flask import Flask, request, jsonify 
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug = True)





data_list = []



		

class info:
    def __init__(self, id, title, problem,point,level,language, input, expected_output):
        self.id = id
        self.title = title
        self.problem = problem
        self.level = level
        self.language = language
        self.input = input
        self.expected_output = expected_output




@app.route('/create', methods = ["POST"])
def Create():
    try:
        id = request.json['id']
        title = request.json['title']
        problem = request.json['problem']
        point = request.json['point']
        level = request.json['level']
        language = request.json['language']
        input = request.json['input']
        expected_output = request.json['expected_output']

        data = info(id, title, problem,point,level,language, input, expected_output)
        data_list.append(data)

        return json.dumps(data.__dict__)
    except Exception as e:
        return jsonify({"Error": "Invalid request."})


@app.route('/read', methods = ["GET"])
def read():
    try:
        copy = []
        for item in data_list:
            s = json.dumps(item.__dict__)
            copy.append(s)
        return jsonify(copy)
    except Exception as e:
        return jsonify({"Error": "Invalid request."})



    


@app.route('/read/<string:id>', methods = ["GET"])
def read_one(id):
    try:
        print(type(id))
        for item in data_list:
            print(type(item.id))
            if item.id == id :
                temp = item
                print(temp)
                break
        return json.dumps(temp.__dict__)
    except Exception as e:
        return jsonify({"Error": "Invalid request."})




@app.route("/update/<string:id>", methods = ["PUT"])
def update(id):
    try:
        print(type(id))
        id_2 = request.json['id']
        title = request.json['title']
        problem = request.json['problem']
        point = request.json['point']
        level = request.json['level']
        language = request.json['language'] 
        input = request.json['input']
        expected_output = request.json['expected_output']
        print(type(id))
        for index in range(len(data_list)):
            print(index)
            
            if data_list[index].id == id :
                temp = id

                data_list[index].title = title
                data_list[index].problem = problem
                data_list[index].point = point
                data_list[index].level = level
                data_list[index].language = language
                data_list[index].input = input
                data_list[index].expected_output = expected_output
                break
        return json.dumps(data_list[temp].__dict__)
    except Exception as e:
        return jsonify({"Error": "Invalid request."})




@app.route("/delete/<string:id>", methods = ["PUT"])
def delete(id):
    try :
        for index in range(len(data_list)):
            print(index)
            if data_list[index].id == id :
                data_list.pop(index)
    except Exception as e:
        return jsonify({"Error": "Invalid request."})







        







