import os
import subprocess


def main():
    print(os.environ)
    subprocess.call(["load-module", "module-suspend-on-idle"], executable="/usr/bin/pactl")


if __name__ == '__main__':
    main()
