### 📄 Blog Maker Lite

---

### Description: This application is a local blog making web app based upon this [tutorial series][tutorial]

---

## 💻 How to Run

1. Clone this repo locally
2. Run with IDE of choice ([PyCharm][pycharm], IntelliJ, etc.) or leverage [Makefile](makefile)
3. [Initialize database models](#-database-configuration)

---

## 💾 Database Configuration

This application leverages [sqllite3][sql-lite-3] to spin up a database locally

- Generate migrations:
```shell
make migration
```

- Run migrations:
```shell
make run-migrations
```

- Create an admin user:
```shell
make super-user
```

- Accessing the database via [admin portal](http://localhost:8000/admin/)

---

## 🛠 Tools used in this project 

- ### 🐍 [Django][django]
- ### 📘 [Markdown][markdown]
- ### ☁ [sql-lite-3][sql-lite-3]
- ### 📝 [Makefile][makefile]


[tutorial]: https://www.mostlypython.com/django-from-first-principles-2/
[pycharm]: https://www.jetbrains.com/guide/python/tutorials/getting-started-pycharm/installation-and-setup/
[django]: https://www.djangoproject.com/
[markdown]: https://www.markdownguide.org/getting-started/
[sql-lite-3]: https://docs.python.org/3/library/sqlite3.html
[makefile]: https://www.gnu.org/software/make/manual/make.html