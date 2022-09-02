from crypt import methods
from flask import Flask, jsonify
from config import config
from flask_mysqldb import MySQL
#arquitectura cliente - servidor -> intercambiar datos entre ellos

app = Flask(__name__)

conexion = MySQL(app)

@app.route('/')
def index():
    return "Ejercicio Back end y Front end"

#  Categorias
@app.route('/categorias', methods=['GET'])
def lista_categorias():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT id, name FROM category"
        cursor.execute(sql)
        datos = cursor.fetchall()
        categorias=[]
        for fila in datos:
            categoria={'id': fila[0], 'name': fila[1]}
            categorias.append(categoria)
        return jsonify({'Categorias': categorias})
    except Exception as ex :
        return "Error"


@app.route('/categorias/<id>', methods=['GET'])
def list_categoria(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT id, name FROM category WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            categoria={'id': datos[0], 'name': datos[1]}
            return jsonify({'Categoria': categoria})
        else:
            return jsonify({'Categoria': "Categoria no encontrado"})
           
    except Exception as ex:
        return "Error"


#Producto
@app.route('/productos', methods=['GET'])
def list_productos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT id, name, url_image, price, discount, category FROM product"
        cursor.execute(sql)
        datos = cursor.fetchall()
        productos=[]
        for fila in datos:
            producto={'id': fila[0], 'name': fila[1], 'url_image': fila[2], 'price': fila[3], 'discount': fila[4], 'category': fila[5] }
            productos.append(producto)
        return jsonify({'Productos': productos})
    except Exception as ex:
        return "Error"


@app.route('/productos/<category>', methods=['GET'])
def list_producto(category):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT id, name, url_image, price, discount, category FROM product WHERE category='{0}'".format(category)
        cursor.execute(sql)
        datos = cursor.fetchall()
        productos=[]
        for fila in datos:
            producto={'id': fila[0], 'name': fila[1], 'url_image': fila[2], 'price': fila[3], 'discount': fila[4], 'category': fila[5] }
            productos.append(producto)
        return jsonify({'Productos': productos})
    except Exception as ex:
        return "Error"




#Error
def notFound(error):
    return "<h3>La página que intentas buscar no existe</h3>"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, notFound)
    app.run()
