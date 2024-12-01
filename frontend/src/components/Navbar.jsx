import React from 'react';
import '../assets/Navbar.css';

const Navbar = () => {
    return (
        <nav className="navbar">
            <div className="navbar-brand">Структурум</div>
            <div className="navbar-links">
                <a href="/">Главная страница</a>
                <a href="search">Поиск сотрудников</a>
                <a href="profile">Личный профиль</a>
            </div>
            <div className="navbar-login">
                <a href="login" className="login">Войти</a>
            </div>
        </nav>
    );
};

export default Navbar;