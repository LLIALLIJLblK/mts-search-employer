import React from 'react';
import '../assets/RegisterPage.css';

const RegisterPage = () => {
  return (
    <div className="register-page">
      <div className="register-form">
        <h1>Регистрация</h1>
        <form>
          <div className="form-group">
            <label htmlFor="phone">Номер телефона</label>
            <input type="text" id="phone" name="phone" />
          </div>
          <div className="form-group">
            <label htmlFor="email">Почта</label>
            <input type="email" id="email" name="email" />
          </div>
          <div className="form-group">
            <label htmlFor="password">Пароль</label>
            <input type="password" id="password" name="password" />
          </div>
          <div className="form-group">
            <label htmlFor="confirmPassword">Повторите пароль</label>
            <input type="password" id="confirmPassword" name="confirmPassword" />
          </div>
          <div className="form-group">
            <label htmlFor="apiKey">API-Key</label>
            <input type="text" id="apiKey" name="apiKey" />
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