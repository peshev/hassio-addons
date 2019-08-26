# Hass.IO MP3 file player from url.
# Writen by Anodev (2019).

# Config
cache_dir = "./cache"


def install_dependencies():
    """Installs dependencies"""
    import importlib
    import subprocess
    modules = ["os", "json", "requests", "random", "playsound"]
    for module in modules:
        try:
            importlib.import_module(module)
        except ImportError:
            subprocess.call(['pip3', 'install', module])


# Check install for all dependencies
install_dependencies()

# Imports
import os
import json
import requests
from random import randint
from playsound import playsound


def setup():
    """Setup"""
    if not os.path.exists(os.path.join(cache_dir)):
        os.makedirs(cache_dir)


def parse_config(path="/data/options.json"):
    """Reads options from json file."""
    with open(path, "r") as f:
        config = json.load(f)
    return config


def download(file_url: str):
    """Download file and save."""
    # Gen name
    name = str(randint(0, 100000)) + '.mp3'
    # Check for file in ./cache folder
    while name in os.listdir(cache_dir):
        name = str(randint(0, 100000)) + '.mp3'
    # Start download file
    try:
        file = requests.get(file_url)
        if file.status_code == 200:
            with open(os.path.join(cache_dir, name), 'wb') as f:
                f.write(file.content)
            return name
        else:
            print("Media Player HTTP status code error!", file.status_code)
    except Exception as e:
        print("Media Player [Unknown error]: ", e)


def play(filename: str):
    """Play music from file"""
    try:
        playsound(os.path.join(cache_dir, filename))
    except Exception as e:
        print("Unknown Error! Details: ", e)


def clean(name: str):
    """Cleans cache folder and removes cache folder"""
    # Remove temp file
    if os.path.exists(os.path.join(cache_dir, name)):
        os.remove(os.path.join(cache_dir, name))
    # Remove cache folder
    if os.path.exists(os.path.join(cache_dir)):
        os.rmdir(os.path.join(cache_dir))


if __name__ == "__main__":
    # Start setup
    setup()
    # Parse config
    cfg = parse_config()
    url = cfg['url']
    # Download file
    nm = download(url)
    # Play file
    play(nm)
    # Clean
    clean(nm)
