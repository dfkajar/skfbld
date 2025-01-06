Name:		obfuscate
Version:	0.0.10
Release:	1%{?dist}
Summary:	Obfuscate image and docs
License:        LGPLv3+
URL:		https://gitlab.gnome.org/World/obfuscate.git
Source0:        https://gitlab.gnome.org/World/obfuscate/-/archive/%{version}/obfuscate-%{version}.tar.gz

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  git
BuildRequires:	libadwaita-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  desktop-file-utils

Requires:	gtk4
Requires:	libadwaita

%description

%prep
cd %{_builddir}/
git clone --recurse-submodules https://gitlab.gnome.org/World/obfuscate.git
cd obfuscate
git checkout 08e4d8f60037402afbc8f61f1eeabc62c86bccf0

%build
cd obfuscate
%meson
%meson_build

%install
cd obfuscate*
%meson_install

%files
%{_bindir}/obfuscate
%{_datadir}/applications/com.belmoussaoui.Obfuscate.desktop
%{_datadir}/glib-2.0/schemas/com.belmoussaoui.Obfuscate.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/com.belmoussaoui.Obfuscate.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.belmoussaoui.Obfuscate-symbolic.svg
%{_datadir}/locale/*/LC_MESSAGES/obfuscate.mo
%{_datadir}/metainfo/com.belmoussaoui.Obfuscate.metainfo.xml
%{_datadir}/obfuscate/obfuscate.gresource

%changelog
* Mon Jun 24 2024 sunrise2011
-
