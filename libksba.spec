Summary:	KSBA = rot13(digit_to_letter(x509)) to be pronounced as Kasbah
Summary(es.UTF-8):	KSBA = rot13(digit_to_letter(x509))
Summary(pl.UTF-8):	KSBA = rot13(digit_to_letter(x509)), wymawiane "kasba"
Summary(pt_BR.UTF-8):	KSBA = rot13(digit_to_letter(x509)) pronunciado como Kasbah
Name:		libksba
Version:	1.0.4
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/libksba/%{name}-%{version}.tar.bz2
# Source0-md5:	9a512633269e8f30e88abfd3b4105c3c
Patch0:		%{name}-info.patch
Patch1:		%{name}-link.patch
URL:		http://www.gnupg.org/related_software/libksba/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.10
BuildRequires:	libgpg-error-devel >= 1.4
BuildRequires:	libtool
BuildRequires:	texinfo
Requires:	libgpg-error >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSBA is a library to make the tasks of working with X.509
certificates, CMS data and related data more easy.

%description -l pl.UTF-8
KSBA jest biblioteką ułatwiającą korzystanie z certyfikatów X.509,
danych CMS i podobnych danych.

%description -l pt_BR.UTF-8
KSBA é uma biblioteca para tratar certificados X.509, dados CMS e
dados relacionados de forma fácil.

%package devel
Summary:	Header files to develop KSBA applications
Summary(es.UTF-8):	Archivos de desarrollo de KSBA
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia programów używających KSBA
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento da KSBA
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgpg-error-devel >= 1.4

%description devel
Header files to develop KSBA applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia programów używających KSBA.

%description devel -l pt_BR.UTF-8
Bibliotecas de desenvolvimento para KSBA.

%package static
Summary:	Static KSBA libraries
Summary(es.UTF-8):	Archivos de desarrollo de KSBA - estatico
Summary(pl.UTF-8):	Biblioteki statyczne KSBA
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento da KSBA - biblioteca estática
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static KSBA libraries.

%description static -l pl.UTF-8
Biblioteki statyczne KSBA.

%description static -l pt_BR.UTF-8
Bibliotecas de desenvolvimento para KSBA - estático.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I gl/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_libdir}/libksba.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libksba.so.8

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksba-config
%attr(755,root,root) %{_libdir}/libksba.so
%{_libdir}/libksba.la
%{_infodir}/ksba.info*
%{_includedir}/ksba.h
%{_aclocaldir}/ksba.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libksba.a
