import React from 'react';
import { Navigate, useLocation, useParams } from 'react-router-dom';

export default function ProtectedRoute({ children, allowedRoles }) {
  const token = localStorage.getItem('token');
  const location = useLocation();
  // const { role: paramRole } = useParams();

  if (!token) {
    // Not logged in
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  let payload;
  try {
    payload = JSON.parse(atob(token.split('.')[1]));
  } catch {
    return <Navigate to="/login" replace />;
  }

  // JWT-Extended v4 puts your identity in `sub`
  const userRole = payload?.sub?.role;
  const normalized = userRole?.toLowerCase().replace(/ /g, '-');

  // If the URL param doesn't match your actual role, kick them out
  if (!allowedRoles.map(r => r.toLowerCase()).includes(normalized)) {
    return <Navigate to="/login" replace />;
  }

  return children;
}