Summary:	KSBA library
Summary(pl):	Biblioteka KSBA
Name:		libksba
Version:	0.4.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/aegypten/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSBA library.

%description -l pl
Biblioteka KSBA.

%package devel
Summary:	Header files to develop KSBA applications
Summary(pl):	Pliki nag³ówkowe do tworzenia programów u¿ywaj±cych KSBA
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files to develop KSBA applications.

%description devel -l pl
Pliki nag³ówkowe do tworzenia programów u¿ywaj±cych KSBA.

%package static
Summary:	Static KSBA library
Summary(pl):	Statyczna biblioteka KSBA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static KSBA library.

%description static -l pl
Statyczna biblioteka KSBA.

%prep
%setup -q

%build
%configure --enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_infodir}/*info*
%{_includedir}/*.h
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
