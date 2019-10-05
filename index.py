from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'xefi550t7t6tjn36.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'otxttx36ewyxk9nw'
app.config['MYSQL_PASSWORD'] = 'j2kyi3w59ef32r9c'
app.config['MYSQL_DB'] = 'wf7cwv96odt3xtzf'
app.config['MYSQL_POLL_RECYCLE'] = 280

mysql = MySQL(app)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def aboutPage():
    return render_template('about.html') 
    
@app.route('/addProd')
def addProd():

    cur = mysql.connection.cursor()
    cur.execute('select * from tb_productos ORDER BY idprod DESC LIMIT 1;')
    lastProd = cur.fetchall()
    
    cur.execute('select * from tb_categorias;')
    categorias = cur.fetchall()

    cur.close()

    return render_template('add.html'   , product = lastProd, lstCat = categorias)

@app.route('/addProd', methods=['POST'])
def addProd_Post():
    if request.method == 'POST':
        idprod      = request.form['idprod']
        descripcion = request.form['descripcion']
        stock       = request.form['stock']
        precio      = request.form['precio']
        idcategoria = request.form['idcategoria']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tb_productos values (%s,%s,%s,%s,%s,1)",(idprod,descripcion,stock,precio,idcategoria))
        mysql.connection.commit()

        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
