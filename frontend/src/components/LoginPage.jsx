import React from 'react';
import '../assets/LoginPage.css';

const LoginPage = () => {
  return (
    <div className="login-page">
      <div className="login-form">
        <h1>Вход</h1>
        <form>
          <div className="form-group">
            <label htmlFor="login">Логин (Номер телефона, почта)</label>
            <input type="text" id="login" name="login" />
          </div>
          <div className="form-group">
            <label htmlFor="password">Пароль</label>
            <input type="password" id="password" name="password" />
          </div>
          <button type="submit" className="login-button">Войти</button>
        </form>
        <div className="register-link">
          <p>Первый раз на сайте? <a href="/register"><b>Зарегистрируйтесь!</b></a></p>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;