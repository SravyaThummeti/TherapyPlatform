import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { register } from '../api/auth';

export default function Register() {
  const [form, setForm] = useState({
    first_name: '', last_name: '', email: '', phone: '', password: '', role: 'Therapist'
  });
  const navigate = useNavigate();

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await register(form);
      navigate('/login');
    } catch (err) {
      alert(err.response?.data?.msg || 'Registration failed');
    }
  };

  return (
    <div style={{ maxWidth: 400, margin: 'auto', paddingTop: 50 }}>
      <h2>Create Account</h2>
      <form onSubmit={handleSubmit}>
        {[
          { name: 'first_name', label: 'First Name' },
          { name: 'last_name',  label: 'Last Name'  },
          { name: 'email',      label: 'Email', type: 'email' },
          { name: 'phone',      label: 'Phone' },
          { name: 'password',   label: 'Password', type: 'password' }
        ].map(({ name, label, type }) => (
          <div key={name} style={{ marginBottom: 15 }}>
            <label>{label}</label><br />
            <input
              name={name}
              type={type || 'text'}
              value={form[name]}
              onChange={handleChange}
              required
              style={{ width: '100%', padding: 8 }}
            />
          </div>
        ))}

        <div style={{ marginBottom: 15 }}>
          <label>Role</label><br />
          <select name="role" value={form.role} onChange={handleChange} style={{ width: '100%', padding: 8 }}>
            {['Therapist','Practice Manager','Billing Staff','Admin Staff','Executive','HR'].map(r => (
              <option key={r} value={r}>{r}</option>
            ))}
          </select>
        </div>

        <button type="submit" style={{ width: '100%', padding: 10 }}>Register</button>
      </form>

      <p style={{ marginTop: 20, textAlign: 'center' }}>
        Already have an account? <Link to="/login">Login</Link>
      </p>
    </div>
  );
}