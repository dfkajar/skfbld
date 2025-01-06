Name:           warehouse
Version:        2.0.1-1
Release:        1%{?dist}
Summary:        A versatile toolbox for viewing flatpak info, managing user data, and batch managing installed flatpaks
License:        GPL-3.0
URL:            https://github.com/flattool/warehouse
Source0:        https://github.com/flattool/warehouse/archive/refs/tags/%{version}.tar.gz

BuildRequires:  git
BuildRequires:  meson
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  appstream-devel
BuildRequires:  python3
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:  gettext-devel
BuildRequires:  python3-gettext

Requires:       gtk4
Requires:       libadwaita
Requires:       python3

%description

%prep
%setup

%build
%meson --buildtype release
%meson_build -j 1

%install
%meson_install


%files
%{_bindir}/warehouse
%{_datadir}/applications/io.github.flattool.Warehouse.desktop
%{_datadir}/glib-2.0/schemas/io.github.flattool.Warehouse.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/io.github.flattool.Warehouse.svg
%{_datadir}/icons/hicolor/symbolic/apps/io.github.flattool.Warehouse-symbolic.svg
%{_datadir}/locale/*/LC_MESSAGES/warehouse.mo
%{_datadir}/metainfo/io.github.flattool.Warehouse.metainfo.xml
%{_datadir}/warehouse/flattool_gui/__init__.py
%{_datadir}/warehouse/flattool_gui/app_row_widget.py
%{_datadir}/warehouse/flattool_gui/common.py
%{_datadir}/warehouse/flattool_gui/const.py
%{_datadir}/warehouse/flattool_gui/downgrade.blp
%{_datadir}/warehouse/flattool_gui/downgrade_window.py
%{_datadir}/warehouse/flattool_gui/filter.blp
%{_datadir}/warehouse/flattool_gui/filter_window.py
%{_datadir}/warehouse/flattool_gui/main.py
%{_datadir}/warehouse/flattool_gui/orphans.blp
%{_datadir}/warehouse/flattool_gui/orphans_window.py
%{_datadir}/warehouse/flattool_gui/properties.blp
%{_datadir}/warehouse/flattool_gui/properties_window.py
%{_datadir}/warehouse/flattool_gui/remotes.blp
%{_datadir}/warehouse/flattool_gui/remotes_window.py
%{_datadir}/warehouse/flattool_gui/search_install.blp
%{_datadir}/warehouse/flattool_gui/search_install_window.py
%{_datadir}/warehouse/flattool_gui/snapshots.blp
%{_datadir}/warehouse/flattool_gui/snapshots_window.py
%{_datadir}/warehouse/flattool_gui/style.css
%{_datadir}/warehouse/flattool_gui/window.py
%{_datadir}/warehouse/warehouse.gresource

%changelog
* Sun Jun 30 2024 dfkajar <dfkajar@gmail.com>
- 
