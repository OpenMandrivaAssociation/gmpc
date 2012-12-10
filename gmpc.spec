Summary:	Gtk2 frontend for the mpd
Name:		gmpc
Version:	11.8.16
Release:	%mkrel 1
License:	GPLv2+
Group:		Sound
URL:		http://gmpc.wikia.com/
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
Patch0:		gmpc-11.8.16-link.patch
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0) >= 2.16
BuildRequires: pkgconfig(gmodule-2.0) >= 2.4
BuildRequires: pkgconfig(gobject-2.0) >= 2.4
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-2.0) >= 2.18
BuildRequires: pkgconfig(libmpd) >= 0.20.95
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(unique-1.0)
BuildRequires: pkgconfig(x11)
BuildRequires: libsm-devel
BuildRequires: libice-devel
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	gob2 vala

%description
GMPC is a frontend for the mpd (Music Player Daemon). 
It's focused on being fast and easy to use, while making 
optimal use of all the functions in mpd.

%package devel
Summary:        GMPC development files
Group:          Development/Other
Provides:       %{name}-devel = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}

%description devel
GMPC development files.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x \
	--disable-static

%make 

%install
%makeinstall_std

%find_lang %{name} --with-gnome

desktop-file-install \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="Audio" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_iconsdir}/*/*/*/*
%{_mandir}/man1/%{name}*

%files devel
%defattr(-,root,root)
%dir %{_includedir}/gmpc
%{_includedir}/gmpc/*.h
%{_libdir}/pkgconfig/%{name}.pc
