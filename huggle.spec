%global forgeurl https://github.com/huggle/huggle3-qt-lx
%global tag 3.4.10
%forgemeta

Name: Huggle
Summary: A program to revert vandalism on wikis
Version: 3.4.10
Release: 0.1%{dist} 

License: GPLv3+ and BSD
URL: https://en.wikipedia.org/wiki/Wikipedia:Huggle

BuildRequires: yaml-cpp-devel
BuildRequires: gcc-c++
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qtwebkit-devel

Source: %{forgesource}
Patch0: use-system-yaml-cpp.patch
Patch1: cmake-patch.patch

%description
Huggle is a diff browser intended for dealing with
vandalism on MediaWiki-based wikis such as Wikipedia.

%prep
%forgesetup
rm src/3rd/yaml-cpp.zip
rm -rf src/3rd/yaml-cpp
pwd
%patch0
pwd
%patch1 -p1

%build
%configure
cd release
%make_build

%install
cd release
%make_install

%files
/usr/local/bin/huggle
/usr/local/lib/libhuggle_core.so
/usr/local/lib/libhuggle_l10n.so
/usr/local/lib/libhuggle_res.so
/usr/local/lib/libhuggle_ui.so
/usr/local/lib/libirc.so
/usr/local/lib/libircclient.so
/usr/local/share/applications/huggle.desktop
/usr/local/share/huggle/extensions/devtools.js
/usr/local/share/huggle/huggle3_newlogo.png
/usr/local/share/man/man1/huggle.1

