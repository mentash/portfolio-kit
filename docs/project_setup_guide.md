# Portfolio Kit - Project Setup Guide

Follow these steps to initialize your project. Execute the commands in your terminal (PowerShell).

## 1. Activate Environment & Install Dependencies

First, ensure you are using the virtual environment you created.

```powershell
# Activate the virtual environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip to the latest version
python -m pip install --upgrade pip

# Install Wagtail (and standard Django dependencies)
pip install wagtail
```

## 2. Initialize the Project

We will use the `wagtail start` command to generate the project skeleton.
_Note: We use the period `.` at the end to generate it in the current directory._

```powershell
# Generate the project structure
wagtail start config .
```

> **Why `config`?** We name the project folder `config` to keep the settings clearly separated from your actual apps. This is a common best practice in modern Django.

## 3. Post-Generation Setup

After generation, Wagtail creates a `requirements.txt`. Let's ensure everything is installed.

```powershell
# Install all generated requirements
pip install -r requirements.txt
```

## 4. Database & User Setup

Now we prepare the database and create your admin account.

```powershell
# Run initial migrations
python manage.py migrate

# Create your superuser account (admin)
python manage.py createsuperuser
```

## 5. Verify Installation

Run the development server to check if everything works.

```powershell
python manage.py runserver
```

Open your browser to:

- **Homepage:** `http://127.0.0.1:8000` (Should see the Wagtail welcome page)
- **Admin:** `http://127.0.0.1:8000/admin` (Login with your superuser)

---

**Next Steps:**
Once you have verified the installation, we will proceed to **Episode 1: Core Platform Foundation** from our Agile Plan.
