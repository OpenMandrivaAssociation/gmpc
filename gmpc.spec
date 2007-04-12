%define name gmpc
%define version 0.14.0
%define release %mkrel 1

%define Summary Gmpc is a gtk2 frontend for the mpd
%define title	Gmpc
%define section Multimedia/Sound 

Summary: 	%Summary
Name: 		%name
Version: 	%version
Release: 	%release
License: GPL
Group: 		Sound
URL: 		http://qballcow.nl/?s=11

Source: 	http://download.qballcow.nl/programs/gmpc/%name-%version.tar.bz2
Source1:	%name-16.png
Source2:	%name-32.png
Source3:	%name.png

BuildRoot: 	%_tmppath/%{name}-%{version}-%{release}-buildroot

BuildRequires: scrollkeeper, gtk2-devel, libglade2.0-devel, gnome-vfs2-devel
BuildRequires: perl-XML-Parser desktop-file-utils libcurl-devel
BuildRequires: libmpd-devel

Requires: gnome-vfs2

%description
MPD supports ogg, flac and mp3 and is very stable 
and light weight, supporting playlists and huge 
libraries.

Features :

 * Support for loading/saving playlists. 
 * File Browser 
 * Browser based on ID3 information. (on artist and albums) 
 * Search 
 * Current playlist viewer with search. 
 * ID3 information 
 * Lots more 

%package devel
Summary:        gmpc devel file
Requires:       %name = %version-%release
Group:          Development/Other
Provides:       %name-devel = %version-%release

%description devel
gmpc devel file

# Prep
%prep
%setup -q

%build
%configure2_5x

%make WARN_CFLAGS=""

%install
rm -rf %buildroot
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std 

%find_lang %name --with-gnome

# menu
mkdir -p %buildroot/%_menudir
cat > %buildroot/%_menudir/%name << EOF
?package(%name): \
command="%_bindir/%name" \
needs="x11" \
icon="%name.png" \
section="%section" \
title="%title" \
longtitle="%Summary" \
xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

# icon
mkdir -p %buildroot/{%_liconsdir,%_iconsdir,%_miconsdir}
#install -m 644 src/pixmaps/%name.png %buildroot/%_datadir/pixmaps/%name.png
install -m 644 %SOURCE1 %buildroot/%_miconsdir/%name.png
install -m 644 %SOURCE2 %buildroot/%_liconsdir/%name.png
install -m 644 %SOURCE3 %buildroot/%_iconsdir/%name.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)

%doc AUTHORS ChangeLog NEWS README

%{_bindir}/%name
%{_datadir}/applications/%name.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_datadir}/pixmaps/*
%_menudir/%name
%_liconsdir/%name.png
%_miconsdir/%name.png
%_iconsdir/%name.png

%files devel
%{_includedir}/gmpc/*.h
%{_libdir}/pkgconfig/%{name}.pc



