Name:           newsflash
Version:        3.3.4
Release:        2%{?dist}
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
BuildRequires:  libmicrodns
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
cd %{_builddir}/
git clone https://gitlab.com/news-flash/news_flash_gtk.git
cd %{_builddir}/news_flash_gtk
git checkout ed5773bf225659e62f262dd08bbad6f9a5304a92

%build
export RUSTFLAGS="%build_rustflags"
cd news_flash_gtk
%meson
%meson_build

%install
cd news_flash_gtk*
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
