# DreamEvent 🎉

**DreamEvent** is an event planning web platform where users can explore services and book personalized events. Whether it’s a wedding, birthday, or corporate function — DreamEvent helps users plan and organize memorable experiences with ease.

---

## ✨ Features

- 🔍 Explore a wide range of event planning services
- 🗓 Book customized events online
- 📋 Event details and service categories
- 🧑 User-friendly interface for browsing and booking
- 🛠 Admin dashboard for managing services and events *(optional)*

---

## 💻 Tech Stack

### 🔧 Backend:
- Python 3.x
- Django Framework
- SQLite Database

### 🎨 Frontend:
- HTML5
- CSS3
- JavaScript

---

## 🚀 Getting Started

### 1. Clone the Repository
git clone https://github.com/mesh2107/DreamEvent.git
cd DreamEvent

2. Create and Activate a Virtual Environment (Recommended)
python -m venv env
# On Windows
env\Scripts\activate
# On macOS/Linux
source env/bin/activate

3. Install Dependencies
pip install -r requirements.txt
4. Apply Migrations
python manage.py migrate

5. Collect Static Files
python manage.py collectstatic --noinput
6. Run the Development Server
python manage.py runserver
