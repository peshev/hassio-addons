# Hass.IO pulseaudio fix
# Writen by Anodev (2020).
import subprocess


def main():
    # pactl load-module module-suspend-on-idle
    subprocess.call(['pactl', 'load-module', "module-suspend-on-idle"])


if __name__ == "__main__":
    main()
