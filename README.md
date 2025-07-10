# Paul Litscher - Personal Website

A personal portfolio website built with HTML, CSS, JavaScript, and a Flask backend for contact form handling.

## Project Structure

```
├── index.html          # Main website
├── styles.css          # Main stylesheet
├── script.js           # Main JavaScript
├── images/             # Image assets
├── blog/               # Blog section
├── contact-backend/    # Flask backend for contact form
│   ├── app.py         # Flask application
│   └── requirements.txt # Python dependencies
└── README.md          # This file
```

## Deployment

This project uses a hybrid deployment approach:
- **Frontend**: GitHub Pages (static hosting)
- **Backend**: Render (Flask API)

### Frontend Deployment (GitHub Pages)

1. Push your code to GitHub
2. Go to repository Settings → Pages
3. Select "Deploy from a branch"
4. Choose `main` branch and `/` (root) folder
5. Your site will be available at `https://yourusername.github.io/repository-name`

### Backend Deployment (Render)

1. Create a `requirements.txt` file in the `contact-backend/` directory
2. Push to GitHub
3. Connect your repository to Render
4. Create a new Web Service
5. Set build command: `pip install -r requirements.txt`
6. Set start command: `gunicorn app:app`
7. Add environment variables for email configuration

## Local Development

### Frontend
Simply open `index.html` in your browser or use a local server:
```bash
python -m http.server 8000
```

### Backend
```bash
cd contact-backend
pip install -r requirements.txt
python app.py
```

## Environment Variables

For the Flask backend, you'll need to set these environment variables:
- `MAIL_USERNAME`: Your Gmail address
- `MAIL_PASSWORD`: Your Gmail app password

## Features

- Responsive design
- Contact form with email backend
- Project showcase
- Blog section
- Modern UI with smooth animations