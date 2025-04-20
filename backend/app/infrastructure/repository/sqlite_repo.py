from sqlite3 import connect
from app.domain.interfaces import TurnoRepository
from app.domain.models import Turno

class SQLiteTurnoRepository(TurnoRepository):
    def __init__(self):
        self.conn = connect('turnos.db')
        self._crear_tabla()
        
    def _crear_tabla(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS turnos (
                id INTEGER PRIMARY KEY,
                estado TEXT,
                datos TEXT
            )
        ''')
        
    def guardar(self, turno: Turno):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO turnos (id, estado, datos) 
            VALUES (?, ?, ?)
        ''', (turno.id, turno.estado, str(turno.datos)))
        self.conn.commit()