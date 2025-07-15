 Django project with JWT authentication, role-based access control, and CRUD functionality for user profiles (UUID, name, email, age):

---

```markdown
# 🛡️ Django JWT Authentication with Role-Based Access & User Profile CRUD

This project is a secure Django RESTful API that implements:

- 🔐 JWT-based authentication
- 👥 Role-based access control (`admin`, `user`, `owner`)
- 🧾 Custom user model with role support
- 🧍 Each user can create/update/view/delete their **own** profile (UUID, name, email, age)
- 🛠 Admin can manage (CRUD) all users' profiles
- ✅ Admin can control access to profile viewing
- ⚙️ SQLite3 database with ORM (no in-memory)

---

## 📁 Project Structure

```

├── Task03/                 # Main project
│   └── settings.py         # Project settings
│   └── urls.py             # Global URLs
├── user\_auth/              # App for user management
│   └── models.py           # CustomUser & Profile models
│   └── views.py            # Registration, Login, Profile CRUD
│   └── urls.py             # App-level routes
│   └── serializers.py      # DRF serializers
├── db.sqlite3              # SQLite3 database
├── manage.py
└── .env                    # Optional for DB credentials

````

---

## 🛠 Requirements

- Python 3.10+
- Django 5.x
- djangorestframework
- djangorestframework-simplejwt
- bcrypt
- python-dotenv

---

## ⚙️ Installation & Setup

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd <project-folder>

# 2. Create a virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run initial migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create a superuser (for admin access)
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
````

---

## 🔐 API Endpoints

| Method | Endpoint         | Access         | Description                 |
| ------ | ---------------- | -------------- | --------------------------- |
| POST   | `/api/register/` | Public         | Register as regular `user`  |
| POST   | `/api/login/`    | Public         | Login and receive JWT token |
| GET    | `/api/profile/`  | Authenticated  | View your own profile       |
| POST   | `/api/profile/`  | Authenticated  | Create your own profile     |
| PUT    | `/api/profile/`  | Authenticated  | Update your own profile     |
| DELETE | `/api/profile/`  | Authenticated  | Delete your own profile     |
| GET    | `/api/users/`    | Admin + Shared | View all users (admin only) |
| GET    | `/admin/`        | Superuser Only | Django admin interface      |

> Note: Only **admin** can assign visibility of user data to others.

---

## 👥 Roles

* **Admin**: Full control via Django admin panel. Can manage any user profile.
* **User**: Can register/login and manage their own profile (CRUD).
* **Owner**: Reserved for future use (business-specific logic).

---

## 🔒 Authentication Flow

1. `POST /api/register/` – Creates a user (role is always `user`)
2. `POST /api/login/` – Returns JWT tokens
3. Authenticated routes require `Authorization: Bearer <access_token>` header

---

## 🗂 Environment Variables (Optional for production)

Create a `.env` file:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_NAME=db.sqlite3
```

---

## 📦 Future Improvements

* Admin-based assignment of visibility
* Token blacklist/logout support
* Profile picture upload
* Email confirmation

---

## 📸 Screenshots

*Not included — add Swagger UI or Postman collection if needed.*

---

## 🧑‍💻 Author

Built with ❤️ using Django by \[Your Name]

---

## 📄 License

This project is open-source and free to use.

```

---

```
