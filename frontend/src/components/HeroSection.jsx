import React from 'react';
import '../assets/HeroSection.css';
import roundTube from '../assets/images/round_tube.svg'; // Импортируйте SVG-файл

const HeroSection = () => {
  return (
    <div className="hero-container">
      <div className="hero-section">
        <div className="hero-content">
          <h1>Встречайте Структурум</h1>
          <p>Веб-сервис визуализации организационной структуры для клиентов МТС Линк</p>
          <a href="#use" className="cta-button">Подробнее</a>
        </div>
        <img src={roundTube} alt="Round Tube" className="round-tube" /> {/* Добавьте SVG в JSX */}
      </div>
    </div>
  );
};

export default HeroSection;