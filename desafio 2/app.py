from flask import Flask, render_template, request, jsonify, redirect, url_for 
from modelos import db, Reservacion
from datetime import datetime, timedelta


app = Flask(__name__)

# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la aplicación de la base de datos
db.init_app(app)

# Importar la clase correcta del modelo
from modelos import Reservacion
    
@app.route('/')
def pagina_reserva():
    return render_template('pagina_reserva.html')

@app.route('/guardar_reservacion', methods=['POST'])
def guardar_reservacion():
    data = request.json
    fecha_str = data['fecha']
    fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d') 

    hora_str = data['hora']
    hora_obj = datetime.strptime(hora_str, '%H:%M').time()  

    nueva_reserva = Reservacion(
        nombre=data['nombre'],
        apellido=data['apellido'],
        telefono=data['telefono'],
        email=data['email'],
        fecha=fecha_obj,
        hora=hora_obj,
        num_personas=data['num_personas'])
        
    db.session.add(nueva_reserva)
    db.session.commit()
    return jsonify({'message': 'Reserva creada correctamente', 'id':nueva_reserva.id})

@app.route('/administrar_reserva')
def administrar_reserva():
    # Tu lógica para la página de administración de reservas
    return render_template('administrar_reserva.html')

#PAGINA PARA LEER reservas

@app.route('/visualizar_reserva/<int:id>', methods=['GET'])
def visualizar_reserva(id):
    reserva = Reservacion.query.get(id)
    if reserva:
        reserva_data = {
            'id': reserva.id, 
            'nombre': reserva.nombre,
            'apellido': reserva.apellido,
            'telefono': reserva.telefono,
            'email': reserva.email,
            'fecha': reserva.fecha.strftime('%Y-%m-%d'),
            'hora': reserva.hora.strftime('%H:%M'),
            'num_personas': reserva.num_personas
        }
        return jsonify(reserva_data)
       
    else:
        return jsonify({'error': 'Reserva no encontrada'}), 404



#Pagina para editar reservas. 
@app.route('/editar_reserva/<int:id>', methods=['GET', 'POST'])
def editar_reserva(id):
    reserva = Reservacion.query.get(id)
    if reserva:
        if request.method == 'POST':
            # Obtener los datos del formulario de edición
            nombre = request.form.get('nombre')
            apellido = request.form.get('apellido')
            telefono = request.form.get('telefono')
            email = request.form.get('email')
            fecha = request.form.get('fecha')
            hora = request.form.get('hora')
            num_personas = request.form.get('num_personas')

            # Actualizar los atributos de la reserva
            reserva.nombre = nombre
            reserva.apellido = apellido
            reserva.telefono = telefono
            reserva.email = email
            reserva.fecha = fecha
            reserva.hora = hora
            reserva.num_personas = num_personas

            # Guardar los cambios en la base de datos
            db.session.commit()

            return redirect(url_for('administrar_reserva'))

        return render_template('editar_reserva.html', reserva=reserva)
    else:
        return jsonify({'error': 'Reserva no encontrada'}), 404

    
@app.route("/cancelar/<int:id_reserva>")
def cancelar(id_reserva):
    # Obtener la reserva a eliminar por su ID
    reserva = Reservacion.query.get(id_reserva)

    if reserva:
        # Eliminar la reserva si existe
        db.session.delete(reserva)
        db.session.commit()
        return redirect(url_for("administrar_reserva"))
    else:
        # Manejar el caso en el que no se encuentra la reserva
        return "Reserva no encontrada", 404

   
if __name__ == '__main__':
    app.run(debug=True)
