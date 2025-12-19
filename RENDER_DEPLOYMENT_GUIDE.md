# 🚀 Deploying to Render - Troubleshooting Guide

## Why Your Changes Aren't Showing on Render

When you push to GitHub but don't see changes on Render, here are the common reasons:

### 1. **Auto-Deploy Needs Time**
Render auto-deploys when you push to GitHub, but it takes 5-10 minutes.

### 2. **Manual Deploy Required**
Sometimes auto-deploy doesn't trigger. You need to manually deploy.

### 3. **Database Migrations Not Run**
New models (like UserLoginInfo) need migrations to be applied.

### 4. **Static Files Not Collected**
CSS changes need to be collected and served.

---

## ✅ Step-by-Step Deployment Process

### **Option 1: Wait for Auto-Deploy (Recommended)**

1. **Check Render Dashboard:**
   - Go to: https://dashboard.render.com
   - Select your `contact-book` service
   - Look for "Events" tab
   - You should see "Deploy triggered from GitHub"

2. **Wait for Deployment:**
   - Watch the build logs
   - Wait for "Deploy live" message
   - Usually takes 5-10 minutes

3. **Verify Build Steps:**
   - Installing dependencies
   - Running `build.sh`
   - Collecting static files
   - Running migrations
   - Starting gunicorn

### **Option 2: Manual Deploy (If Auto-Deploy Fails)**

1. **Go to Render Dashboard:**
   ```
   https://dashboard.render.com
   ```

2. **Select Your Service:**
   - Click on `contact-book` service

3. **Trigger Manual Deploy:**
   - Click "Manual Deploy" button (top right)
   - Select "Deploy latest commit"
   - Click "Deploy"

4. **Watch Build Logs:**
   - Click on the deployment in Events tab
   - Watch logs for any errors

---

## 🔍 Check Deployment Status

### In Render Dashboard:

**1. Events Tab:**
- Shows all deployments
- Check if latest commit deployed
- Look for "Deploy live" status

**2. Logs Tab:**
- Shows runtime logs
- Check for errors
- Verify migrations ran

**3. Environment Tab:**
- Verify environment variables:
  - `DEBUG` = False
  - `SECRET_KEY` = (generated)
  - `ALLOWED_HOSTS` = (set)
  - `DATABASE_URL` = (auto-set)

---

## ⚠️ Common Issues & Fixes

### **Issue 1: Migrations Not Applied**

**Symptom:** Error about missing tables (UserLoginInfo)

**Fix:** Run migrations manually in Render Shell:

1. Go to your service in Render
2. Click "Shell" tab
3. Run:
   ```bash
   python manage.py migrate
   ```

### **Issue 2: Static Files Not Loading**

**Symptom:** No CSS styling, broken layout

**Fix:** Collect static files:

1. In Render Shell:
   ```bash
   python manage.py collectstatic --no-input
   ```

2. Or redeploy (triggers build.sh)

### **Issue 3: New Dependencies Not Installed**

**Symptom:** Import errors (user-agents module)

**Fix:**
- Ensure `requirements.txt` was pushed
- Trigger manual deploy
- Check build logs for pip install output

### **Issue 4: Database Connection Error**

**Symptom:** Can't connect to database

**Fix:**
1. Check `DATABASE_URL` environment variable
2. Verify database service is running
3. Check if database plan has enough connections

### **Issue 5: Template Not Found**

**Symptom:** Error about missing templates

**Fix:**
1. Verify `templates/` folder pushed to GitHub
2. Check `TEMPLATES` `DIRS` in settings.py:
   ```python
   'DIRS': [BASE_DIR / 'templates'],
   ```

---

## 🛠️ Manual Deployment Checklist

Before deploying, verify:

- [ ] All changes committed to git
- [ ] All changes pushed to GitHub
- [ ] `requirements.txt` includes `user-agents>=2.2.0`
- [ ] `build.sh` runs collectstatic and migrate
- [ ] `settings.py` has correct TEMPLATES DIRS
- [ ] Database migrations created locally
- [ ] Static files collected locally (test)

---

## 📋 Render Shell Commands (If Needed)

Access Render Shell from dashboard, then run:

```bash
# 1. Check Python packages installed
pip list | grep user-agents

# 2. Run migrations
python manage.py migrate

# 3. Collect static files
python manage.py collectstatic --no-input

# 4. Create superuser (if needed)
python manage.py createsuperuser

# 5. Check database
python manage.py dbshell

# 6. List migrations
python manage.py showmigrations

# 7. Check settings
python manage.py diffsettings
```

