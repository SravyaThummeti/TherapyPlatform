import axios from 'axios';

// BaseURL is /api via your proxy
export function createAuthorization(data) {
  return axios.post('/authorizations', data);
}
