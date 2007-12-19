Summary:	GMPC is a gtk2 frontend for the mpd
Name:		gmpc
Version:	0.15.5.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Sound
URL:		http://sarine.nl/gmpc/
Source:		http://download.qballcow.nl/%{name}-%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	scrollkeeper
BuildRequires:	gtk2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	perl(XML::Parser) 
BuildRequires:	desktop-file-utils
BuildRequires:	libcurl-devel
BuildRequires:	libmpd-devel >= 0.15.0
Requires:	gnome-vfs2

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
	--with-curl=%{_prefix} \
	--enable-artist-browser \
	--disable-static

%make 

%install
rm -rf %{buildroot}
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std 

%find_lang %{name} --with-gnome

desktop-file-install \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="AudioVideo;Audio" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*

%files devel
%dir %{_includedir}/gmpc
%{_includedir}/gmpc/*.h
%{_libdir}/pkgconfig/%{name}.pc
