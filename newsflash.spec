Name:           newsflash
Version:        3.3.5
Release:        1%{?dist}
Summary:        Follow your favorite blogs & news sites.
License:        GPL-3.0
URL:            https://gitlab.com/news-flash/news_flash_gtk
Source0:        https://gitlab.com/news-flash/news_flash_gtk/-/archive/v.%{version}/news_flash_gtk-v.%{version}.tar.gz

BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  rust-openssl-devel
BuildRequires:  sqlite-devel
BuildRequires:  gettext-devel
BuildRequires:  xdg-utils
BuildRequires:  blueprint-compiler
BuildRequires:  clapper-devel
BuildRequires:  webkitgtk6.0-devel
BuildRequires:  libmicrodns-devel

Requires:       webkitgtk6.0
Requires:       libadwaita
Requires:       gtk4
Requires:       sqlite3
Requires:       gettext
Requires:       openssl
Requires:       libmicrodns

%description


%prep
%setup -n news-flash-gtk-v.%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/io.gitlab.news_flash.NewsFlash
%{_datadir}/icons/hicolor/*/apps/io.gitlab.news_flash.NewsFlash*.svg
%{_datadir}/applications/io.gitlab.news_flash.NewsFlash.desktop
%{_datadir}/locale/*/LC_MESSAGES/newsflash.mo
%{_datadir}/metainfo/io.gitlab.news_flash.NewsFlash.appdata.xml

%changelog
* Tue Jun 25 2024 dfkajar <dfkajar@gmail.com>
-
