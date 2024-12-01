import React from 'react';
import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom';
import Navbar from './components/Navbar';
import HeroSection from './components/HeroSection';
import AboutSection from './components/AboutSection';
import LoginPage from './components/LoginPage';
import RegisterPage from './components/RegisterPage';
import Footer from './components/Footer';
import ProfilePage from './components/ProfilePage';
import SearchEmployPage from './components/SearchEmployPage';

const App = () => {
  const location = useLocation();

  return (
    <div>
      {(location.pathname !== '/login' && location.pathname !== '/register') && <Navbar />}
      <Routes>
        <Route path="/" element={<><HeroSection /><AboutSection /></>} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/search" element={<SearchEmployPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/profile" element={<ProfilePage />} /> {/* Добавьте этот маршрут */}
      </Routes>
      {(location.pathname !== '/login' && location.pathname !== '/register') && <Footer />}
    </div>
  );
};

const AppWrapper = () => (
  <Router>
    <App />
  </Router>
);

export default AppWrapper;