Name:           authenticator
Version:        4.5.0
Release:        1%{?dist}
Summary:        Generate Two-Factor Codes
License:        GPL-3.0
URL:            https://gitlab.gnome.org/World/Authenticator
Source0:        https://gitlab.gnome.org/World/Authenticator/-/archive/%{version}/Authenticator-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  meson
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gstreamer1-plugins-bad-free-devel
BuildRequires:  gstreamer1-plugins-base gstreamer1-plugins-base-devel
BuildRequires:  gstreamer1-plugins-good gstreamer1-plugins-good-extras
BuildRequires:  desktop-file-utils
BuildRequires:  openssl-devel
BuildRequires:  libappstream-glib-devel
BuildRequires:  sqlite-devel
BuildRequires:  zbar-devel
BuildRequires:  cmake

Requires:       gtk4
Requires:       libadwaita
Requires:       glib2
Requires:       gstreamer1
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good

%description

%prep
%autosetup

%build
%meson
%meson_build -j 1

%install
%meson_install

%files
# %license add-license-file-here
# %doc add-docs-here
%{_bindir}/authenticator
%{_datadir}/applications/com.belmoussaoui.Authenticator.desktop
%{_datadir}/authenticator/authenticator.gresource
%{_datadir}/dbus-1/services/com.belmoussaoui.Authenticator.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/com.belmoussaoui.Authenticator.search-provider.ini
%{_datadir}/glib-2.0/schemas/com.belmoussaoui.Authenticator.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/com.belmoussaoui.Authenticator.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.belmoussaoui.Authenticator-symbolic.svg
%{_datadir}/locale/*/LC_MESSAGES/authenticator.mo
%{_datadir}/metainfo/com.belmoussaoui.Authenticator.metainfo.xml

%changelog
* Sun Jun 30 2024 dfkajar <dfkajar@gmail.com>
-
