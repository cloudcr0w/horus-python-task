# Horus DevOps Recruitment Task – Python

This project was created as part of a technical task for a DevOps position.

The script fetches user data from the [randomuser.me](https://randomuser.me/) API and creates Linux users based on the retrieved information.


## ✅ What the script does

- Sends 100 requests to the API in batches of 5, with a 2-second delay between batches.
- Each batch is executed concurrently (5 requests in parallel).
- For each user:
  - the Linux username is created based on the API `login.username`
  - full name is assigned as a comment to the account
  - **All created users have a `test_` prefix for easy cleanup after execution.**


## 🐍 How to run

```bash
python3 main.py
```

⚠️ Requires `sudo` privileges to create users with `useradd`.


## 📁 Files

```bash
|-- main.py
|-- README.md
```

## 👤 Author

Adam Wrona – [LinkedIn Profile](https://www.linkedin.com/in/adam-wrona-111ba728b/)
adamwronowy@gmail.com