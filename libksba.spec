Summary:	KSBA = rot13(digit_to_letter(x509)) to be pronounced as Kasbah
Summary(es):	KSBA = rot13(digit_to_letter(x509))
Summary(pt_BR):	KSBA = rot13(digit_to_letter(x509)) pronunciado como Kasbah
Summary(pl):	KSBA = rot13(digit_to_letter(x509))
Name:		libksba
Version:	0.4.7
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/aegypten/%{name}-%{version}.tar.gz
Patch0:		%{name}-info.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSBA is a library to make the tasks of working with X.509
certificates, CMS data and related data more easy.

%description -l pt_BR
KSBA é uma biblioteca para tratar certificados X.509, dados CMS e
dados relacionados de forma fácil.

%package devel
Summary:	Header files to develop KSBA applications
Summary(es):	Archivos de desarrollo de KSBA
Summary(pl):	Pliki nag³ówkowe do tworzenia programów u¿ywaj±cych KSBA
Summary(pt_BR):	Arquivos de desenvolvimento da KSBA
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files to develop KSBA applications.

%description devel -l pl
Pliki nag³ówkowe do tworzenia programów u¿ywaj±cych KSBA.

%description devel -l pt_BR
Bibliotecas de desenvolvimento para KSBA.

%package static
Summary:	Development files from KSBA - static lib
Summary(es):	Archivos de desarrollo de KSBA - estatico
Summary(pt_BR):	Arquivos de desenvolvimento da KSBA - biblioteca estática
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
KSBA devel libraries - static.

%description static -l pt_BR
Bibliotecas de desenvolvimento para KSBA - estático.

%prep
%setup -q
%patch -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared

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
