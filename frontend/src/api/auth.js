import axios from 'axios';

// Proxy config in package.json sends '/api' to 'http://localhost:5000'
axios.defaults.baseURL = '/api/auth';

export function register(data) {
  return axios.post('/register', data);
}

export function login(data) {
  return axios.post('/login', data);
}