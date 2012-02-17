Name:           tangogis
Version:        1.0.0
Release:        1%{?dist}.R
Summary:        GTK+ mapping and GPS application
Summary(ru):    GTK+ карты, навигация, GPS

Group:          Applications/Productivity
License:        GPLv2
URL:            http://www.tangogps.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#Source0:       http://tangogis.googlecode.com/files/%{name}-%{version}.tar.bz2
Source0:        %{name}-%{version}.svn60.tar.xz
Source1:        %{name}.desktop
Source100:      README.RFRemix

BuildRequires:  bluez-libs-devel
BuildRequires:  dbus-devel
BuildRequires:  gtk2-devel
BuildRequires:  GConf2-devel
BuildRequires:  libcurl-devel
BuildRequires:  libexif-devel
BuildRequires:  libsoup-devel
BuildRequires:  libxml2-devel
BuildRequires:  sqlite-devel
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  cmake

Requires:   dbus
Requires:   gpsd
Requires:   gpscorrelate
Requires:   jhead

%description
Tangogis is a fork of tangogps for to make better view, addition many various
functions(e.g. supporting WGS-84 Mercator and other maps) and many
tangogps-bugs fix. Mainstream of project is a creation fast easy for use and
relaible software product for use as car computer on unix-like OS platform
hardware.

%prep
%setup -q -n %{name}-%{version}.svn60


%build
mkdir build
cd build
%{cmake} ..
make %{?_smp_mflags}
cd ..
cp %{SOURCE100} .

%install
rm -rf $RPM_BUILD_ROOT
cd build
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --vendor="fedora" \
--dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
rm -rf %{buildroot}/usr/doc/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README README.RFRemix
%{_bindir}/%{name}
%{_datadir}/applications/fedora-%{name}.desktop
%{_datadir}/%{name}/interface.glade


%changelog
* Fri Feb 17 2012 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.0.svn60-1.R
- Initial package for Fedora.
