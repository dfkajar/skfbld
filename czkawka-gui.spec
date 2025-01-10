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
BuildRequires:  ffmpeg

Requires:       gtk4
Requires:       ffmpeg
Requires:       libheif
Requires:       LibRaw

%description
Czkawka (tch•kav•ka (IPA: [ˈʧ̑kafka]), "hiccup" in Polish) is a simple, fast and free app to remove unnecessary files from your computer.

%prep
%setup

%build
cargo run --release --bin czkawka_gui --features "heif,libraw"

%install
# %meson_install

%files
%license add-license-file-here
%doc add-docs-here

%changelog
* Sun Jun 30 2024 dfkajar <dfkajar@gmail.com>
- 
