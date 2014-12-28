Summary:	Input Pad for IBus
Summary(pl.UTF-8):	Input Pad (ekranowa tablica wprowadzania znaków) dla IBusa
Name:		ibus-input-pad
Version:	1.4.2
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://code.google.com/p/input-pad/downloads/list
Source0:	http://input-pad.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	942e8b36eb0fb1208fd48c3ff3fbf3b4
URL:		http://code.google.com/p/input-pad/
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.8
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	ibus-devel >= 1.4
BuildRequires:	input-pad-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.8
Requires:	gtk+3 >= 3.0
Requires:	ibus >= 1.4
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
%configure \
	--with-gtk=3.0

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
%{_datadir}/ibus-input-pad
%{_desktopdir}/ibus-setup-input-pad.desktop
