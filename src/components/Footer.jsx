import React from 'react';
import '../assets/Footer.css';

const Footer = () => {
  return (
    <footer className="footer">

      <div className="info-footer">
        <h2>Важная информация</h2>
        <p>Данный сайт является проектом, сделанным с целью обучения и повышения своих навыков, а также для презентации и защиты на хакатоне Hack&Change (29.11.2024 - 01.12.2024).</p>
        <p>Стиль взят с интернет-ресурсов компании МТС находящихся в открытом доступе.</p>
      </div>

      <div className="chill_people">
          <p><b>Сделано командой VSUETA НА ПРОДЕ</b></p>
          <p>Никита Дужнов - Fullstack </p>
          <p>Алексей Овчинников - Backend </p>
          <p>Илья Иванчихин- Спикер</p>
          <p>Алексей Тронев - Frontend </p>
      </div>
      
    </footer>
  );
};

export default Footer;