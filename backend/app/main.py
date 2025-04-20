from flask import Flask

app = Flask(__name__)

# ... (rutas y configuración)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # ← ¡Esto mantendrá el contenedor activo!