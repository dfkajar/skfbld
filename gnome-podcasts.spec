%global debug_package %{nil}
Name:           podcasts
Version:        0.7.2
Release:        1%{?dist}
Summary:        Listen to your favorite podcasts, right from your desktop.
License:        GPL-3.0
URL:            https://apps.gnome.org/Podcasts
Source0:        %{url}/podcasts/-/archive/%{version}/podcasts-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(gtk4) >= 4.16.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.20
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 1.20
BuildRequires:  pkgconfig(gstreamer-play-1.0) >= 1.20
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.20
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0) >= 1.20
BuildRequires:  pkgconfig(gstreamer-bad-audio-1.0) >= 1.20
BuildRequires:  rust-openssl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libappstream)
BuildRequires:  sqlite

Requires:       gtk4
Requires:       libadwaita
Requires:       gstreamer1
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gstreamer1-plugins-bad-free
Requires:       openssl

%description

%prep
%autosetup

%build
%meson --buildtype release
%meson_build -j 1

%install
%meson_install

%files
%{_bindir}/gnome-podcasts
%{_datadir}/applications/org.gnome.Podcasts.desktop
%{_datadir}/dbus-1/services/org.gnome.Podcasts.service
%{_datadir}/glib-2.0/schemas/org.gnome.Podcasts.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Podcasts*.svg
%{_datadir}/metainfo/org.gnome.Podcasts.appdata.xml
%{_datadir}/locale/*/LC_MESSAGES/gnome-podcasts.mo

%changelog
* Mon Jun 24 2024 sunrise2011
-
