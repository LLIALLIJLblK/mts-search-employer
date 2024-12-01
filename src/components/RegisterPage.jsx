import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../assets/RegisterPage.css';

const RegisterPage = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    phone: '',
    email: '',
    password: '',
    confirmPassword: '',
    apiKey: '',
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('http://localhost/auth/sign-up', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: formData.email,
          password: formData.password,
          platform_key: formData.apiKey,
        }),
      });

      if (response.ok) {
        // Если регистрация прошла успешно, перенаправляем на страницу /search
        navigate('/search');
      } else {
        // Обработка ошибок, если регистрация не удалась
        console.error('Ошибка регистрации:', response.statusText);
      }
    } catch (error) {
      console.error('Ошибка при отправке запроса:', error);
    }
  };

  return (
    <div className="register-page">
      <div className="register-form">
        <h1>Регистрация</h1>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="email">Почта</label>
            <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label htmlFor="password">Пароль</label>
            <input type="password" id="password" name="password" value={formData.password} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label htmlFor="confirmPassword">Повторите пароль</label>
            <input type="password" id="confirmPassword" name="confirmPassword" value={formData.confirmPassword} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label htmlFor="apiKey">API-Key</label>
            <input type="text" id="apiKey" name="apiKey" value={formData.apiKey} onChange={handleChange} />
          </div>
          <button type="submit" className="register-button">Зарегистрироваться</button>
        </form>
        <div className="login-link">
          <p>Уже есть аккаунт? <a href="/login"><b>Войдите!</b></a></p>
        </div>
      </div>
    </div>
  );
};

export default RegisterPage;