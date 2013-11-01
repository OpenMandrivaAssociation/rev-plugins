%define name    rev-plugins
%define version 0.3.1
%define release %mkrel 5

Summary:        A reverb plugin for LADSPA
Name:           %{name}
Version:        0.6.1
Release:        1
License:        GPLv2
Group:          Sound
Source:         http://www.kokkinizita.net/linuxaudio/downloads/REV-plugins-%{version}.tar.bz2
URL:            http://www.kokkinizita.net/linuxaudio
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
mkdir -p %{buildroot}%{_libdir}/ladspa
make DESTDIR=%{buildroot} install

%clean

%files
%doc AUTHORS README
%{_libdir}/ladspa/*.so



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-5mdv2011.0
+ Revision: 614707
- the mass rebuild of 2010.1 packages

* Fri Apr 09 2010 Frank Kober <emuse@mandriva.org> 0.3.1-4mdv2010.1
+ Revision: 533407
- drop patch0, update url, rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import rev-plugins

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Thu Aug 25 2005 Austin Acton <austin@mandriva.org> 0.3.1-1mdk
- 0.3.1
- build flags

* Sat May 8 2004 Austin Acton <austin@mandrake.org> 0.2.1-1mdk
- initial package

