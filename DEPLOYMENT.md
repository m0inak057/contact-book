# 🚀 Vercel Deployment Checklist

Follow these steps to deploy your Contact Book to Vercel:

## ✅ Pre-Deployment Checklist

- [x] Django project created
- [x] Contact model and views implemented
- [x] HTML templates created
- [x] CSS styling added
- [x] Static files configured
- [x] `vercel.json` created
- [x] `build_files.sh` created
- [x] `requirements.txt` generated
- [x] `.gitignore` created
- [x] `.env.example` created
- [x] Migrations run locally
- [x] Local testing completed

## 📋 Deployment Steps

### 1. Set Up Production Database

**Choose one of these options:**

#### Option A: Vercel Postgres (Easiest)
1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Create a new Postgres database
3. Copy the `DATABASE_URL` connection string

#### Option B: Neon (Free PostgreSQL)
1. Sign up at [Neon](https://neon.tech/)
2. Create a new project
3. Copy the connection string

#### Option C: Supabase (Free PostgreSQL)
1. Sign up at [Supabase](https://supabase.com/)
2. Create a new project
3. Go to Project Settings > Database
4. Copy the connection string

### 2. Update Dependencies for PostgreSQL

```bash
# Activate your virtual environment first
pip install dj-database-url psycopg2-binary
pip freeze > requirements.txt
```

### 3. Generate a New Secret Key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output - you'll need it for Vercel environment variables.

### 4. Initialize Git Repository

```bash
git init
git add .
git commit -m "Initial commit - Django Contact Book ready for deployment"
```

### 5. Create GitHub Repository

1. Go to [GitHub](https://github.com/)
2. Click "New Repository"
3. Name it (e.g., "contact-book-django")
4. Don't initialize with README (we already have one)
5. Copy the repository URL

### 6. Push Code to GitHub

```bash
git remote add origin <your-github-repo-url>
git branch -M main
git push -u origin main
```

### 7. Deploy to Vercel

1. Go to [Vercel](https://vercel.com/)
2. Click "Add New Project"
3. Import your GitHub repository
4. Configure project:
   - Framework Preset: **Other**
   - Root Directory: **./** (keep default)
   - Build Command: Leave empty
   - Output Directory: Leave empty

### 8. Add Environment Variables in Vercel

Click "Environment Variables" and add these:

| Name | Value | Environment |
|------|-------|-------------|
| `SECRET_KEY` | (your generated key from step 3) | Production, Preview, Development |
| `DEBUG` | `False` | Production, Preview |
| `DEBUG` | `True` | Development |
| `ALLOWED_HOSTS` | `.vercel.app` | Production, Preview, Development |
| `DATABASE_URL` | (your PostgreSQL connection string) | Production, Preview, Development |

### 9. Deploy!

Click the **"Deploy"** button and wait for the build to complete.

### 10. Run Migrations on Production

After deployment, you need to run migrations:

#### Method A: Using Python directly
1. Install and configure `psycopg2-binary`
2. Set the `DATABASE_URL` environment variable locally
3. Run: `python manage.py migrate`

#### Method B: Using Vercel CLI (Recommended)
```bash
# Install Vercel CLI
npm i -g vercel

# Login
vercel login

# Link to your project
vercel link

# Pull environment variables
vercel env pull .env.production

# Run migrations
python manage.py migrate
```

### 11. Create Superuser (Optional)

To access Django admin:

```bash
python manage.py createsuperuser
```

Enter username, email, and password when prompted.

### 12. Test Your Deployment

1. Visit your Vercel URL (e.g., `https://your-app.vercel.app`)
2. Test all features:
   - [ ] View contacts page loads
   - [ ] Can add a new contact
   - [ ] Can search for contacts
   - [ ] Can edit a contact
   - [ ] Can delete a contact
   - [ ] Static CSS files load correctly
3. Visit `/admin` to test Django admin

### 13. Configure Custom Domain (Optional)

1. In Vercel Dashboard, go to your project
2. Click "Settings" > "Domains"
3. Add your custom domain
4. Follow DNS configuration instructions
5. Update `ALLOWED_HOSTS` environment variable to include your domain

## 🔧 Troubleshooting

### Issue: Static files not loading
**Solution**: 
- Check that WhiteNoise is in `requirements.txt`
- Verify `STATICFILES_STORAGE` setting in `settings.py`
- Run `python manage.py collectstatic` locally to test

### Issue: Database connection errors
**Solution**:
- Verify `DATABASE_URL` is correct
- Check that PostgreSQL database is running
- Ensure database accepts connections from Vercel IPs

### Issue: "Bad Request (400)" error
**Solution**:
- Add your Vercel domain to `ALLOWED_HOSTS`
- Check that environment variables are set correctly

### Issue: CSRF verification failed
**Solution**:
- Add `CSRF_TRUSTED_ORIGINS = ['https://*.vercel.app']` in settings.py
- Make sure your domain is in `ALLOWED_HOSTS`

### Issue: Migrations not applied
**Solution**:
- Use Vercel CLI to run migrations
- Or connect directly to your PostgreSQL database and run migrations

## 📝 Post-Deployment Tasks

- [ ] Test all functionality thoroughly
- [ ] Set up monitoring (optional)
- [ ] Configure backups for your database
- [ ] Set up custom domain (optional)
- [ ] Add SSL certificate (Vercel does this automatically)
- [ ] Share your app with users!

## 🎉 Success!

Your Contact Book is now live on Vercel!

**Next Steps:**
- Share the URL with friends and family
- Consider adding authentication for multiple users
- Add more features like contact photos, tags, groups, etc.
- Set up CI/CD for automatic deployments

---

**Need Help?**
- Check the [README.md](README.md) for detailed documentation
- Visit [Vercel Documentation](https://vercel.com/docs)
- Check [Django Documentation](https://docs.djangoproject.com/)
