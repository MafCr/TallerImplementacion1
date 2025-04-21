<template>
    <div>
      <h1>Sistema de Turnos Virtuales</h1>
      <button @click="solicitarTurno">Solicitar Turno</button>
      <p v-if="turno">Tu turno es: {{ turno }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        turno: null
      };
    },
    methods: {
      async solicitarTurno() {
        try {
          const response = await fetch('http://backend:5000/api/turnos', {
            method: 'POST'
          });
          this.turno = await response.json();
        } catch (error) {
          console.error('Error al solicitar turno:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  h1 {
    color: #2c3e50;
  }
  button {
    padding: 10px 20px;
    background-color: #42b983;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  </style>