import subprocess


def is_loaded():
    """This function determines if the module `module-suspend-on-idle` is loaded """
    proc = subprocess.Popen(["pactl", "list", "short"], stdout=subprocess.PIPE)
    stdout = proc.communicate()[0].decode("UTF-8")
    if "module-suspend-on-idle" in stdout:
        return True
    else:
        return False


def load_module():
    """This function loads the module and returns any errors that occur in the process."""
    proc = subprocess.Popen(["pactl", "load-module", "module-suspend-on-idle"], stderr=subprocess.PIPE)
    stderr = proc.communicate()[1].decode("UTF-8")
    return stderr


def unload_module():
    """This function unloads the module and returns any errors that occur in the process."""
    proc = subprocess.Popen(["pactl", "unload-module", "module-suspend-on-idle"], stderr=subprocess.PIPE)
    stderr = proc.communicate()[1].decode("UTF-8")
    return stderr


def main():
    """Main function"""
    if is_loaded():
        err = unload_module()
        if len(err) > 0:
            raise Exception("[ALSA&PULSEAUDIO FIX][ERROR] Error unloading module `module-suspend-on-idle`!"
                            "Output pactl: {}".format(err))
    err = load_module()
    if len(err) > 0:
        Exception("[ALSA&PULSEAUDIO FIX][ERROR] Error loading module `module-suspend-on-idle`!"
                  "Output pactl: {}".format(err))
    else:
        print("[ALSA&PULSEAUDIO FIX][INFO] Module `module-suspend-on-idle` loaded successfully!")


if __name__ == '__main__':
    main()
