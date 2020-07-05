# 🥧 Alsa & PulseAudio Fix 🥧

## 📄 Description
This add-on eliminates the [problem](https://github.com/home-assistant/audio/issues/12) of ``Device or resource busy`` on computers with an **external ALSA and PULSEAUDIO** caused by the docker container ```hassio_audio```.

## 🔍 Warning!
This is a **very dirty temporary hack**, but it **works**.

## 🏷 Install
1. Add this url to your hass.io addons repos: \
`https://github.com/OPHoperHPO/hassio-addons`
2. Update addons list.
3. Install this add-on.

## 🧰 How to use
1. Install add-on.
2. Run it.
3. Check the add-on’s logs to make sure that
the problem was fixed by successfully loading the module.
> If you ever lose sound again, just launch the add-on manually, or configure the add-on to automatically restart using `automation` in the Home Assistant.
> When you restart the add-on, it reinitializes the module.
> After each reboot of the container with hass.io, this add-on will start automatically.

### 💵 Support me:
You can thank me for developing this project, provide financial support for the development of new projects and buy me a small cup of coffee.☕ \
  Just support me on these platforms:    \
  ⭐[**Boosty**⭐](https://boosty.to/anodev)   \
  ⭐[**DonationAlerts**⭐](https://www.donationalerts.com/r/anodev_development)

## 🧷 Urls
[Add-on link](https://github.com/OPHoperHPO/hassio-addons/tree/master/pulseaudio_fix)

## 👪 Credits
Developed by [Anodev](https://github.com/OPHoperHPO)

## 🎓 License
[Apache License 2.0](https://github.com/OPHoperHPO/hassio-addons/blob/master/pulseaudio_fix/LICENSE)
   Copyright 2020 Anodev (OPHoperHPO)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.