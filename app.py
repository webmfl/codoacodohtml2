from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_BD']='crudpy'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acercade')
def acercade():
    return render_template('acercade.html')

@app.route('/citytour')
def citytour():
    return render_template('citytour.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/paquetes')
def paquetes():
    return render_template('paquetes.html')





@app.route('/crear')
def crear():
    return render_template('crear.html')
   


@app.route('/destroy/<int:id>')
def eliminar(id):
    sql = "DELETE FROM `crudpy`.`empleados` WHERE id=%s;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,(id))
    conn.commit()
    return redirect('/mostrar')

@app.route('/mostrar')
def mostrar():
    sql = "SELECT * FROM `crudpy`.`empleados`;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    empleados=cursor.fetchall()
    return render_template('mostrar.html', empleados = empleados)

@app.route('/store', methods=['POST'])
def grabar():
    #recibiendo datos del formulario
    _nombre=request.form['nombre']
    _dni=request.form['dni']
    _telefono=request.form['telefono']

    sql = "INSERT INTO `crudpy`.`empleados` (`id`, `nombre`, `dni`, `telefono`) VALUES (NULL, %s, %s, %s);"
    datos=(_nombre,_dni,_telefono)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return render_template('index.html')

@app.route('/edit/<int:id>')
def edit(id):
    sql = "SELECT * FROM `crudpy`.`empleados` WHERE id=%s;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, (id))
    empleados=cursor.fetchall()
    conn.commit()
    return render_template('editar.html', empleados=empleados)

@app.route('/update', methods=['POST'])
def update():
    #recibiendo datos del formulario
    _nombre=request.form['nombre']
    _dni=request.form['dni']
    _telefono=request.form['telefono']
    id=request.form['idForm']

    sql = "UPDATE `crudpy`.`empleados` SET `nombre`=%s, `dni`=%s, `telefono`=%s WHERE id=%s"
    datos=(_nombre,_dni,_telefono, id)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/mostrar')


if __name__== '__main__':
    app.run(None, 5000, True)

