%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Firmware for imx platform
Name            : firmware-imx
Version         : 10.12.01
Release         : 1
License         : Freescale EULA
Vendor          : Freescale and third party
Packager        : Alan Tull
Group           : System Environment/Libraries
Source          : %{name}-%{version}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

Binary only package.

%Prep
%setup

%Build

%Install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{pfx}/lib/firmware
cp -rf firmware/* $RPM_BUILD_ROOT/%{pfx}/lib/firmware

install -d $RPM_BUILD_ROOT/%{pfx}/usr/share/doc/linux-firmware/licenses
cp -rf licenses/* $RPM_BUILD_ROOT/%{pfx}/usr/share/doc/linux-firmware/licenses

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
