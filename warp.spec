Name:           warp
Version:        0.7.0
Release:        1%{?dist}
Summary:        Fast and secure file transfer
License:        GPL-3.0
URL:            https://gitlab.gnome.org/World/warp
Source0:        https://gitlab.gnome.org/World/warp/-/archive/v%{version}/warp-v%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:	cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconf-pkg-config
BuildRequires:  git
BuildRequires:  itstool
BuildRequires:  libappstream-glib-devel
BuildRequires:  zbar-devel

Requires:       libadwaita
Requires:       gtk4
Requires:       hicolor-icon-theme

%description

%prep
cd %{_builddir}/
git clone --recurse-submodules https://gitlab.gnome.org/World/warp.git
cd warp
git checkout 1daa60691aa1a697acaff55450dcccb085023fc7

%build
cd warp
%meson
%meson_build

%install
cd warp*
%meson_install

%files
%{_bindir}/warp
%{_datadir}/applications/app.drey.Warp.desktop
%{_datadir}/help/*/warp/*.page
%{_datadir}/icons/hicolor/scalable/apps/app.drey.Warp.svg
%{_datadir}/icons/hicolor/symbolic/apps/app.drey.Warp-symbolic.svg
%{_datadir}/locale/*/LC_MESSAGES/warp.mo
%{_datadir}/metainfo/app.drey.Warp.metainfo.xml

%changelog
* Mon Jun 24 2024 sunrise2011
-
