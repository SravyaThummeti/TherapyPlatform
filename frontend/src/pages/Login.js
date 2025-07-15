import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { login } from '../api/auth';

export default function Login() {
  const [form, setForm] = useState({ email: '', password: '' });
  const navigate = useNavigate();

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const { data } = await login(form);
      localStorage.setItem('token', data.access_token);
      const payload = JSON.parse(atob(data.access_token.split('.')[1]));
      // const normalized = payload.identity.role.toLowerCase().replace(/ /g, '-');
      // Flask-JWT-Extended v4 encodes identity under 'sub'
      const role = payload?.sub?.role;  // use 'sub' claim
      const normalized = role.toLowerCase().replace(/ /g, '-');
      navigate(`/dashboard/${normalized}`);
    } catch (err) {
      alert(err.response?.data?.msg || 'Login failed');
    }
  };

  return (
    <div style={{ maxWidth: 400, margin: 'auto', paddingTop: 50 }}>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: 15 }}>
          <label>Email</label><br />
          <input
            name="email"
            type="email"
            value={form.email}
            onChange={handleChange}
            required
            style={{ width: '100%', padding: 8 }}
          />
        </div>
        <div style={{ marginBottom: 15 }}>
          <label>Password</label><br />
          <input
            name="password"
            type="password"
            value={form.password}
            onChange={handleChange}
            required
            style={{ width: '100%', padding: 8 }}
          />
        </div>
        <button type="submit" style={{ width: '100%', padding: 10 }}>Login</button>
      </form>

      <p style={{ marginTop: 20, textAlign: 'center' }}>
        New User? <Link to="/register">Create an account</Link>
      </p>
    </div>
  );
}