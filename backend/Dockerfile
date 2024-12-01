# Используем официальный образ Python версии 3.12 в качестве базового
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем текущую директорию в контейнер в /app
COPY . /app

# Устанавливаем зависимости
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install

# Открываем порт, на котором будет работать приложение
EXPOSE 8000

# Запускаем приложение
CMD ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

