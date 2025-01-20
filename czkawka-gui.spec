Name:           czkawka
Version:        8.0.0
Release:        1%{?dist}
Summary:        Multi functional app to find duplicates, empty folders, similar images etc.

License:        GPL-3.0
URL:            https://github.com/qarmin/czkawka
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  git
BuildRequires:  meson
BuildRequires:  gtk4-devel
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  libheif-devel
BuildRequires:  LibRaw-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  gcc-c++

Requires:       gtk4
Requires:       ffmpeg-free
Requires:       libheif
Requires:       LibRaw

%description
Czkawka (tch•kav•ka (IPA: [ˈʧ̑kafka]), "hiccup" in Polish) is a simple, fast and free app to remove unnecessary files from your computer.

%prep
%setup

%build
cargo build --release --bin czkawka_gui --features "heif,libraw"

%install
%__install -d -m 0755 %{buildroot}%{_bindir}
%__install -D -m 0755 %{builddir}/%{name}-%{version}/target/release/czkawka_gui %{buildroot}%{_bindir}/czkawka-gui
%__install -D -m 0755 %{buildroot}%{_datadir}
%__install -D -m 0755 %{buildroot}%{_datadir}/applications/com.github.qarmin.czkawka.desktop
%__install -D -m 0755 %{builddir}/%{name}-%{version}/data/com.github.qarmin.czkawka.metainfo.xml %{buildroot}%{_datadir}/metainfo/com.github.qarmin.czkawka.metainfo.xml
%__install -D -m 0755 %{builddir}/%{name}-%{version}/data/icons/com.github.qarmin.czkawka.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/com.github.qarmin.czkawka.svg
%__install -D -m 0755 %{builddir}/%{name}-%{version}/data/icons/com.github.qarmin.czkawka-symbolic.svg %{buildroot}%{_datadir}/icons/hicolor/symbolic/com.github.qarmin.czkawka-symbolic.svg

%files
# %license add-license-file-here
# %doc add-docs-here
%{_bindir}/czkawka_gui
%{_datadir}/metainfo/com.github.qarmin.czkawka.metainfo.xml
%{_datadir}/applications/com.github.qarmin.czkawka.desktop
%{_datadir}/icons/hicolor/scalable/com.github.qarmin.czkawka.svg
%{_datadir}/icons/hicolor/symbolic/com.github.qarmin.czkawka-symbolic.svg

%changelog
* Sun Jun 30 2024 dfkajar <dfkajar@gmail.com>
- 
