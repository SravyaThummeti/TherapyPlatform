import React, { useState } from 'react';
import { createAuthorization } from '../../api/authorizations';

export default function AuthorizationForm() {
  const [form, setForm] = useState({
    patient_id: '', therapist_id: '',
    insurance_id: '', referral_id: '',
    start_date: '', end_date: '',
    visits_authorized: ''
  });
  const [error, setError] = useState('');

  const handleChange = e =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await createAuthorization(form);
      alert('✅ Authorization created');
      setForm({
        patient_id: '', therapist_id: '',
        insurance_id: '', referral_id: '',
        start_date: '', end_date: '',
        visits_authorized: ''
      });
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
    <div style={{ maxWidth: 500, margin: 'auto', padding: 20 }}>
      <h2>New Authorization</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        {[
          { name: 'patient_id',        label: 'Patient ID' },
          { name: 'therapist_id',      label: 'Therapist ID' },
          { name: 'insurance_id',      label: 'Insurance ID' },
          { name: 'referral_id',       label: 'Referral ID (opt)' },
          { name: 'start_date',        label: 'Start Date', type: 'date' },
          { name: 'end_date',          label: 'End Date',   type: 'date' },
          { name: 'visits_authorized', label: 'Visits Authorized', type: 'number' }
        ].map(({ name, label, type }) => (
          <div key={name} style={{ marginBottom: 12 }}>
            <label>{label}</label><br/>
            <input
              name={name}
              type={type || 'text'}
              value={form[name]}
              onChange={handleChange}
              required={name !== 'referral_id'}
              style={{ width: '100%', padding: 8 }}
            />
          </div>
        ))}
        <button type="submit" style={{ padding: '8px 16px' }}>
          Save Authorization
        </button>
      </form>
    </div>
  );
}
