%global debug_package %{nil}
Name:       	eartag
Version:    	0.6.3
Release:    	1%{?dist}
Summary:        Simple music tag editor

License:        GPL-3.0
URL:           	https://gitlab.gnome.org/World/eartag
Source0:        https://gitlab.gnome.org/World/eartag/-/archive/%{version}/eartag-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  meson
BuildRequires:  cargo
BuildRequires:  gtk4-devel
BuildRequires:  pygobject2-devel
BuildRequires:  python3-pillow-devel
BuildRequires:  python3-file-magic
BuildRequires:  desktop-file-utils
BuildRequires:  libadwaita-devel
BuildRequires:  blueprint-compiler

Requires:	python3
Requires:       gtk4
Requires:       libadwaita
Requires:       python3-mutagen
Requires:       python3-eyed3
Requires:       python3-pytaglib
Requires:       python3-pillow
Requires:       pygobject2
Requires:       python3-file-magic
Requires:       python3-acoustid

%description

%prep
%setup

%build
%meson --buildtype release
%meson_build -j 1

%install
%meson_install

%files
%{_bindir}/eartag
%{_datadir}/eartag/eartag/config.py
%{_datadir}/eartag/eartag/extract.py
%{_datadir}/eartag/eartag/filelist.py
%{_datadir}/eartag/eartag/identify.py
%{_datadir}/eartag/eartag/musicbrainz.py
%{_datadir}/eartag/eartag/utils/__init__.py
%{_datadir}/eartag/eartag/utils/bgtask.py
%{_datadir}/eartag/eartag/utils/extracttags.py
%{_datadir}/eartag/eartag/utils/limiters.py
%{_datadir}/eartag/eartag/utils/misc.py
%{_datadir}/eartag/eartag/utils/previewselector.py
%{_datadir}/eartag/eartag/utils/tagselector.py
%{_datadir}/eartag/eartag/utils/tagsyntaxhighlight.py
%{_datadir}/eartag/eartag/utils/validation.py
%{_datadir}/eartag/eartag/utils/widgets.py
%{_datadir}/eartag/eartag/backends/file_mutagen_asf.py
%{_datadir}/eartag/eartag/backends/file_mutagen_common.py
%{_datadir}/eartag/eartag/backends/file_mutagen_id3.py
%{_datadir}/eartag/eartag/backends/file_mutagen_mp4.py
%{_datadir}/metainfo/app.drey.EarTag.metainfo.xml
%{_datadir}/applications/app.drey.EarTag.desktop
%{_datadir}/eartag/eartag.gresource
%{_datadir}/eartag/eartag/__init__.py
%{_datadir}/eartag/eartag/backends/__init__.py
%{_datadir}/eartag/eartag/backends/file.py
%{_datadir}/eartag/eartag/backends/file_mutagen_vorbis.py
%{_datadir}/eartag/eartag/fileview.py
%{_datadir}/eartag/eartag/main.py
%{_datadir}/eartag/eartag/window.py
%{_datadir}/eartag/eartag/dialogs.py
%{_datadir}/eartag/eartag/filemanager.py
%{_datadir}/eartag/eartag/rename.py
%{_datadir}/eartag/eartag/tagentry.py
%{_datadir}/glib-2.0/schemas/app.drey.EarTag.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/app.drey.EarTag.svg
%{_datadir}/icons/hicolor/symbolic/apps/app.drey.EarTag-symbolic.svg
%{_datadir}/locale/*/LC_MESSAGES/app.drey.EarTag.mo

%changelog
* Sun Jun 30 2024 dfkajar <dfkajar@gmail.com>
-
