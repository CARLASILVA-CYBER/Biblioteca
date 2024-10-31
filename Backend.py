
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pymysql
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

# Configuração do MySQL
mysql_connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="biblioteca"
)

# Configuração do MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["biblioteca_logs"]
user_logs = mongo_db["user_logs"]

class Books(Resource):
    def get(self):
        cursor = mysql_connection.cursor()
        cursor.execute("SELECT * FROM livros")
        books = cursor.fetchall()
        return jsonify(books)

class Borrow(Resource):
    def post(self):
        data = request.get_json()
        cursor = mysql_connection.cursor()
        cursor.execute("INSERT INTO emprestimos (id_usuario, id_livro, data_emprestimo) VALUES (%s, %s, NOW())", 
                       (data['user_id'], data['book_id']))
        mysql_connection.commit()
        user_logs.insert_one({"user_id": data['user_id'], "action": "borrow", "book_id": data['book_id']})
        return jsonify({"message": "Empréstimo realizado com sucesso"})

class Return(Resource):
    def put(self):
        data = request.get_json()
        cursor = mysql_connection.cursor()
        cursor.execute("UPDATE emprestimos SET data_devolucao = NOW() WHERE id_usuario = %s AND id_livro = %s", 
                       (data['user_id'], data['book_id']))
        mysql_connection.commit()
        user_logs.insert_one({"user_id": data['user_id'], "action": "return", "book_id": data['book_id']})
        return jsonify({"message": "Livro devolvido com sucesso"})

class Recommendations(Resource):
    def get(self):
        user_id = request.args.get('user_id')
        recommendations = ["Livro A", "Livro B", "Livro C"]
        return jsonify(recommendations)

api.add_resource(Books, '/books')
api.add_resource(Borrow, '/borrow')
api.add_resource(Return, '/return')
api.add_resource(Recommendations, '/recommendations')

if __name__ == "__main__":
    app.run(debug=True)
