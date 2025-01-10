%global debug_package %{nil}
Name:           warehouse
Version:        2.0.2
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
%setup -n warehouse-%{version}	

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
%{_datadir}/warehouse/warehouse.gresource
%{_datadir}/warehouse/data/style.css
%{_datadir}/warehouse/src/change_version_page/change_version_page.py
%{_datadir}/warehouse/src/change_version_page/change_version_worker.py
%{_datadir}/warehouse/src/const.py
%{_datadir}/warehouse/src/gtk/app_row.py
%{_datadir}/warehouse/src/gtk/attempt_install_dialog.py
%{_datadir}/warehouse/src/gtk/error_toast.py
%{_datadir}/warehouse/src/gtk/installation_chooser.py
%{_datadir}/warehouse/src/gtk/loading_status.py
%{_datadir}/warehouse/src/gtk/sidebar_button.py
%{_datadir}/warehouse/src/host_info.py
%{_datadir}/warehouse/src/install_page/file_install_dialog.py
%{_datadir}/warehouse/src/install_page/install_page.py
%{_datadir}/warehouse/src/install_page/pending_page.py
%{_datadir}/warehouse/src/install_page/result_row.py
%{_datadir}/warehouse/src/install_page/results_page.py
%{_datadir}/warehouse/src/install_page/select_page.py
%{_datadir}/warehouse/src/main.py
%{_datadir}/warehouse/src/main_window/window.py
%{_datadir}/warehouse/src/package_install_worker.py
%{_datadir}/warehouse/src/packages_page/filters_page.py
%{_datadir}/warehouse/src/packages_page/packages_page.py
%{_datadir}/warehouse/src/packages_page/uninstall_dialog.py
%{_datadir}/warehouse/src/properties_page/properties_page.py
%{_datadir}/warehouse/src/remotes_page/add_remote_dialog.py
%{_datadir}/warehouse/src/remotes_page/remote_row.py
%{_datadir}/warehouse/src/remotes_page/remotes_page.py
%{_datadir}/warehouse/src/snapshot_page/new_snapshot_dialog.py
%{_datadir}/warehouse/src/snapshot_page/snapshot_box.py
%{_datadir}/warehouse/src/snapshot_page/snapshot_page.py
%{_datadir}/warehouse/src/snapshot_page/snapshots_list_page.py
%{_datadir}/warehouse/src/snapshot_page/tar_worker.py
%{_datadir}/warehouse/src/user_data_page/data_box.py
%{_datadir}/warehouse/src/user_data_page/data_subpage.py
%{_datadir}/warehouse/src/user_data_page/user_data_page.py


%changelog
* Sun Jun 30 2024 dfkajar <dfkajar@gmail.com>
- 