---

## 🔄 Force Redeploy

If nothing works, force a complete redeploy:

### Method 1: Clear Build Cache

1. Go to service Settings
2. Scroll to "Build & Deploy"
3. Click "Clear build cache"
4. Click "Manual Deploy" → "Clear build cache & deploy"

### Method 2: Make a Dummy Commit

```bash
# Add a comment to README
echo "# Deploy trigger" >> README.md
git add README.md
git commit -m "Trigger Render redeploy"
git push origin master
```

### Method 3: Redeploy from Render

1. In Render dashboard
2. Events tab
3. Find successful previous deploy
4. Click "Redeploy"

---

## ✅ Verification Steps

After deployment, verify these work:

1. **Visit your Render URL:**
   ```
   https://contact-book-xxxx.onrender.com
   ```

2. **Test Login Page:**
   - Should show styled login form
   - Try logging in with username

3. **Check Login History:**
   - Log in
   - Navigate to Login History
   - Should see stats cards and styled table

4. **Test Signup:**
   - Create new account with username
   - Should require username + email + password

5. **Check Admin:**
   - Go to `/admin/`
   - Login with superuser
   - Check "User Login Info" model exists

---

## 🐛 Debug Deployment Issues

### Check Build Logs:

Look for these in Render build logs:

```
✓ Installing dependencies from requirements.txt
✓ Collecting static files
✓ Running migrations
✓ Starting gunicorn
```

### Common Error Messages:

**1. "ModuleNotFoundError: No module named 'user_agents'"**
- **Fix:** Requirements.txt not updated or not installed
- **Action:** Redeploy

**2. "OperationalError: no such table: contacts_userlogininfo"**
- **Fix:** Migrations not run
- **Action:** Run `python manage.py migrate` in Shell

**3. "TemplateDoesNotExist at /accounts/login/"**
- **Fix:** Templates folder not in correct location
- **Action:** Verify TEMPLATES DIRS setting

**4. "Static file not found: contacts/css/style.css"**
- **Fix:** Static files not collected
- **Action:** Run collectstatic or redeploy

---

## 📊 Expected Build Output

Your Render build should show:

```bash
==> Building...
==> Running build command: './build.sh'
Collecting asgiref==3.10.0
Collecting dj-database-url==3.0.1
Collecting Django>=5.0,<5.1
...
Collecting user-agents>=2.2.0
Successfully installed ... user-agents-2.2.0
==> Collecting static files...
128 static files copied to '/opt/render/project/src/staticfiles'
==> Running migrations...
Operations to perform:
  Apply all migrations: account, admin, auth, contacts, contenttypes, sessions, sites, socialaccount
Running migrations:
  Applying contacts.0003_userlogininfo... OK
==> Build successful!
==> Deploying...
==> Deploy live at https://contact-book-xxxx.onrender.com
```

---

## 🎯 Quick Fix Summary

**If changes aren't showing:**

1. **Wait 10 minutes** - Auto-deploy takes time
2. **Check Render Dashboard** - Look for deployment status
3. **Manual Deploy** - Trigger if auto-deploy failed
4. **Check Logs** - Look for errors in Events tab
5. **Run Migrations** - Use Render Shell if needed
6. **Clear Cache** - Clear build cache and redeploy

---

## 💡 Pro Tips

1. **Always check Render Events tab** after pushing to GitHub
2. **Watch build logs in real-time** to catch errors early
3. **Keep Render Shell open** for quick debugging
4. **Test locally first** before deploying
5. **Use manual deploy** if auto-deploy is unreliable
6. **Check environment variables** if settings seem wrong

---

## 📞 Still Not Working?

If deployment still fails:

1. **Check Render Status:**
   - https://status.render.com
   - Verify no outages

2. **Review Render Docs:**
   - https://render.com/docs/deploy-django

3. **Check GitHub Integration:**
   - Settings → Connected Services
   - Verify GitHub connected

4. **Contact Render Support:**
   - Use in-dashboard chat
   - Provide deployment logs

---

## 🎉 Success Indicators

Your deployment is successful when:

- ✅ Build logs show "Deploy live"
- ✅ No errors in runtime logs
- ✅ Website accessible at Render URL
- ✅ Login page shows new styling
- ✅ Login History page works
- ✅ Username login works
- ✅ Admin shows UserLoginInfo model

---

*Last Updated: November 15, 2025*
