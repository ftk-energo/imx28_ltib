%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : The Typesafe Signal Framework for C++
Name            : libsigc++
Version         : 2.0.3
Release         : 1
Vendor          : Freescale
Packager        : Stuart Hughes
Group           : System Environment/Libraries
Source          : %{name}-%{version}.tar.bz2
License         : LGPL
BuildRoot       : %{_tmppath}/%{name}

%Description
%{summary}

%Prep
%setup 

%Build
./configure --prefix=%{_prefix} --enable-shared=yes --disable-dependency-tracking --enable-examples=no --enable-tests=no
make

%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}

%Clean
rm -rf $RPM_BUILD_ROOT


%Files
%defattr(-,root,root)
%{pfx}/*
