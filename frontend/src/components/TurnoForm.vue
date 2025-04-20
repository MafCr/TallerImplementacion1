<template>
    <form @submit.prevent="submit">
      <input v-model="form.id" type="number">
      <button type="submit">Crear Turno</button>
    </form>
  </template>
  
  <script>
  import { crearTurno } from '../api/turnos';
  
  export default {
    data() {
      return {
        form: { id: null }
      }
    },
    methods: {
      async submit() {
        await crearTurno(this.form);
      }
    }
  }
  </script>