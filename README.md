# Paul Litscher - Personal Portfolio & Blog

A personal website and blog built with HTML, CSS, and JavaScript, featuring an AI-themed blog section and a Flask backend for contact form handling.

---

## 📁 Project Structure

```
├── index.html            # Main landing page
├── styles.css            # Main site stylesheet
├── script.js             # Main JavaScript (handles UI, contact form, etc.)
├── images/               # Image assets
├── blog/                 # Blog section (AI learning guide, posts, blog CSS)
│   ├── index.html        # Blog index
│   ├── ai-learning-guide.html  # AI learning guide post
│   └── ...               # Other blog posts & CSS
├── contact-backend/      # Flask backend for contact form
│   ├── app.py            # Flask application
│   └── venv/             # Python virtual environment (optional)
│   └── ...
├── requirements.txt      # Frontend dependencies (if any)
└── README.md             # This file
```

---

## 🚀 Deployment

### Frontend (Static Hosting)
- Can be hosted on GitHub Pages, Netlify, Vercel, or any static host.
- Just upload the contents of the root directory (excluding `contact-backend/`).

### Backend (Flask API for Contact Form)
- Deploy `contact-backend/app.py` to a service like Render, Heroku, or your own server.
- Make sure to set environment variables for email (see below).

---

## 🛠️ Local Development

### Frontend
Open `index.html` directly in your browser, or run a local server:
```bash
python -m http.server 8000
```

### Backend
```bash
cd contact-backend
pip install -r requirements.txt
python app.py
```

---

## ✉️ Contact Form Integration
- The contact form on the main page sends a POST request with JSON to the Flask backend.
- Make sure your backend is running and accessible at the URL specified in the form's `action` (default: Render deployment).
- The backend expects JSON with the following fields:
  - `name`, `email`, `subject`, `message`

---

## 🔑 Environment Variables (Backend)
Set these for email sending:
- `MAIL_USERNAME`: Your email address (e.g., Gmail)
- `MAIL_PASSWORD`: Your app password (not your main email password)

---

## ✨ Features
- Responsive, modern design
- AI-themed blog section (with beginner-friendly AI learning guide)
- Contact form with email backend (JSON POST)
- Project showcase
- Smooth animations and accessibility improvements

---

## 🧠 AI Blog Highlights
- Simple, non-technical breakdown of AI for beginners
- Learning path and resource recommendations
- Personal opinions and tips from Paul Litscher
- Custom AI-inspired theme for select blog posts

---

## 📣 Contributions & Feedback
This project is personal, but suggestions and feedback are welcome! Feel free to open an issue or contact me via the website.