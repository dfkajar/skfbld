%global debug_package %{nil}
Name:           amberol
Version:        2025.1
Release:        1
Summary:        Simple and modern GNOME music player
License:        GPL-3.0
URL:            https://gitlab.gnome.org/World/amberol
Source0:        %{url}/-/archive/%{version}/amberol-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(gtk4) >= 4.16.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.20
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 1.20
BuildRequires:  pkgconfig(gstreamer-play-1.0) >= 1.20
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.20
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0) >= 1.20
BuildRequires:  pkgconfig(gstreamer-bad-audio-1.0) >= 1.20
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)

Requires:       libadwaita
Requires:       gtk4
Requires:       hicolor-icon-theme
Requires:	desktop-file-utils
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
%{_datadir}/metainfo/io.bassi.Amberol.metainfo.xml
%{_datadir}/glib-2.0/schemas/io.bassi.Amberol.gschema.xml
%{_datadir}/applications/io.bassi.Amberol.desktop
%{_datadir}/dbus-1/services/io.bassi.Amberol.service
%{_datadir}/icons/hicolor/scalable/apps/io.bassi.Amberol.svg
%{_datadir}/icons/hicolor/symbolic/apps/io.bassi.Amberol-symbolic.svg
%{_datadir}/locale/*/LC_MESSAGES/amberol.mo

%changelog
* Mon Jan 07 2025 sunrise2011
- First build
