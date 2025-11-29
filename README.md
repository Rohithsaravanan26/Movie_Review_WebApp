# 🎬 CineScope – Django Movie Review App

CineScope is a single-page **movie review** web application built with **Django**.  
Users can browse movies, view ratings, and submit reviews – all from one sleek, responsive page.

---

## ✨ Features

- 📝 Add reviews for movies (name, rating, comment)
- ⭐ Interactive star rating (1–5)
- 🎞️ Movie list with average rating and review count
- ⚡ Single-page UX using AJAX (no full page reload)
- 🎨 Modern, attractive UI (pure HTML + CSS + a bit of JS)
- 🛡️ CSRF-protected POST requests
- 🛠️ Django admin to manage movies and reviews

---

## 🗂 Project Structure

```bash
Movie/
├─ manage.py
├─ moviereview/
│  ├─ __init__.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ asgi.py
│  └─ wsgi.py
├─ reviews/
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ models.py
│  ├─ urls.py
│  └─ views.py
└─ templates/
   └─ index.html
```
🚀 Getting Started (Local Setup)
1️⃣ Clone the repository
bash
```
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```
2️⃣ Create and activate a virtual environment
bash
Copy code
# Create venv
```
python -m venv .venv
```
# Activate (Windows PowerShell)
```
.\.venv\Scripts\Activate.ps1
```
# Activate (Windows CMD)
```
.\.venv\Scripts\activate.bat
```
# Activate (Linux/macOS)
```
source .venv/bin/activate
```
3️⃣ Install dependencies
If you have a requirements.txt:

bash
```
Copy code
pip install -r requirements.txt
```
Or just install Django:
bash
Copy code
```
pip install django
```
4️⃣ Apply migrations
bash
Copy code
```
python manage.py makemigrations
python manage.py migrate
```
5️⃣ Create a superuser (for Django admin)
bash
Copy code
```
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

6️⃣ Run the development server
bash
Copy code
python manage.py runserver
Open your browser and visit:

App: http://127.0.0.1:8000/

Admin: http://127.0.0.1:8000/admin/

🧩 Usage
Add Movies
Go to /admin/ and log in with your superuser account.

Create one or more Movie entries:

Title

Tagline (optional)

Description (optional)

Release date

Poster URL (optional image URL)

Genre

Add Reviews
Go to the main page /.

Select a movie in the dropdown.

Enter:

Your name

Rating (click the stars)

Your review text

Click Post review.

The review is submitted via AJAX and appears instantly under that movie.

🏗️ Tech Stack
Backend: Django (Python)

Database: SQLite (default, for development)

Frontend: HTML, CSS, vanilla JavaScript

Admin Panel: Django Admin

⚙️ Important Files
moviereview/settings.py
Registers the reviews app in INSTALLED_APPS.

Configures the global templates/ directory.

Uses SQLite as the default database.

reviews/models.py
Defines two models:

Movie – title, tagline, description, release_date, poster_url, genre, etc.

Review – ForeignKey to Movie, name, rating, comment, created_at.

reviews/views.py
home – renders index.html with all movies and reviews.

add_review – AJAX endpoint to create a new review and return updated data as JSON.

templates/index.html
Single-page UI

Uses Django template language to loop over movies and reviews.

Uses JavaScript fetch() to post reviews asynchronously.

📝 Example Environment (Dev)
This project is designed for development with:

Python 3.10+ (recommended)

Django 5.x (or 4.x – adjust as needed)

SQLite (no extra config needed)

🌐 Deployment Notes
This is a classic Django app and requires a Python server.
You cannot run Django directly on GitHub Pages (static hosting only).

Typical deployment options:

Render

Railway

Heroku (if available)

Any VPS (Ubuntu + gunicorn + nginx)

Basic steps for deployment usually include:

Pushing the code to GitHub.

Creating a requirements.txt:

bash
Copy code
```
pip freeze > requirements.txt
```
Using gunicorn as the WSGI server:

text
Copy code
```
web: gunicorn moviereview.wsgi:application
Setting DEBUG = False and configuring ALLOWED_HOSTS.
```
✅ To-Do / Possible Improvements
✅ Pagination or infinite scroll for reviews

✅ Add search / filter for movies

✅ Add authentication and user profiles

✅ Dockerize the project for easier deployment

✅ Switch to PostgreSQL in production

🤝 Contributing
Pull requests and suggestions are welcome!

Fork the repo

Create a new branch: git checkout -b feature/my-feature

Commit your changes: git commit -m "Add awesome feature"

Push the branch: git push origin feature/my-feature

Open a Pull Request

📄 License

MIT License – feel free to use and modify this project for learning or personal projects.
