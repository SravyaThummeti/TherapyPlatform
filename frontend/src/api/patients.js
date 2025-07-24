import axios from 'axios';

export function createPatient(data) {
  return axios.post('/patients', data);
}
