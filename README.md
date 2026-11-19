# Dear Diary ♡

A personal journaling web application built with Django, designed to help users record their thoughts, preserve memories, and reflect on their emotions.

## 🌷 About the Project

Dear Diary is a web-based journaling application that provides users with a personal space to write and manage diary entries. It includes mood tracking and visual mood analytics to help users reflect on their emotional journey.

The project is being developed as a learning experience to explore full-stack web development and gradually integrate AI-powered features.

## ✨ Features

- **User Authentication:** Sign up, log in, and log out.
- **Create Diary Entries:** Write and save personal thoughts and memories.
- **Manage Entries:** View, edit, and delete diary entries.
- **Mood Tracking:** Associate moods with diary entries.
- **Mood Analytics:** Visualize mood distribution across the latest seven diary entries using a doughnut chart.
- **Image Uploads:** Attach images to diary entries.
- **Search Memories:** Search diary entries using keywords.

## 🛠️ Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Visualization:** Chart.js
- **Version Control:** Git and GitHub

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Reema-Sherin/dear-diary.git
cd dear-diary
```

### 2. Create a virtual environment

```bash
python -m venv env
```

Activate it on Windows:

```bash
env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Set up your own local environment variables, including the Django `SECRET_KEY`. Do not upload your `.env` file or share secret credentials.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## 🔮 Future Enhancements

The following features are planned for future development:

- AI Best Friend – an AI-powered journaling companion.
- Ask Your Diary – search and retrieve information from previous diary entries using natural language.
- Voice journaling and speech-to-text.
- To-do list with in-app reminders.
- Personal achievements and milestones scrapbook.
- Enhanced privacy and security features.

## 📌 Project Status

Currently under active development. New features and improvements are being added progressively.

## 👩‍💻 Developer

**Reema Sherin**

B.Tech Computer Science and Engineering Student

[GitHub Profile](https://github.com/Reema-Sherin)
