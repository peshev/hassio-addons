# Alsa & PulseAudio Fix
## Description:
This add-on eliminates the [problem](https://github.com/home-assistant/audio/issues/12) of ``Device or resource busy`` on computers with an **external ALSA and PULSEAUDIO** caused by the docker container ```hassio_audio```.
## Warning!
This is a **very dirty temporary hack**, but it **works**.
## How to use:
1. Install add-on.
2. Run it.
3. Check the add-on’s logs to make sure that
the problem was fixed by successfully loading the module.
> If you ever lose sound again, just launch the add-on manually, or configure the add-on to automatically restart using `automation` in the Home Assistant.
> When you restart the add-on, it reinitializes the module.
> After each reboot of the container with hass.io, this add-on will start automatically.
## Install:
1. Add this url to your hass.io addons repos: \
`https://github.com/OPHoperHPO/hassio-addons`
2. Update addons list.
3. Install this add-on.
## Urls:
[Add-on link](https://github.com/OPHoperHPO/hassio-addons/tree/master/pulseaudio_fix)
## Credits:
Developed by [Anodev](https://github.com/OPHoperHPO)
