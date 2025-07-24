import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';

import Register from './features/auth/Register';
import Login    from './features/auth/Login';
import ProtectedRoute from './components/ProtectedRoute';
import TherapistDashboard from './features/therapist/TherapistDashboard';
import PracticeManagerDashboard from './features/practiceManager/PracticeManagerDashboard';
import BillingDashboard from './features/billing/BillingDashboard';
import AdminDashboard from './features/admin/AdminDashboard';
import ExecutiveDashboard from './features/executive/ExecutiveDashboard';
import HRDashboard from './features/hr/HRDashboard';
import AuthorizationForm from './features/authorizations/AuthorizationForm';
import PatientForm from './features/patients/PatientForm';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Index: redirect '/' to '/login' */}
        <Route index element={<Navigate to="/login" replace />} />
        <Route path="/" element={<Navigate to="/login" replace />} />

        {/* Public routes */}
        <Route path="/register" element={<Register />} />
        <Route path="/login"    element={<Login />} />

         {/* ── Protected Dashboard ───────────────────────────── */}
        {/* <Route
          path="/dashboard/:role"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        /> */}

        <Route path="/dashboard/therapist" element={
          <ProtectedRoute allowedRoles={['Therapist']}>
            <TherapistDashboard />
          </ProtectedRoute>
        } />
        <Route path="/dashboard/practice-manager" element={
          <ProtectedRoute allowedRoles={['Practice Manager']}>
            <PracticeManagerDashboard />
          </ProtectedRoute>
        } />
        <Route path="/dashboard/billing-staff" element={
          <ProtectedRoute allowedRoles={['Billing Staff']}>
            <BillingDashboard />
          </ProtectedRoute>
        } />
        <Route path="/dashboard/admin-staff" element={
          <ProtectedRoute allowedRoles={['Admin Staff']}>
            <AdminDashboard />
          </ProtectedRoute>
        } />
        <Route path="/dashboard/executive" element={
          <ProtectedRoute allowedRoles={['Executive']}>
            <ExecutiveDashboard />
          </ProtectedRoute>
        } />
        <Route path="/dashboard/hr" element={
          <ProtectedRoute allowedRoles={['HR']}>
            <HRDashboard />
          </ProtectedRoute>
        } />

        <Route
          path="/dashboard/therapist/new-authorization"
          element={
          <ProtectedRoute allowedRoles={['Therapist']}>
          <AuthorizationForm />
          </ProtectedRoute>
        } />

        <Route
          path="/dashboard/admin/new-patient" 
          element={ 
          <ProtectedRoute allowedRoles={['Admin Staff']}> 
            <PatientForm /> 
          </ProtectedRoute> 
          } />




        {/* Catch-all: any other path redirects to login */}
        <Route path="*" element={<Navigate to="/login" replace />} />
      </Routes>
    </BrowserRouter>
  );
}