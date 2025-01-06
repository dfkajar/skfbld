Name:           amberol
Version:        2024.2 
Release:        1
Summary:        Simple and modern GNOME music player
License:        GPL-3.0
Source0:        https://gitlab.gnome.org/World/amberol/-/archive/%{version}/amberol-%{version}.tar.gz
URL:            https://gitlab.gnome.org/World/amberol.git

BuildRequires:  meson
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:	cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils
BuildRequires:	reuse
BuildRequires:  dbus-devel
BuildRequires:  pkgconf-pkg-config
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gstreamer1-plugins-bad-free-devel
BuildRequires:  git

Requires:       libadwaita
Requires:       gtk4
Requires:       hicolor-icon-theme
Requires:       gstreamer1
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-bad-free

# ASS subtitles (assrender)
Recommends:     gstreamer1-plugins-bad-free-extras

# CD Playback
Suggests:       gstreamer1-plugins-ugly-free

%description
A GNOME music player

%prep
%setup

%build
%meson --buildtype release
%meson_build -j 1

%install
%meson_install

%files
%{_bindir}/amberol
%{_datadir}/amberol/amberol.gresource
%{_datadir}/appdata/io.bassi.Amberol.appdata.xml
%{_datadir}/applications/io.bassi.Amberol.desktop
%{_datadir}/dbus-1/services/io.bassi.Amberol.service
%{_datadir}/glib-2.0/schemas/io.bassi.Amberol.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/io.bassi.Amberol.svg
%{_datadir}/icons/hicolor/symbolic/apps/io.bassi.Amberol-symbolic.svg
%{_datadir}/locale/*/LC_MESSAGES/amberol.mo

%changelog
