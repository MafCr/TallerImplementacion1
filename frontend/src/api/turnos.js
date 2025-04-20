import axios from 'axios';

export const crearTurno = (data) => 
  axios.post('http://localhost:5000/turnos', data);