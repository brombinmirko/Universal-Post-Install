'''
   Copyright 2017 Mirko Brombin (brombinmirko@gmail.com)
 
   This file is part of Universal Post Install.
 
   Universal Post Install is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
          the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
 
   Universal Post Install is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
 
   You should have received a copy of the GNU General Public License
   along with Universal Post Install.  If not, see <http://www.gnu.org/licenses/>.
'''
import helper
 
# Define the package manager
E = "apt"
 
helper.title("Deepin")
helper.author("Mirko Brombin")
helper.website("https://linuxhub.it")
 
# Check for release
distro = helper.get_distro()
if distro.release == "15.4.1":
    class PostInstall:
        global E
        # Define menu voices
        voices_en_US = [
            ("Abilita PPA (add-apt-repository)", "enable_ppa"),
            ("Install Deepin Deb Installer ", "install_ddi"),
            ("Install Deepin System Monitor ", "install_deepinsysmonitor"), 
            ("Install Deepin Presentation Assistant ", "install_dpassistant"),  
            ("Install Microsoft core Fonts", "install_mscorefonts"),
            ("Install Flash plugin", "install_flashplugin"),
            ("Install LibreOffice ", "install_libreoffice"),
            ("Install Natron ", "install_natron"),
            ("Install Lightworks ", "install_lightworks"),
            ("Install Firefox ", "install_firefox"),
            ("Install more applications ", "launch_store"),
        ]
        voices_it_IT = [
            ("Imposta il mirror Italiano GARR", "install_garr_it"),
            ("Abilita PPA (add-apt-repository)", "enable_ppa"),
            ("Installa Deepin Deb Installer ", "install_ddi"), 
            ("Installa Deepin System Monitor ", "install_deepinsysmonitor"), 
            ("Installa Deepin Presentation Assistant ", "install_dpassistant"),  
            ("Installa Microsoft core Fonts", "install_mscorefonts"),
            ("Installa plugin Flash", "install_flashplugin"),
            ("Installa LibreOffice ", "install_libreoffice_it"),
            ("Installa Natron ", "install_natron"),
            ("Installa Lightworks ", "install_lightworks"),
            ("Installa Firefox ", "install_firefox_it"),
            ("Installa altre applicazioni ", "launch_store"), 
        ]
       
        # Define functions for each menu voice
        def install_garr_it(self):
            helper.do("cd")
            helper.do("bash -c 'cat << EOF > /etc/apt/sources.list\n# Generated by deepin-installer\n# deb [by-hash=force] http://packages.deepin.com/deepin unstable main contrib non-free\n# deb-src http://packages.deepin.com/deepin unstable main contrib non-free\n##########################################################################################\ndeb [by-hash=force] http://ba.mirror.garr.it/mirrors/deepin/ panda main contrib non-free\nEOF'", True)
            helper.pkg_update(E)
        
        def enable_ppa(self):
            helper.pkg_install("python-software-properties software-properties-common", E)
            helper.pkg_update(E)
        
        def install_ddi(self):
            helper.pkg_install("deepin-deb-installer", E)
            helper.pkg_update(E)
        
        def install_deepinsysmonitor(self):
            helper.pkg_install("deepin-system-monitor", E)
            helper.pkg_update(E)
        
        def install_dpassistant(self):
            helper.pkg_install("deepin-presentation-assistant", E)
            helper.pkg_update(E)
        
        def install_mscorefonts(self):
            helper.pkg_install("ttf-mscorefonts-installer", E)
            helper.pkg_update(E)
        
        def install_flashplugin(self):
            helper.pkg_install("flashplugin-nonfree", E)
            helper.pkg_update(E)

        def install_libreoffice(self):
            helper.pkg_install("libreoffice-base libreoffice-style-sifr libreoffice-gtk", E)
            helper.pkg_update(E)

        def install_libreoffice_it(self):
            helper.pkg_install("libreoffice-base libreoffice-style-sifr libreoffice-gtk libreoffice-l10n-it", E)
            helper.pkg_update(E)

        def install_natron(self):
            helper.pkg_install("natron", E)
            helper.pkg_update(E)

        def install_lightworks(self):
            helper.pkg_install("lightworks", E)
            helper.pkg_update(E)

        def install_firefox(self):
            helper.pkg_install("firefox", E)
            helper.pkg_update(E)

        def install_firefox_it(self):
            helper.pkg_install("firefox firefox-locale-it", E)
            helper.pkg_update(E)

        def launch_store(self):
            helper.pkg_install("screen", E)
            helper.do("screen -d -m deepin-appstore")
else:
    helper.not_compatible()
 
# Load script
pi = PostInstall()
try:
    voices = eval('pi.voices_' + distro.lang)
except AttributeError:
    voices = pi.voices_en_US
helper.steps(voices, pi)
