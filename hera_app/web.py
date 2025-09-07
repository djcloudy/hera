from __future__ import annotations

from flask import Flask, redirect, render_template, url_for

from .manager import apply_updates, check_updates

app = Flask(__name__)

# List of hosts to manage. Replace with your actual server hostnames.
SERVERS = ["localhost"]


@app.route("/")
def dashboard():
    statuses = [check_updates(host) for host in SERVERS]
    return render_template("dashboard.html", statuses=statuses)


@app.route("/apply/<host>")
def apply(host: str):
    if host in SERVERS:
        apply_updates(host)
    return redirect(url_for("dashboard"))


if __name__ == "__main__":  # pragma: no cover
    app.run(debug=True)
