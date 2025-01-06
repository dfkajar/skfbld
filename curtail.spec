Name:           Curtail
Version:        1.12.0
Release:        1%{?dist}
Summary:        Simple & useful image compressor.
License:        GPL-3.0
URL:            https://github.com/Huluti/Curtail
Source0:        https://github.com/Huluti/Curtail/archive/refs/tags/%{version}.tar.gz

BuildRequires:  git
BuildRequires:  meson
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  python3
BuildRequires:  desktop-file-utils

Requires:       gtk4
Requires:       libadwaita
Requires:       oxipng	
Requires:       pngquant
Requires:       jpegoptim
Requires:       libwebp
Requires:       python3-scour

%description


%prep
%autosetup

%build
%meson --buildtype release
%meson_build -j 1

%install
%meson_install

%files
# %license add-license-file-here
# %doc add-docs-here
%{_bindir}/curtail
%{_datadir}/curtail/curtail.gresource
%{_datadir}/curtail/curtail/__init__.py
%{_datadir}/curtail/curtail/compressor.py
%{_datadir}/curtail/curtail/main.py
%{_datadir}/curtail/curtail/preferences.py
%{_datadir}/curtail/curtail/resultitem.py
%{_datadir}/curtail/curtail/tools.py
%{_datadir}/curtail/curtail/window.py
%{_datadir}/applications/com.github.huluti.Curtail.desktop
%{_datadir}/glib-2.0/schemas/com.github.huluti.Curtail.gschema.xml
%{_datadir}/locale/*/LC_MESSAGES/curtail.mo
%{_datadir}/metainfo/com.github.huluti.Curtail.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/com.github.huluti.Curtail.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.github.huluti.Curtail-symbolic.svg

%changelog
* Sun Jun 30 2024 dfkajar <dfkajar@gmail.com>
- 
