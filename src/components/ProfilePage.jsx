import React, { useState } from 'react';
import '../assets/ProfilePage.css';

const ProfilePage = () => {
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState({
    firstName: 'Иван',
    lastName: 'Иванов',
    middleName: 'Иванович',
    alias: 'nickname',
    vkLink: 'https://vk.com/id',
    about: 'Всем привет! Я Иванов Иван Иванович, молодой DevOps из г. Воронеж. В данной компании я принимал участие в таких проектах как: Name1, Name2, Name3. Закончил какой-то государственный ВУЗ, в общем я сюда напишу хоть что-то, чтобы можно было заполнить место, так как я сейчас не в силах что-то сгенерировать сам. Сюда тоже можно какую-то информацию добавить, в общем надо будет посмотреть как оно работает уже на стадии разработки. Надеюсь нам получится довести это всё до конца.',
    gender: 'мужской',
    telegramLink: 'https://t.me/id',
    city: 'Воронеж',
    email: 'example@mail.ru',
    birthDate: '01.01.2000',
    position: 'DevOps',
    phone: '+7 (8)ХО ХХХ-ХХ-ХХ',
    oldPassword: '',
    newPassword: '',
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setIsEditing(false);
    // Здесь вы можете добавить логику для сохранения данных
    console.log('Form data submitted:', formData);
  };

  const toggleEditMode = () => {
    setIsEditing(!isEditing);
  };

  return (
    <div className="profile-page">
      <div className="profile-card">
        <h1>Личный профиль</h1>
        {isEditing ? (
          <form onSubmit={handleSubmit}>
            <div className="profile-info">
              <div className="profile-image">
                <label htmlFor="imageUpload">Загрузить изображение</label>
                <input type="file" id="imageUpload" name="imageUpload" />
              </div>
              <div className="profile-fields">
                <div className="form-group">
                  <label htmlFor="firstName">Имя</label>
                  <input type="text" id="firstName" name="firstName" value={formData.firstName} onChange={handleChange} />
                </div>
                <div className="form-group">
                  <label htmlFor="lastName">Фамилия</label>
                  <input type="text" id="lastName" name="lastName" value={formData.lastName} onChange={handleChange} />
                </div>
                <div className="form-group">
                  <label htmlFor="middleName">Отчество</label>
                  <input type="text" id="middleName" name="middleName" value={formData.middleName} onChange={handleChange} />
                </div>
                <div className="form-group">
                  <label htmlFor="alias">Псевдоним</label>
                  <input type="text" id="alias" name="alias" value={formData.alias} onChange={handleChange} />
                </div>
                <div className="form-group">
                  <label htmlFor="vkLink">Ссылка на VK</label>
                  <input type="text" id="vkLink" name="vkLink" value={formData.vkLink} onChange={handleChange} />
                </div>
                <div className="form-group">
                  <label htmlFor="about">О себе</label>
                  <textarea id="about" name="about" value={formData.about} onChange={handleChange} />
                </div>
                <div className="form-group">
                  <label htmlFor="gender">Пол</label>
                  <input type="text" id="gender" name="gender" value={formData.gender} onChange={handleChange} />
                </div>
                <div className="form-group">
                  <label htmlFor="telegramLink">Ссылка на Telegram</label>
                  <input type="text" id="telegramLink" name="telegramLink" value={formData.telegramLink} onChange={handleChange} />
                </div>
                <div className="form-group">
                  <label htmlFor="city">Город</label>
                  <input type="text" id="city" name="city" value={formData.city} onChange={handleChange} />
                </div>
                <div className="form-group">
                  <label htmlFor="email">Почта</label>
                  <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} />
                </div>
                <div className="form-group">
                  <label htmlFor="birthDate">Дата рождения</label>
                  <input type="text" id="birthDate" name="birthDate" value={formData.birthDate} onChange={handleChange} />
                </div>
                <div className="form-group">
                  <label htmlFor="position">Должность</label>
                  <input type="text" id="position" name="position" value={formData.position} onChange={handleChange} />
                </div>
                <div className="form-group">
                  <label htmlFor="phone">Номер телефона</label>
                  <input type="text" id="phone" name="phone" value={formData.phone} onChange={handleChange} />
                </div>
              </div>
            </div>
            <div className="change-password">
              <h2>Хотите сменить пароль?</h2>
              <div className="form-group">
                <label htmlFor="oldPassword">Старый пароль</label>
                <input type="password" id="oldPassword" name="oldPassword" value={formData.oldPassword} onChange={handleChange} />
              </div>
              <div className="form-group">
                <label htmlFor="newPassword">Новый пароль</label>
                <input type="password" id="newPassword" name="newPassword" value={formData.newPassword} onChange={handleChange} />
              </div>
            </div>
            <button type="submit" className="save-button">Сохранить изменения</button>
          </form>
        ) : (
          <div className="profile-view">
            <div className="profile-header">
              <h2>{formData.lastName} {formData.firstName} {formData.middleName}</h2>
              <p>{formData.position}, {formData.birthDate.split('.')[2]} год., г. {formData.city}</p>
              <p>@{formData.alias}</p>
              <p>Проекты в которых принимает участие: [Name1], [Name2], [Name3].</p>
              <p>Офис: ул. Наименования, д. 123, этаж 7, кабинет 34</p>
              
            </div>
            <div className="profile-details">
              <div className="contact-info">
                <h3>Контактная информация</h3>
                <p>Номер телефона: {formData.phone}</p>
                <p>Почта: {formData.email}</p>
                <p>VK профиль: <a href={formData.vkLink}>{formData.vkLink}</a></p>
                <p>Telegram: <a href={formData.telegramLink}>{formData.telegramLink}</a></p>
              </div>
              <div className="general-info">
                <h3>Общие данные</h3>
                <p>Опыт работы: X лет</p>
                <p>Дата рождения: {formData.birthDate}</p>
                <p>Пол: {formData.gender}</p>
              </div>
              <div className="about-info">
                <h3>О себе</h3>
                <p>{formData.about}</p>
                
              </div>
              
            </div>
            <button onClick={toggleEditMode} className="edit-button">Редактировать профиль</button>
          </div>
        )}
      </div>
    </div>
  );
};

export default ProfilePage;