# 📒 Contact Book - Django Web Application

A modern, full-featured contact management system built with Django and ready to deploy on Render.

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
- **Deployment**: Render
- **WSGI Server**: Gunicorn

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

## Deploying to Render

For detailed deployment instructions, see [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md)

### Quick Deploy Steps:

1. **Push your code to GitHub**:
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

2. **Create a Render account** at [https://render.com/](https://render.com/)

3. **Create a PostgreSQL database** (Free tier available)

4. **Deploy as Web Service**:
   - Connect your GitHub repository
   - Render will auto-detect `render.yaml`
   - Set environment variables (DATABASE_URL, SECRET_KEY, etc.)
   - Click "Deploy"

5. **Your app will be live** at `https://your-app.onrender.com`

For complete step-by-step instructions, see [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md)

## Environment Variables

Create a `.env` file in the root directory for local development:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,.onrender.com
DATABASE_URL=postgresql://user:password@host:port/dbname
```

For production on Render, set these in the Render dashboard.

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
├── render.yaml         # Render configuration
├── build.sh            # Build script for Render
└── .gitignore          # Git ignore file
```

## Troubleshooting

### Static files not loading
Make sure WhiteNoise is installed and configured in `settings.py`.

### Database connection errors
Verify your `DATABASE_URL` environment variable is correct and using the **Internal Database URL** from Render.

### CSRF token errors
Add your Render domain to `ALLOWED_HOSTS` in settings.

### Application sleeping
Free tier services sleep after 15 minutes of inactivity. First request may take 30 seconds.

### Build failures
Check the build logs in Render dashboard and verify all dependencies are in `requirements.txt`.

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues, please create an issue in the GitHub repository.

---

**Made with ❤️ using Django**
