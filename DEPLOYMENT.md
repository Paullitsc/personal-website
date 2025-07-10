# Deployment Guide

This guide will walk you through deploying your hybrid website using GitHub Pages for the frontend and Render for the backend.

## Prerequisites

1. **GitHub Account**: For hosting your code and frontend
2. **Render Account**: For hosting your Flask backend
3. **Gmail Account**: For sending emails from your contact form

## Step 1: Prepare Your Repository

### 1.1 Initialize Git Repository
```bash
git init
git add .
git commit -m "Initial commit"
```

### 1.2 Create GitHub Repository
1. Go to [GitHub](https://github.com) and create a new repository
2. Name it something like `personal-website`
3. Make it public (required for GitHub Pages)
4. Don't initialize with README (you already have one)

### 1.3 Push to GitHub
```bash
git remote add origin https://github.com/yourusername/personal-website.git
git branch -M main
git push -u origin main
```

## Step 2: Deploy Frontend (GitHub Pages)

### 2.1 Enable GitHub Pages
1. Go to your repository on GitHub
2. Click **Settings** tab
3. Scroll down to **Pages** section (in the left sidebar)
4. Under **Source**, select **Deploy from a branch**
5. Choose **main** branch and **/** (root) folder
6. Click **Save**

### 2.2 Access Your Site
Your site will be available at:
`https://yourusername.github.io/personal-website`

## Step 3: Deploy Backend (Render)

### 3.1 Create Render Account
1. Go to [Render](https://render.com)
2. Sign up with your GitHub account
3. Verify your email

### 3.2 Create New Web Service
1. Click **New +** → **Web Service**
2. Connect your GitHub repository
3. Select your repository

### 3.3 Configure the Service
- **Name**: `your-website-backend` (or any name you prefer)
- **Environment**: `Python 3`
- **Build Command**: `pip install -r contact-backend/requirements.txt`
- **Start Command**: `cd contact-backend && gunicorn app:app`
- **Plan**: Free

### 3.4 Add Environment Variables
Click **Environment** tab and add:
- **Key**: `MAIL_USERNAME`
- **Value**: Your Gmail address

- **Key**: `MAIL_PASSWORD`
- **Value**: Your Gmail app password (see Gmail setup below)

### 3.5 Deploy
Click **Create Web Service**. Render will automatically deploy your app.

### 3.6 Get Your Backend URL
After deployment, you'll get a URL like:
`https://your-website-backend.onrender.com`

## Step 4: Update Frontend to Use Backend

### 4.1 Update Contact Form URL
1. In your `index.html`, find the contact form
2. Replace the action URL with your Render backend URL:
```html
<form class="contact-form" action="https://your-website-backend.onrender.com/contact" method="POST" target="_blank">
```

### 4.2 Push Changes
```bash
git add .
git commit -m "Update backend URL"
git push
```

GitHub Pages will automatically redeploy with the new backend URL.

## Step 5: Gmail Setup (for Contact Form)

### 5.1 Enable 2-Factor Authentication
1. Go to your Google Account settings
2. Enable 2-Factor Authentication

### 5.2 Generate App Password
1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Under "Signing in to Google", click **App passwords**
3. Generate a new app password for "Mail"
4. Use this password in your Render environment variables

## Step 6: Test Your Deployment

### 6.1 Test Frontend
1. Visit your GitHub Pages URL
2. Verify all sections load correctly
3. Test responsive design on mobile

### 6.2 Test Backend
1. Fill out the contact form on your website
2. Submit the form
3. Check if you receive the email
4. Check Render logs if there are issues

## Troubleshooting

### Frontend Issues
- **Images not loading**: Check file paths are correct
- **Styling issues**: Clear browser cache
- **GitHub Pages not updating**: Wait a few minutes, check repository settings

### Backend Issues
- **Email not sending**: Check environment variables in Render
- **App not starting**: Check Render logs for Python errors
- **CORS issues**: Add CORS headers to Flask app if needed

### Common Render Issues
- **Build fails**: Check requirements.txt syntax
- **App crashes**: Check gunicorn command and app.py structure
- **Environment variables**: Ensure they're set correctly in Render dashboard

## Maintenance

### Updates
1. Make changes locally
2. Test locally first
3. Push to GitHub
4. Frontend updates automatically
5. Backend redeploys automatically

### Monitoring
- Check Render dashboard for backend status
- Monitor GitHub Pages deployment status
- Test contact form periodically

## Cost
- **GitHub Pages**: Free
- **Render**: Free tier (750 hours/month)
- **Gmail**: Free (with app password)

## Security Notes
- Never commit environment variables to Git
- Use app passwords, not your main Gmail password
- Consider adding rate limiting to your contact form
- Regularly update dependencies

## Next Steps
- Add a custom domain
- Set up analytics
- Add a blog system
- Implement caching
- Add SSL certificate (included with both platforms) 