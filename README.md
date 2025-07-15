```markdown
# 🛡️ Django JWT Auth + Role-Based Access + Profile CRUD 🔐

This project is a **secure Django REST API** that provides:

✨ JWT Authentication  
🔐 Role-Based Access Control (`admin`, `user`, `owner`)  
👤 Custom User Model  
📝 Profile CRUD (UUID, Name, Email, Age)  
📦 SQLite3 Persistent Database  
🚫 Admin Hidden from Public Registration  

---

## 📁 Project Structure

```

prodigy task 3/
├── Task03/
│   ├── settings.py       # Django settings
│   ├── urls.py           # Root URL routing
├── user\_auth/
│   ├── models.py         # CustomUser & Profile model
│   ├── serializers.py    # DRF serializers
│   ├── views.py          # Register, Login, CRUD logic
│   ├── urls.py           # App-level API routing
├── db.sqlite3            # SQLite3 DB
├── manage.py
├── .gitignore
├── .venv/

````

---

## 🚀 Features

- ✅ **Register/Login** using Django REST Framework
- 🔐 **JWT Token** authentication (`access`, `refresh`)
- 👥 **CustomUser** model with roles: `admin`, `user`, `owner`
- 🗂️ Each user can:
  - Create & edit their profile (UUID, name, email, age)
  - View only their data
- 👑 **Admin**:
  - Has full access to all users' data
  - Can edit/delete any profile
  - Can assign view access to other users
- 📂 SQLite database (persistent storage)
- 🔏 Passwords are hashed using **bcrypt**

---

## 🛠 Installation

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
````

2. **Set up virtual environment**

```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser (admin)**

```bash
python manage.py createsuperuser
```

6. **Run the server**

```bash
python manage.py runserver
```

---

## 🧪 API Endpoints

| Method | Endpoint         | Access         | Description                    |
| ------ | ---------------- | -------------- | ------------------------------ |
| POST   | `/api/register/` | Public         | Register as regular user       |
| POST   | `/api/login/`    | Public         | Login with username/password   |
| GET    | `/api/profile/`  | Authenticated  | View own profile               |
| POST   | `/api/profile/`  | Authenticated  | Create own profile             |
| PUT    | `/api/profile/`  | Authenticated  | Update own profile             |
| DELETE | `/api/profile/`  | Authenticated  | Delete own profile             |
| GET    | `/api/users/`    | Admin Only     | View all user details          |
| GET    | `/admin/`        | Superuser Only | Admin interface (hidden route) |

> 💡 Only `admin` can assign which users have access to others' data.

---

## 👥 User Roles

| Role  | Permissions                                             |
| ----- | ------------------------------------------------------- |
| user  | Register/login, manage own profile only                 |
| owner | Same as user (reserved for extended control later)      |
| admin | Manage all users, assign access, and control the system |

---

## 🔐 Authentication

1. Register via `/api/register/`
2. Login via `/api/login/` → get `access` and `refresh` tokens
3. Use token in header:

```
Authorization: Bearer <access_token>
```

---

## 📦 Environment Variables (optional)

You can use `.env` and `python-dotenv` to secure sensitive data:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_NAME=db.sqlite3
```

---

## ❌ Security Notes

* Admin creation is **only** allowed through `createsuperuser`
* Registration endpoint allows only `user` role
* Admin dashboard is hidden at `/admin/`

---

## ✅ To Push to GitHub

```bash
git init
git remote add origin https://github.com/yourusername/repo.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

---

## 📂 .gitignore Example

```gitignore
*.pyc
__pycache__/
db.sqlite3
.env
.venv/
.idea/
*.log
```

---

## 🧑‍💻 Built With

* Django
* Django REST Framework
* SimpleJWT
* bcrypt
* SQLite3

---

## 📄 License

Open-source project. Free to use and modify ✨

---

## 🙋‍♂️ Author

Built by **\[Your Name]**
Feel free to contribute or suggest improvements!

```
