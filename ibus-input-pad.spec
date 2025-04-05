Summary:	Input Pad for IBus
Summary(pl.UTF-8):	Input Pad (ekranowa tablica wprowadzania znaków) dla IBusa
Name:		ibus-input-pad
Version:	1.5.0
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/fujiwarat/ibus-input-pad/releases
Source0:	https://github.com/fujiwarat/ibus-input-pad/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	342ce2eb5a1f8cd6d344a9e3a5a458d7
URL:		https://github.com/fujiwarat/ibus-input-pad
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.37.0
BuildRequires:	gtk+3-devel >= 3.10
BuildRequires:	ibus-devel >= 1.5.3
BuildRequires:	input-pad-devel >= 1.1
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.37.0
Requires:	gtk+3 >= 3.10
Requires:	ibus >= 1.5.3
Requires:	input-pad >= 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
The input pad engine for IBus platform.

%description -l pl.UTF-8
Silnik Input Pad (ekranowa tablica wprowadzania znaków) dla platformy
IBus.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libexecdir}/ibus-engine-input-pad
%attr(755,root,root) %{_libexecdir}/ibus-setup-input-pad
%{_datadir}/ibus/component/input-pad.xml
%{_desktopdir}/ibus-setup-input-pad.desktop
