from flask import Flask, jsonify, request  # import objects from the Flask model

app = Flask(__name__)  # define app using Flask

languages = [{'name': 'JavaScript'}, {'name': 'Python'}, {'name': 'Ruby'}]


@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works!'})


@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages': languages})


@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    for i in languages:
        if i['name'] == name:
            return jsonify(i)
    return jsonify({'message': 'language not found'})
    # langs = [language for language in languages if language['name'] == name]
    # return jsonify({'language': langs[0]})


@app.route('/lang', methods=['POST'])
def addOne():
    vari = {'name': request.json['name']}
    languages.append(vari)
    return jsonify({'languages': languages})


@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'language': langs[0]})


@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
    lang = [language for language in languages if language['name'] == name]
    languages.remove(lang[0])
    return jsonify({'languages': languages})


if __name__ == '__main__':
    app.run(debug=True, port=8080)  # run app on port 8080 in debug mode
