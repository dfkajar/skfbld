Name:           video-trimmer
Version:        0.8.2
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
BuildRequires:  desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	blueprint-compiler
BuildRequires:	python3-gobject-devel
BuildRequires:	zbar-devel

Requires:       gtk4
Requires:       libadwaita

%description

%prep
cd %{_builddir}/
git clone --recurse-submodules https://gitlab.gnome.org/YaLTeR/video-trimmer.git
cd video-trimmer
git checkout 68c7a71f6e0e6e2b3a69aee3985089db597a385c

%build
cd video-trimmer
%meson --buildtype release
%meson_build -j 1

%install
cd video-trimmer*
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


