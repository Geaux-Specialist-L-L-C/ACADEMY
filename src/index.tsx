import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import { ProfileProvider } from './contexts/ProfileContext';
import App from './App';
import ErrorBoundary from './components/shared/ErrorBoundary';
import './index.css';

// Firebase configuration with environment variables
const firebaseConfig = {
  apiKey: process.env.REACT_APP_FIREBASE_API_KEY || '',
  authDomain: process.env.REACT_APP_FIREBASE_AUTH_DOMAIN || '',
  projectId: process.env.REACT_APP_FIREBASE_PROJECT_ID || '',
  storageBucket: process.env.REACT_APP_FIREBASE_STORAGE_BUCKET || '',
  messagingSenderId: process.env.REACT_APP_FIREBASE_MESSAGING_SENDER_ID || '',
  appId: process.env.REACT_APP_FIREBASE_APP_ID || '',
  measurementId: process.env.REACT_APP_FIREBASE_MEASUREMENT_ID || '',
  databaseURL: process.env.REACT_APP_FIREBASE_DATABASE_URL || ''
};

// SSL configuration
const sslConfig = {
  key: process.env.REACT_APP_SSL_KEY || '',
  cert: process.env.REACT_APP_SSL_CERT || ''
};

// Listen for auth service worker status events
window.addEventListener('firebase-auth-worker-status', (event: Event) => {
  const { success, isSecure, error } = (event as CustomEvent).detail;
  if (!success) {
    console.warn(
      'Auth service worker initialization status:',
      { success, isSecure, error }
    );
  }
});

// Listen for auth errors from service worker
window.addEventListener('firebase-auth-error', (event: Event) => {
  const { error, fallbackToRedirect } = (event as CustomEvent).detail;
  console.error('Firebase auth error:', error);
  if (fallbackToRedirect) {
    console.info('Falling back to redirect method for authentication');
  }
});

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);

root.render(
  <React.StrictMode>
    <ErrorBoundary>
      <BrowserRouter>
        <AuthProvider>
          <ProfileProvider>
            <App />
          </ProfileProvider>
        </AuthProvider>
      </BrowserRouter>
    </ErrorBoundary>
  </React.StrictMode>
);
