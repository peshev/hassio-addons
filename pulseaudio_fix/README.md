# 🥧 Alsa & PulseAudio Fix 🥧

## 📄 Description
This add-on eliminates the [problem](https://github.com/home-assistant/audio/issues/12) of ``Device or resource busy`` on computers with an **external ALSA and PULSEAUDIO** caused by the docker container ```hassio_audio```.

## 💵 Support me:  
  You can thank me for developing any of my projects, provide financial support for developing new projects and buy me a small cup of coffee.☕ \
  Just support me on these platforms:
  * ![](https://github.com/OPHoperHPO/OPHoperHPO/raw/master/assets/imgs/boosty_logo.jpeg) [**Boosty**](https://boosty.to/anodev)
  * ![](https://github.com/OPHoperHPO/OPHoperHPO/raw/master/assets/imgs/donationalerts_logo.png) [**DonationAlerts**](https://www.donationalerts.com/r/anodev_development)
  * ![](https://github.com/OPHoperHPO/OPHoperHPO/raw/master/assets/imgs/paypal_logo.jpg) [**PayPal**](https://paypal.me/anodevru)

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
3. Check add-on logs for the presence of this line: `[ALSA&PULSEAUDIO FIX][INFO] Module `module-suspend-on-idle` loaded successfully!`
> If you ever lose sound again, just launch the add-on manually, or configure the add-on to automatically restart using `automation` in the Home Assistant. \
> When you restart the add-on, it reinitializes the module. \
> After each reboot of the container with hass.io, this add-on will start automatically.

## 🧷 Urls
[Add-on link](https://github.com/OPHoperHPO/hassio-addons/tree/master/pulseaudio_fix)

## 👪 Credits
Developed by [Anodev](https://github.com/OPHoperHPO)

## 🎓 License
   [Apache License 2.0](https://github.com/OPHoperHPO/hassio-addons/blob/master/pulseaudio_fix/LICENSE.md)
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
