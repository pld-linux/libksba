Summary:	KSBA = rot13(digit_to_letter(x509)) to be pronounced as Kasbah
Summary(es):	KSBA = rot13(digit_to_letter(x509))
Summary(pl):	KSBA = rot13(digit_to_letter(x509)), wymawiane "kasba"
Summary(pt_BR):	KSBA = rot13(digit_to_letter(x509)) pronunciado como Kasbah
Name:		libksba
Version:	0.9.15
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/libksba/%{name}-%{version}.tar.bz2
# Source0-md5:	2a35d17a3d014f67e893c5134d26b877
Patch0:		%{name}-info.patch
Patch1:		%{name}-link.patch
URL:		http://www.gnupg.org/related_software/libksba/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9.3
BuildRequires:	libgpg-error-devel >= 0.7
BuildRequires:	libtool
BuildRequires:	texinfo
Requires:	libgpg-error >= 0.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSBA is a library to make the tasks of working with X.509
certificates, CMS data and related data more easy.

%description -l pl
KSBA jest bibliotek± u³atwiaj±c± korzystanie z certyfikatów X.509,
danych CMS i podobnych danych.

%description -l pt_BR
KSBA é uma biblioteca para tratar certificados X.509, dados CMS e
dados relacionados de forma fácil.

%package devel
Summary:	Header files to develop KSBA applications
Summary(es):	Archivos de desarrollo de KSBA
Summary(pl):	Pliki nag³ówkowe do tworzenia programów u¿ywaj±cych KSBA
Summary(pt_BR):	Arquivos de desenvolvimento da KSBA
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgpg-error-devel >= 0.7

%description devel
Header files to develop KSBA applications.

%description devel -l pl
Pliki nag³ówkowe do tworzenia programów u¿ywaj±cych KSBA.

%description devel -l pt_BR
Bibliotecas de desenvolvimento para KSBA.

%package static
Summary:	Static KSBA libraries
Summary(es):	Archivos de desarrollo de KSBA - estatico
Summary(pl):	Biblioteki statyczne KSBA
Summary(pt_BR):	Arquivos de desenvolvimento da KSBA - biblioteca estática
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static KSBA libraries.

%description static -l pl
Biblioteki statyczne KSBA.

%description static -l pt_BR
Bibliotecas de desenvolvimento para KSBA - estático.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I gl/m4
%{__autoconf}
%{__automake}
%configure

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
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_infodir}/*.info*
%{_includedir}/*.h
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
