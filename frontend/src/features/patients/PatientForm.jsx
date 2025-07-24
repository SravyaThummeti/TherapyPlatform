import React, { useState } from 'react';
import { createPatient } from '../../api/patients';

export default function PatientForm() {
  const [form, setForm] = useState({ first_name:'', last_name:'', dob:'' });
  const [error, setError] = useState('');

  const handleChange = e =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await createPatient(form);
      alert('✅ Patient created');
      setForm({ first_name:'', last_name:'', dob:'' });
      setError('');
    } catch (err) {
      setError(
        err.response?.data
          ? JSON.stringify(err.response.data)
          : 'Server error'
      );
    }
  };

  return (
    <div style={{ maxWidth: 400, margin: 'auto', padding: 20 }}>
      <h2>New Patient</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        {[
          { name: 'first_name', label: 'First Name', type: 'text' },
          { name: 'last_name',  label: 'Last Name',  type: 'text' },
          { name: 'dob',        label: 'Date of Birth', type: 'date' }
        ].map(({ name, label, type }) => (
          <div key={name} style={{ marginBottom: 12 }}>
            <label>{label}</label><br/>
            <input
              name={name}
              type={type}
              value={form[name]}
              onChange={handleChange}
              required
              style={{ width: '100%', padding: 8 }}
            />
          </div>
        ))}
        <button type="submit" style={{ padding: '8px 16px' }}>
          Save Patient
        </button>
      </form>
    </div>
  );
}
