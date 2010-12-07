%define name    rev-plugins
%define version 0.3.1
%define release %mkrel 5

Summary:        A reverb plugin for LADSPA
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPLv2
Group:          Sound
Source:         http://www.kokkinizita.net/linuxaudio/downloads/REV-plugins-%{version}.tar.bz2
URL:            http://www.kokkinizita.net/linuxaudio
BuildRoot:      %{_tmppath}/%{name}-buildroot
Requires:       ladspa

%description
This reverb is based on gverb by Juhana Sadeharju, but the code
(now C++) is entirely original, including a second input for stereo
operation, and some code to prevent FP denormalisation.

%prep
%setup -q -n REV-plugins-%{version}
perl -p -i -e 's/\-O2/\$\(RPM_OPT_FLAGS\)/g' Makefile
perl -p -i -e 's/\/usr\/lib\/ladspa/\$\(DESTDIR\)\/usr\/%_lib\/ladspa/g' Makefile

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ladspa
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README
%{_libdir}/ladspa/*.so

