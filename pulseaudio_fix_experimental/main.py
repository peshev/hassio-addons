import subprocess

def get_config():
    process = subprocess.Popen(['bashio::config'], stdout=subprocess.PIPE)
    stdout = process.communicate()[0]
    return dict(stdout)

def main():
    config = get_config()
    print(config)
    subprocess.call(["pactl", "load-module", "module-suspend-on-idle"])


if __name__ == '__main__':
    main()
