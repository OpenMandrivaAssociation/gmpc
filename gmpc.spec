Summary:	Gtk2 frontend for the mpd
Name:		gmpc
Version:	0.20.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Sound
URL:		http://gmpc.wikia.com/
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	scrollkeeper
BuildRequires:	gtk2-devel >= 2.12
BuildRequires:	libglade2.0-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libmpd-devel >= 0.19.2
BuildRequires:	gob2
BuildRequires:	intltool
BuildRequires:	curl-devel
BuildRequires:	libsexy-devel
BuildRequires:	libsoup-2.4-devel
BuildRequires:	vala
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

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

%build
%configure2_5x \
	--enable-system-libsexy \
	--disable-static

%make 

%install
rm -rf %{buildroot}
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std 

%find_lang %{name} --with-gnome

desktop-file-install \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="Audio" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
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
