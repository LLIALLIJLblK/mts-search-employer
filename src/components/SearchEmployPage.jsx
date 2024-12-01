import React, { useState } from 'react';
import '../assets/SearchEmployPage.css';

const SearchEmployPage = () => {
  const [formData, setFormData] = useState({
    position: '',
    ageRange: '',
    city: '',
    skills: '',
    gender: '',
    educationPlace: '',
    startDate: '',
    officeType: '',
    floorNumber: '',
    email: '',
    phone: '',
    socialLink: '',
    about: '',
  });

  const [searchQuery, setSearchQuery] = useState('');

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSearchChange = (e) => {
    setSearchQuery(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Здесь вы можете добавить логику для обработки данных формы
    console.log('Form data submitted:', formData);
    console.log('Search query:', searchQuery);
  };

  return (
    <div className="search-employ-page">
      <aside className="filters">
        <h2>Фильтры</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="position">Должность</label>
            <select id="position" name="position" value={formData.position} onChange={handleChange}>
              <option value="">Выберите из списка</option>
              <option value="developer">Разработчик</option>
              <option value="designer">Дизайнер</option>
              <option value="manager">Менеджер</option>
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="ageRange">Возраст</label>
            <div className="age-range-options">
              <label>
                <input type="radio" name="ageRange" value="18-30" checked={formData.ageRange === '18-30'} onChange={handleChange} />
                18-30
              </label>
              <label>
                <input type="radio" name="ageRange" value="30-45" checked={formData.ageRange === '30-45'} onChange={handleChange} />
                30-45
              </label>
              <label>
                <input type="radio" name="ageRange" value="45-60" checked={formData.ageRange === '45-60'} onChange={handleChange} />
                45-60
              </label>
              <label>
                <input type="radio" name="ageRange" value="60+" checked={formData.ageRange === '60+'} onChange={handleChange} />
                60+
              </label>
            </div>
          </div>
          <div className="form-group">
            <label htmlFor="city">Город</label>
            <select id="city" name="city" value={formData.city} onChange={handleChange}>
              <option value="">Выберите из списка</option>
              <option value="moscow">Москва</option>
              <option value="saint-petersburg">Санкт-Петербург</option>
              <option value="voronezh">Воронеж</option>
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="skills">Навыки</label>
            <textarea id="skills" name="skills" value={formData.skills} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label htmlFor="gender">Пол</label>
            <select id="gender" name="gender" value={formData.gender} onChange={handleChange}>
              <option value="">Выберите из списка</option>
              <option value="male">Мужской</option>
              <option value="female">Женский</option>
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="educationPlace">Место учебы</label>
            <input type="text" id="educationPlace" name="educationPlace" value={formData.educationPlace} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label htmlFor="startDate">Дата начала работы</label>
            <input type="date" id="startDate" name="startDate" value={formData.startDate} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label htmlFor="officeType">Тип офиса</label>
            <select id="officeType" name="officeType" value={formData.officeType} onChange={handleChange}>
              <option value="">Выберите из списка</option>
              <option value="central">Центральный</option>
              <option value="district">Районный</option>
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="floorNumber">Номер этажа</label>
            <input type="number" id="floorNumber" name="floorNumber" value={formData.floorNumber} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label htmlFor="email">Почта</label>
            <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label htmlFor="phone">Телефон</label>
            <input type="tel" id="phone" name="phone" value={formData.phone} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label htmlFor="socialLink">Ссылка на соцсеть</label>
            <input type="text" id="socialLink" name="socialLink" value={formData.socialLink} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label htmlFor="about">О себе</label>
            <textarea id="about" name="about" value={formData.about} onChange={handleChange} />
          </div>
          <button type="submit" className="search-button">Применить фильтры</button>
        </form>
      </aside>
      <div className="search-content">
        <div className="search-bar">
          <input type="text" placeholder="Поиск по имени, фамилии, должности..." value={searchQuery} onChange={handleSearchChange} />
          <button onClick={handleSubmit}>Поиск</button>
        </div>
        <div className="employee-list">
          <h2>Список сотрудников</h2>
          {/* Здесь будет список сотрудников */}
        </div>
      </div>
    </div>
  );
};

export default SearchEmployPage;