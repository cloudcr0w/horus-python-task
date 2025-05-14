import subprocess
import time
from concurrent.futures import ThreadPoolExecutor

import requests


# dodawanie użytkowników
def user_add(username, fullname=None, user_dir=None):
    cmd = ["sudo", "useradd", "-m"]
    if fullname:
        cmd += ["-c", fullname]
    if user_dir:
        cmd += ["-d", user_dir]
    cmd.append(username)
    try:
        subprocess.run(
            cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True
        )
        print(f"✅ Utworzono użytkownika: {username} ({fullname})")
    except subprocess.CalledProcessError:
        print(f"⚠️ Nie udało się utworzyć użytkownika {username} – może już istnieje.")

# przerabianie danych użytkowników – wyciąganie imienia, nazwiska i loginu (username)
def fetch_user(i, offset):
    response = requests.get("https://randomuser.me/api/", timeout=5)
    if response.status_code == 200:
        data = response.json()
        user = data["results"][0]

        username = f"test_{user['login']['username']}"
        return {
            "index": offset + i + 1,
            "first": user["name"]["first"],
            "last": user["name"]["last"],
            "username": username,
        }
    else:
        return {"index": offset + i + 1, "error": True}

# pętla dla 20 paczek po 5 użytkowników
for loop_users in range(20):
    offset = loop_users * 5
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(lambda i: fetch_user(i, offset), range(5)))

# sortowanie i wypisanie wyników po kolei z przerwą 2s pomiędzy
    results.sort(key=lambda x: x["index"])

    for user in results:
        if "error" in user:
            print(f"[{user['index']}] ❌ Błąd API")
        else:
            print(
                f"[{user['index']}] Name: {user['first']} {user['last']} – login: {user['username']}"
            )
        fullname = f"{user['first']} {user['last']}"
        user_add(user["username"], fullname)
    time.sleep(2)
