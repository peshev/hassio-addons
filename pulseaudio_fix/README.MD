# Home Assistant Fix Add-on: Alsa & PulseAudio Fix
This add-on eliminates the [problem](https://github.com/home-assistant/audio/issues/12) of ``Device or resource busy`` on computers with an **external ALSA and PULSEAUDIO** caused by the docker container ```hassio_audio```
\
## Warning!
This is a *very dirty temporary hack*, but it **works**.
## How to use:
1. Install addon.
2. Run it.
3. If the problem is present, then it will fix itself.
4. PROFIT!! \
\
**After each reboot of the container with hassio, this fix will start automatically.**
## Install:
1. Add this url to your Hass.io addons repos: \
`https://github.com/OPHoperHPO/hassio-addons`
2. Update addons list.
3. Install this addon.
## Urls:
[Addon link](https://github.com/OPHoperHPO/hassio-addons/tree/master/pulseaudio_fix)
## Credits:
Developed by [Anodev](https://github.com/OPHoperHPO)
