# 🚀 Render Deployment Guide

Complete guide to deploy your Contact Book Django application to Render.

## ✅ Pre-Deployment Checklist

- [x] Django project configured
- [x] Contact model and views working
- [x] Templates and static files ready
- [x] `render.yaml` created
- [x] `build.sh` created
- [x] `requirements.txt` updated with gunicorn
- [x] `.gitignore` configured
- [x] PostgreSQL database support configured

## 📋 Deployment Steps

### 1. Prepare Your Repository

1. **Make sure all changes are committed:**
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

### 2. Create Render Account

1. Go to [https://render.com/](https://render.com/)
2. Click **"Get Started"**
3. Sign up with GitHub (recommended for easy deployment)

### 3. Create PostgreSQL Database

1. From Render Dashboard, click **"New +"** → **"PostgreSQL"**
2. Configure database:
   - **Name**: `contact-book-db`
   - **Database**: `contact_book`
   - **User**: `contact_book_user`
   - **Region**: Choose closest to your users
   - **Plan**: **Free** (perfect for development)
3. Click **"Create Database"**
4. Wait for database to be provisioned (~2-3 minutes)
5. **Important**: Copy the **Internal Database URL** (starts with `postgresql://`)
   - You can find it in the database info page
   - Format: `postgresql://user:password@host:5432/database`

### 4. Create Web Service

#### Option A: Using render.yaml (Recommended - Automated)

1. Click **"New +"** → **"Blueprint"**
2. Connect your GitHub repository
3. Render will detect `render.yaml` and auto-configure
4. Set environment variables:
   - `DATABASE_URL`: Paste the Internal Database URL from step 3
   - `SECRET_KEY`: Auto-generated (or create your own)
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: Will be auto-configured
5. Click **"Apply"**

#### Option B: Manual Setup

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Configure service:
   - **Name**: `contact-book`
   - **Region**: Same as database
   - **Branch**: `main` (or `master`)
   - **Runtime**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn contactbook_project.wsgi:application`
   - **Plan**: **Free**

4. **Add Environment Variables:**
   Click **"Advanced"** → **"Add Environment Variable"**
   
   Add these variables:
   ```
   DATABASE_URL = <paste your PostgreSQL Internal Database URL>
   SECRET_KEY = <generate a random secret key>
   DEBUG = False
   PYTHON_VERSION = 3.12.0
   ```

5. Click **"Create Web Service"**

### 5. Generate Secret Key

To generate a secure SECRET_KEY, run this locally:

```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Or use this online: [Djecrety](https://djecrety.ir/)

### 6. Wait for Deployment

- Render will automatically:
  - Install dependencies from `requirements.txt`
  - Collect static files
  - Run database migrations
  - Start the application with Gunicorn

- Check the **Logs** tab to monitor progress
- First deployment takes ~5-10 minutes

### 7. Access Your Application

Once deployed, your app will be available at:
```
https://contact-book-xxxx.onrender.com
```

(Replace `xxxx` with your actual Render service identifier)

## 🔧 Post-Deployment Configuration

### Create Superuser (Admin Access)

1. Go to your Render service dashboard
2. Click **"Shell"** tab
3. Run:
   ```bash
   python manage.py createsuperuser
   ```
4. Follow prompts to create admin account
5. Access admin at: `https://your-app.onrender.com/admin/`

### Custom Domain (Optional)

1. Go to your web service settings
2. Click **"Custom Domain"**
3. Add your domain and follow DNS instructions

## 🔄 Continuous Deployment

Render automatically deploys when you push to GitHub:

```bash
git add .
git commit -m "Update feature"
git push origin main
```

Render will detect changes and redeploy automatically!

## 📊 Monitoring & Logs

- **Logs**: View real-time logs in the Render dashboard
- **Metrics**: Monitor CPU, memory usage in the Metrics tab
- **Health Checks**: Render automatically monitors your app

## 🐛 Troubleshooting

### Common Issues

**1. Build Failed**
- Check `build.sh` has execute permissions
- Verify `requirements.txt` is correct
- Check logs for specific error

**2. Database Connection Error**
- Verify `DATABASE_URL` is set correctly
- Use **Internal Database URL**, not external
- Ensure database and web service are in same region

**3. Static Files Not Loading**
- Run `python manage.py collectstatic` in shell
- Verify `STATIC_ROOT` in settings.py
- Check WhiteNoise is configured

**4. Application Timeout**
- Free tier services sleep after 15 min of inactivity
- First request after sleep takes ~30 seconds

### Run Commands Manually

Access Shell from Render dashboard:
```bash
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py createsuperuser
```

## 💰 Render Free Tier Limits

- ✅ 750 hours/month (enough for 1 service 24/7)
- ✅ Automatic HTTPS
- ✅ Free PostgreSQL database (90 days, then expires)
- ⚠️ Services sleep after 15 minutes of inactivity
- ⚠️ 512 MB RAM limit

## 🔒 Security Best Practices

1. ✅ Never commit `.env` file
2. ✅ Use strong SECRET_KEY
3. ✅ Set DEBUG=False in production
4. ✅ Keep dependencies updated
5. ✅ Use environment variables for sensitive data

## 📚 Additional Resources

- [Render Django Documentation](https://render.com/docs/deploy-django)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)
- [Render Community Forum](https://community.render.com/)

## 🎉 Success!

Your Contact Book is now live on Render! 🚀

Visit your app and start managing contacts from anywhere in the world.

Need help? Check the Render dashboard logs or documentation.
