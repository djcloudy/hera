# Hera

Hera is a lightweight web dashboard for keeping your lab's Linux servers up to
update. It connects to each server over SSH, checks for pending `apt` package
updates and lets you trigger upgrades directly from the dashboard.

## Features

- View pending package updates for each server.
- Trigger package upgrades remotely.
- Simple web interface built with Flask.

## Getting started

1. Ensure passwordless SSH access to each server you want to manage.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Update the `SERVERS` list in `hera_app/web.py` with your hostnames.
4. Launch the application:

   ```bash
   python -m hera_app.web
   ```

The dashboard will display each server and the number of packages awaiting
upgrade. Selecting **Apply Updates** runs `apt-get upgrade -y` on the target
server.

This project is an early prototype and does not yet include vulnerability
scanning or support for non-`apt` package managers.
