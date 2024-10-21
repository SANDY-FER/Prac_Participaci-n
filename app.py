from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Ruta para la página de inicio de sesión
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validar usuario (puedes usar un simple check para ejemplo)
        if username and password:  # Acepta cualquier usuario/contraseña para demostración
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            return "Por favor, ingrese un nombre de usuario y una contraseña válidos."
    return render_template('login.html')

# Ruta para la página de bienvenida después de iniciar sesión
@app.route('/set_session')
def welcome():
    if 'username' in session:
        username = session['username']
        return render_template('welcome.html', username=username)
    return redirect(url_for('login'))

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
