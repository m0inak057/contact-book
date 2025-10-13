# 🗄️ Supabase Database Setup Guide

This guide will help you set up Supabase PostgreSQL database for your Contact Book application.

## 📋 Step-by-Step Setup

### Step 1: Create Supabase Account

1. Go to [https://supabase.com/](https://supabase.com/)
2. Click **"Start your project"**
3. Sign up with GitHub, Google, or email
4. Verify your email if required

### Step 2: Create a New Project

1. Once logged in, click **"New Project"**
2. Fill in the project details:
   - **Name**: `contact-book` (or any name you prefer)
   - **Database Password**: Create a **strong password** (SAVE THIS!)
   - **Region**: Choose the region closest to you or your users
   - **Pricing Plan**: Select **"Free"** (perfect for this project)
3. Click **"Create new project"**
4. Wait 2-3 minutes for the database to be provisioned

### Step 3: Get Your Database Connection String

1. Once the project is ready, click on the **Settings** icon (⚙️) in the left sidebar
2. Navigate to **Database** in the settings menu
3. Scroll down to the **Connection String** section
4. You'll see multiple connection options:
   - **URI** ← Use this one!
   - Session mode
   - Transaction mode
   - Direct connection

5. Copy the **URI** connection string. It looks like:
   ```
   postgresql://postgres:[YOUR-PASSWORD]@db.xxxxxxxxxxxxxx.supabase.co:5432/postgres
   ```

6. **Important**: Replace `[YOUR-PASSWORD]` with your actual database password you set in Step 2

   Final format:
   ```
   postgresql://postgres:your_actual_password@db.xxxxxxxxxxxxxx.supabase.co:5432/postgres
   ```

### Step 4: Test Database Connection Locally

1. Open the `.env` file in your project root
2. Update the `DATABASE_URL` with your Supabase connection string:
   ```env
   DATABASE_URL=postgresql://postgres:your_actual_password@db.xxx.supabase.co:5432/postgres
   ```

3. Run migrations to create tables in Supabase:
   ```bash
   python manage.py migrate
   ```

4. If successful, you'll see output like:
   ```
   Operations to perform:
     Apply all migrations: admin, auth, contacts, contenttypes, sessions
   Running migrations:
     Applying contenttypes.0001_initial... OK
     Applying auth.0001_initial... OK
     ...
   ```

5. Create a superuser (optional but recommended):
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Test your app at `http://localhost:8000`

### Step 5: Verify Database in Supabase Dashboard

1. Go back to your Supabase project dashboard
2. Click on **Table Editor** in the left sidebar
3. You should see your Django tables:
   - `auth_user`
   - `contacts_contact`
   - `django_migrations`
   - etc.

4. Click on `contacts_contact` to see your contacts table structure

### Step 6: Configure for Vercel Deployment

When deploying to Vercel, you need to add the same `DATABASE_URL` as an environment variable:

1. Go to your Vercel project dashboard
2. Click on **Settings** > **Environment Variables**
3. Add a new variable:
   - **Key**: `DATABASE_URL`
   - **Value**: Your full Supabase connection string
   - **Environment**: Check all (Production, Preview, Development)
4. Click **Save**

## 🔒 Security Best Practices

### 1. Never Commit Your `.env` File
- The `.env` file is already in `.gitignore`
- Never share your database password publicly

### 2. Use Strong Passwords
- Use a password manager to generate strong passwords
- Minimum 16 characters with mixed case, numbers, and symbols

### 3. Rotate Credentials Regularly
- Change your database password periodically
- Update it in both `.env` and Vercel environment variables

### 4. Enable Row Level Security (RLS) - Optional
If you want extra security:
1. Go to Supabase Dashboard > Authentication
2. Enable RLS policies for your tables
3. Define who can read/write data

## 📊 Monitoring Your Database

### Check Database Usage
1. Go to Supabase Dashboard
2. Click on **Settings** > **Database**
3. View:
   - Database size
   - Connection count
   - Query performance

### Free Tier Limits
- **Database Size**: 500 MB
- **Bandwidth**: 5 GB
- **API Requests**: 500,000/month
- **Storage**: 1 GB

## 🔧 Troubleshooting

### Connection Refused Error
**Error**: `could not connect to server: Connection refused`

**Solution**:
1. Check if your IP is allowed (Supabase allows all by default)
2. Verify your password is correct (no special characters that need escaping)
3. Check your internet connection

### SSL Required Error
**Error**: `FATAL: no pg_hba.conf entry for host`

**Solution**:
Add `?sslmode=require` to your connection string:
```
postgresql://postgres:password@db.xxx.supabase.co:5432/postgres?sslmode=require
```

### Password Contains Special Characters
If your password has special characters like `@`, `#`, `!`, you need to URL-encode them:
- `@` → `%40`
- `#` → `%23`
- `!` → `%21`
- `&` → `%26`

Or use a password without special characters.

### Too Many Connections
**Error**: `FATAL: sorry, too many clients already`

**Solution**:
- Free tier allows max 60 connections
- Add `conn_max_age` to settings (already configured)
- Close unused connections

## 🎯 Testing Your Setup

Run this checklist to verify everything works:

- [ ] Supabase project created
- [ ] Database password saved securely
- [ ] Connection string copied and updated in `.env`
- [ ] `python manage.py migrate` runs successfully
- [ ] Can create a superuser
- [ ] Can view tables in Supabase Table Editor
- [ ] Local development server connects to Supabase
- [ ] Can add/edit/delete contacts through the app
- [ ] Data persists in Supabase (refresh table editor)

## 🚀 Switching Between SQLite and Supabase

### Use SQLite (Local Development)
Leave `DATABASE_URL` empty in `.env`:
```env
DATABASE_URL=
```

### Use Supabase (Production/Testing)
Add your Supabase connection string:
```env
DATABASE_URL=postgresql://postgres:password@db.xxx.supabase.co:5432/postgres
```

The app automatically switches based on the `DATABASE_URL` environment variable!

## 📚 Additional Resources

- [Supabase Documentation](https://supabase.com/docs)
- [Django Database Documentation](https://docs.djangoproject.com/en/5.2/ref/databases/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## 💡 Pro Tips

1. **Backup Your Data**: Supabase has automatic backups, but you can also export manually
2. **Use Supabase Studio**: Built-in SQL editor for running queries
3. **Monitor Logs**: Check Database > Logs for query performance
4. **Connection Pooling**: Already configured with `conn_max_age=600`

---

**Need Help?** Check the Supabase community or Django documentation for additional support.

**Ready to Deploy?** Once your database is set up and tested locally, follow the [DEPLOYMENT.md](DEPLOYMENT.md) guide to deploy to Vercel!
