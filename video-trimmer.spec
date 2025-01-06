Name:           video-trimmer
Version:        0.9.0
Release:        1%{?dist}
Summary:        Trim videos quickly
License:        GPL-3.0
URL:            https://gitlab.gnome.org/YaLTeR/video-trimmer
Source0:        https://gitlab.gnome.org/YaLTeR/video-trimmer/-/archive/v%{version}/video-trimmer-v%{version}.tar.gz

BuildRequires:  git
BuildRequires:  meson
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  glib2-devel
BuildRequires:  gtk4-devel
Buildrequires:  libadwaita-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-bad-free-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gstreamer1-plugins-good-extras
BuildRequires:  gstreamer1-vaapi
BuildRequires:  gstreamer1-plugins-good 
BuildRequires:  gstreamer1-plugins-base
BuildRequires:  gstreamer1-vaapi 
BuildRequires:  desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	blueprint-compiler
BuildRequires:	python3-gobject-devel
BuildRequires:	zbar-devel

Requires:       gtk4
Requires:       libadwaita

%description

%prep
%setup -n video-trimmer-v%{version}

%build
%meson
%meson_build 

%install
%meson_install

%files
%{_bindir}/video-trimmer
%{_datadir}/applications/org.gnome.gitlab.YaLTeR.VideoTrimmer.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gitlab.YaLTeR.VideoTrimmer.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.gitlab.YaLTeR.VideoTrimmer.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.gitlab.YaLTeR.VideoTrimmer-symbolic.svg
%{_datadir}/locale/*/LC_MESSAGES/video-trimmer.mo
%{_datadir}/metainfo/org.gnome.gitlab.YaLTeR.VideoTrimmer.metainfo.xml
%{_datadir}/video-trimmer/video-trimmer.gresource

%changelog
* Mon Jun 24 2024 sunrise2011
-


