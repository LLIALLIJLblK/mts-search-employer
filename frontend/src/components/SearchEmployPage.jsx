import React, { useState, useEffect } from 'react';
import axios from 'axios';
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
  const [users, setUsers] = useState([]);
  const [filteredUsers, setFilteredUsers] = useState([]);
  const [appliedFilters, setAppliedFilters] = useState('');
  const [selectedGender, setSelectedGender] = useState('');
  const [selectedUser, setSelectedUser] = useState(null);

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const response = await axios.get('http://localhost/filters/users/search');
      setUsers(response.data);
      setFilteredUsers(response.data);
    } catch (error) {
      console.error('Error fetching users:', error);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSearchChange = (e) => {
    setSearchQuery(e.target.value);
    filterUsers(e.target.value, selectedGender);
  };

  const handleGenderChange = (e) => {
    setSelectedGender(e.target.value);
    filterUsers(searchQuery, e.target.value);
  };

  const filterUsers = (query, gender) => {
    const filtered = users.filter(user => {
      const fullName = `${user.last_name} ${user.first_name} ${user.father_name}`.toLowerCase();
      const genderMatch = gender ? user.sex === gender : true;
      return fullName.includes(query.toLowerCase()) && genderMatch;
    });
    setFilteredUsers(filtered);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Здесь вы можете добавить логику для обработки данных формы
    console.log('Form data submitted:', formData);
    setAppliedFilters(`Воронеж 18-30`); // Пример примененных фильтров
  };

  const handleUserClick = async (userId) => {
    try {
      const response = await axios.get(`http://localhost/filters/users/${userId}`);
      setSelectedUser(response.data);
    } catch (error) {
      console.error('Error fetching user details:', error);
    }
  };

  const closeModal = () => {
    setSelectedUser(null);
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
            <select id="gender" name="gender" value={selectedGender} onChange={handleGenderChange}>
              <option value="">Выберите пол</option>
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
          {appliedFilters && <p>Примененные фильтры: {appliedFilters}</p>}
          {filteredUsers.map(user => (
            <div key={user.id} className="employee-card" onClick={() => handleUserClick(user.id)}>
              <h3>{user.last_name} {user.first_name} {user.father_name}</h3>
              <p>{user.about_user || 'Информация отсутствует'}</p>
            </div>
          ))}
        </div>
      </div>
      {selectedUser && (
        <div className="modal">
          <div className="modal-content">
            <span className="close" onClick={closeModal}>&times;</span>
            <h2>{selectedUser.user.last_name} {selectedUser.user.first_name} {selectedUser.user.father_name}</h2>
            <p><strong>Email:</strong> {selectedUser.user.email}</p>
            <p><strong>Телефон:</strong> {selectedUser.user.phone_number || 'Не указан'}</p>
            <p><strong>Пол:</strong> {selectedUser.user.sex || 'Не указан'}</p>
            <p><strong>Дата рождения:</strong> {selectedUser.user.birthday || 'Не указана'}</p>
            <p><strong>Дата начала работы:</strong> {selectedUser.user.date_of_start_work || 'Не указана'}</p>
            <p><strong>О себе:</strong> {selectedUser.user.about_user || 'Не указано'}</p>
            <p><strong>Департамент:</strong> {selectedUser.departament.title}</p>
            <p><strong>Команда:</strong> {selectedUser.team ? selectedUser.team.title : 'Не указана'}</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default SearchEmployPage;