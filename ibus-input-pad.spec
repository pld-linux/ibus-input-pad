Summary:	Input Pad for IBus
Name:		ibus-input-pad
Version:	1.4.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://input-pad.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	bc25c9c8706e6840b26a5dd79fc6b14d
URL:		http://code.google.com/p/input-pad/
BuildRequires:	gtk+3-devel
BuildRequires:	ibus-devel
BuildRequires:	input-pad-devel
BuildRequires:	libtool
Requires:	ibus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
The input pad engine for IBus platform.

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
%doc AUTHORS README
%attr(755,root,root) %{_libexecdir}/ibus-engine-input-pad
%attr(755,root,root) %{_libexecdir}/ibus-setup-input-pad
%{_datadir}/ibus/component/input-pad.xml
%{_datadir}/ibus-input-pad
