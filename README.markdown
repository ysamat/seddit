# Seddit

## Overview
Seddit is a Reddit-inspired web application built with Django, designed as a homework assignment (HW4). It allows users to sign up, log in, create posts, comment, upvote, and explore subseddits (tag-based forums). The project features a responsive design styled with Tailwind CSS and includes basic CRUD operations for a social media-like experience.

## Features
- **User Authentication**: Sign up, log in, and log out functionality.
- **Homepage**: Displays the 10 most recent posts with titles, authors, dates, and tags.
- **Post Creation**: Authenticated users can create posts with titles, content, and tags.
- **Post Details**: View posts with comments, upvotes, and tags; includes options to comment, upvote, or delete (for post owners).
- **Subseddits**: Tag-based forums showing posts with specific tags.
- **Responsive Design**: Styled with Tailwind CSS for a modern, user-friendly interface.

## Tech Stack
- **Backend**: Django 5.2 (compatible with Python 3.13)
- **Frontend**: HTML templates with Tailwind CSS (via CDN)
- **Database**: SQLite (default Django database)
- **Python**: 3.13.2 (can be adjusted to 3.6–3.10 for Django 3.2)

## Setup Instructions

### Prerequisites
- Python 3.6+ (3.13.2 recommended for Django 5.2)
- pip (Python package manager)
- Virtual environment (recommended)

### Installation
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd seddit
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
   ```

3. **Install Dependencies**:
   ```bash
   pip install django==5.2
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a Superuser (Optional)**:
   To access the admin interface:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   - Access the app at `http://127.0.0.1:8000/`.

## Usage
- **Homepage**: Visit `http://127.0.0.1:8000/` to see recent posts.
- **Sign Up/Log In**: Use `/signup/` and `/login/` to create and access your account.
- **Create Posts**: Go to `/create_post/` (requires login) to add new posts with tags.
- **Interact with Posts**: View posts at `/post/<post_id>/`, where you can comment, upvote, or delete (if owner).
- **Subseddits**: Explore tag-based forums at `/s/<tag>/` (e.g., `/s/python/`).
- **Admin Interface**: Access `/admin/` to manage users and posts (requires superuser login).

## Project Structure
```
seddit/
├── forum/              # Django app for core functionality
│   ├── migrations/     # Database migration files
│   ├── models.py       # Models (Post, Tag, Upvote, Comment)
│   ├── urls.py         # URL routing for the forum app
│   ├── views.py        # Views for handling requests
│   └── ...             # Other app files
├── seddit/             # Project settings and configuration
│   ├── settings.py     # Django settings
│   ├── urls.py         # Root URL routing
│   ├── wsgi.py         # WSGI configuration
│   └── ...             # Other project files
├── templates/          # HTML templates with Tailwind CSS
│   ├── base.html
│   ├── index.html
│   └── ...             # Other templates
├── venv/               # Virtual environment
└── manage.py           # Django management script
```

## Troubleshooting
- **OperationalError: no such table**:
  - Run `python manage.py makemigrations` and `python manage.py migrate`.
- **Port Already in Use**:
  - Kill the process using port 8000:
    ```powershell
    Get-NetTCPConnection -LocalPort 8000
    Stop-Process -Id <PID> -Force
    ```
  - Or run on a different port: `python manage.py runserver 8001`.
- **Django Not Found**:
  - Ensure the virtual environment is activated and Django is installed:
    ```bash
    pip install django==5.2
    ```

## Contributing
This project was created as a homework assignment. Contributions are welcome for educational purposes! Feel free to fork, submit issues, or create pull requests.

## License
This project is unlicensed and intended for educational use.