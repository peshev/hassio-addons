# Hass.IO pulseaudio fix
# Writen by Anodev (2020).
import subprocess


def main():
    # pactl load-module module-suspend-on-idle
    print("-----------Start command")
    process = subprocess.call(['pactl', 'load-module', "module-suspend-on-idle"])
    print("-----------Work Finished; Exit Code: ", process)


if __name__ == "__main__":
    main()
