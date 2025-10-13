# 📒 Contact Book - Django Web Application

A modern, full-featured contact management system built with Django and ready to deploy on Vercel.

## Features

- ➕ Create new contacts
- 📋 View all contacts in a responsive grid
- ✏️ Edit existing contacts
- 🗑️ Delete contacts with confirmation
- 🔍 Search contacts by name, phone, email, or address
- 📱 Responsive design for mobile and desktop
- 🎨 Modern UI with gradient background

## Tech Stack

- **Backend**: Django 5.2
- **Frontend**: HTML5, CSS3
- **Database**: SQLite (development), PostgreSQL (production)
- **Deployment**: Vercel

## Local Development Setup

### Prerequisites

- Python 3.12+
- pip
- Virtual environment (recommended)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd "CONTACT BOOK"
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Open your browser**
   Navigate to `http://localhost:8000`

## Deploying to Vercel

### Step 1: Prepare Your Database

Vercel doesn't support SQLite in production. You need a PostgreSQL database:

#### Option A: Vercel Postgres (Recommended)
1. Go to your Vercel project dashboard
2. Click on "Storage" tab
3. Create a new "Postgres" database
4. Copy the environment variables

#### Option B: External PostgreSQL
Use services like:
- [Neon](https://neon.tech/) (Free tier available)
- [Supabase](https://supabase.com/) (Free tier available)
- [Railway](https://railway.app/)
- [ElephantSQL](https://www.elephantsql.com/)

### Step 2: Update settings.py for Production Database

1. Install `dj-database-url`:
   ```bash
   pip install dj-database-url psycopg2-binary
   pip freeze > requirements.txt
   ```

2. Update `contactbook_project/settings.py`:
   ```python
   import dj_database_url
   
   # Add at the end of settings.py
   if not DEBUG:
       DATABASES = {
           'default': dj_database_url.config(
               default=config('DATABASE_URL'),
               conn_max_age=600
           )
       }
   ```

### Step 3: Push to GitHub

1. Initialize Git repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Django Contact Book"
   ```

2. Create a new repository on GitHub

3. Push your code:
   ```bash
   git remote add origin <your-github-repo-url>
   git branch -M main
   git push -u origin main
   ```

### Step 4: Deploy on Vercel

1. Go to [Vercel](https://vercel.com/)
2. Click "Add New Project"
3. Import your GitHub repository
4. Configure your project:
   - **Framework Preset**: Other
   - **Root Directory**: `./`
   - **Build Command**: Leave empty or use `pip install -r requirements.txt`
   - **Output Directory**: Leave empty

5. **Add Environment Variables**:
   Click on "Environment Variables" and add:
   ```
   SECRET_KEY=<generate-a-new-secret-key>
   DEBUG=False
   ALLOWED_HOSTS=.vercel.app
   DATABASE_URL=<your-postgres-connection-string>
   ```

   To generate a new SECRET_KEY, run:
   ```python
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

6. Click "Deploy"

### Step 5: Run Migrations on Production

After deployment, you need to run migrations on your production database:

1. Install Vercel CLI:
   ```bash
   npm i -g vercel
   ```

2. Login to Vercel:
   ```bash
   vercel login
   ```

3. Link your project:
   ```bash
   vercel link
   ```

4. Run migrations:
   ```bash
   vercel env pull .env.production
   python manage.py migrate --settings=contactbook_project.settings
   ```

   Or use Vercel's dev environment:
   ```bash
   vercel dev
   # Then in another terminal:
   python manage.py migrate
   ```

### Step 6: Create Superuser (Optional)

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

Visit `https://your-app.vercel.app/admin` to login.

## Environment Variables

Create a `.env` file in the root directory (copy from `.env.example`):

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,.vercel.app
DATABASE_URL=postgresql://user:password@host:port/dbname
```

## Project Structure

```
CONTACT BOOK/
├── contactbook_project/     # Django project settings
│   ├── settings.py         # Main settings
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI application
├── contacts/              # Contacts app
│   ├── models.py         # Contact model
│   ├── views.py          # View functions
│   ├── urls.py           # App URLs
│   ├── admin.py          # Admin configuration
│   └── templates/        # HTML templates
│       └── contacts/
│           ├── base.html
│           ├── contact_list.html
│           ├── contact_form.html
│           └── contact_confirm_delete.html
├── static/               # Static files (CSS, JS)
│   └── css/
│       └── style.css
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
├── vercel.json         # Vercel configuration
├── build_files.sh      # Build script for Vercel
└── .gitignore          # Git ignore file
```

## Troubleshooting

### Static files not loading on Vercel
Make sure WhiteNoise is installed and configured in `settings.py`.

### Database connection errors
Verify your `DATABASE_URL` environment variable is correct.

### CSRF token errors
Add your Vercel domain to `ALLOWED_HOSTS` in settings.

### Migrations not applied
Run migrations after deployment using Vercel CLI.

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues, please create an issue in the GitHub repository.

---

**Made with ❤️ using Django**
