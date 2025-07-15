import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';

import Register from './pages/Register';
import Login    from './pages/Login';
import ProtectedRoute from './components/ProtectedRoute';
import TherapistDashboard from './pages/TherapistDashboard';
import PracticeManagerDashboard from './pages/PracticeManagerDashboard';
import BillingDashboard from './pages/BillingDashboard';
import AdminDashboard from './pages/AdminDashboard';
import ExecutiveDashboard from './pages/ExecutiveDashboard';
import HRDashboard from './pages/HRDashboard';

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




        {/* Catch-all: any other path redirects to login */}
        <Route path="*" element={<Navigate to="/login" replace />} />
      </Routes>
    </BrowserRouter>
  );
}