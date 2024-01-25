from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@localhost:8081/bdpythonapp'
app.config['SQLALCHEMY_TRACk_MODIFICATION'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#creacion de tabla categoria
class Category(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_num = db.Column(db.String(100))
    cat_desp = db.Column(db.String(100))
    
    def __init__(self, cat_num, cat_desp):
        self.cat_num = cat_num
        self.cat_desp = cat_desp

# Crear las tablas en la base de datos
db.create_all()

#esquema categoria

class CategoriaSchema(ma.Schema):
    class Meta:
        fielts = ('cat_id','cat_none','cat_desp')
        
# una sola respuesta 
categoria_schema = CategoriaSchema()
#cuando sean muchas respuestas
categoria_schema = CategoriaSchema(many=True)

#GET
@app.route('/categoria',methods=['GET'])
def get_categorias():
    all_categorias =Categoria.Query.all()
    result = categoria_schema.dump(all_categorias)

#GET POR iD

@app.route('/categoria/<id>',methods=['GET'])
def get_categoria_x_id(id):
    una_categoria = Categoria.Query.get(id)
    return categoria_schema.jsonify(una_categoria)

#meodo POST

@app.route('/categoria',methods=['POST'])
def insert_categoria():
    cat_nom = request.json['cat_nom']
    cat_nom = request.json['cat_desp']
    nuevo_registro=categoria(cat_nom,cat_desp)
    db.session.add(nuevo_registro)
    db.session.commit()
    return categoria_schema.jsonify(nuevo_registro)

#put

@app.router('/categoria/<id>',methods=['PUT'])
def update_categoria(id):
    idcat = Categoria.Query.get(id)
    
    cat_nom = request.json['cat_nom']
    cat_nom = request.json['cat_desp']
    
    data = request.get_json
    idcat.cat_nom = cat_nom
    idcat.cat_desp = cat_desp
    
    actualizarcategoria.cat_nom = cat_none
    actualizarcategoria.cat_desp = cat_desp
    
    db.session.commit()
    
    return categoria_schema.commit()

#delete
@app.route('categoria/<id>',methods=['DELETE'])
def delete_categoria(id):
    eliminarcategoria = Categoria.query.get(id)
    bd.session.delete(eliminarcateroria)
    db.session.commit()
    return categoria_schema.jsonify(eliminarcategoria)
    


@app.route('/categoria',(self, *args, **kwargs):
    return super().(*args, **kwargs)
)
#mensaje de bienvenida

def index():
    return jsonify({'mensaje':'Bienvenido  a mi app Rest con PYTHON'})

if __name__=="__main__":
    app.run(debug=True)
    

    

