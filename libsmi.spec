Summary:	Structure of Management Information library
Summary(pl.UTF-8):	Biblioteka SMI (Struktur zarządzania informacjami)
Summary(ru.UTF-8):	Библиотека для доступа к информации SMI MIB
Summary(uk.UTF-8):	Бібліотека для доступу до інформації SMI MIB
Name:		libsmi
Version:	0.4.8
Release:	1.5
License:	BSD
Group:		Libraries
Source0:	ftp://ftp.ibr.cs.tu-bs.de/pub/local/libsmi/%{name}-%{version}.tar.gz
# Source0-md5:	760b6b1070738158708649ed2c63425e
Source1:	%{name}-smi.conf
URL:		http://www.ibr.cs.tu-bs.de/projects/libsmi/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Suggests:	mibs-libsmi
Suggests:	pibs-libsmi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libsmi is a C library that allows network management applications to
access MIB module information through a well defined API that hides
the nasty details of locating and parsing SMIv1/v2 MIB modules.

Libsmi supports exact and iterative retrieval functions for all major
SMIv1 and SMIv2 constructs (except the AGENT-CAPABILITIES statement).

%description -l pl.UTF-8
libsmi jest biblioteką pozwalającą aplikacjom zarządzania siecią na
dostęp do informacji o modułach MIB poprzez dobrze zdefiniowane API,
ukrywające brzydkie szczegóły szukania i analizy modułów MIB SMIv1/v2.

libsmi obsługuje dokładne i iterujące funkcje odczytujące dla
wszystkich głównych konstrukcji SMIv1 i SMIv2 (poza instrukcją
AGENT-CAPABILITIES).

%description -l ru.UTF-8
Libsmi - это C библиотека, дающая программам управления сетью доступ к
информационным модулям MIB посредством хорошо определенного API,
который прячет неприятные детали поиска и разбора модулей SMIv1/v2
MIB.

%description -l uk.UTF-8
Libsmi - це C бібліотека, що надає програмам управління мережею доступ
до інформаційних модулів MIB через добре визначений API, що приховує
неприємні деталі пошуку та розбору модулів SMIv1/v2 MIB.

%package progs
Summary:	SMI tools
Summary(pl.UTF-8):	Narzędzia SMI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description progs
SMI tools.

%description progs -l pl.UTF-8
Narzędzia SMI.

%package -n mibs-dirs
Summary:	Common directories for MIBs
Group:		Base

%description -n mibs-dirs
Common directories for MIBs (Management Information Base).

%package -n pibs-dirs
Summary:	LibSMI provided PIBs
Group:		Base

%description -n pibs-dirs
Common directories for PIBs (Policy Information Base).

%package -n mibs-libsmi
Summary:	LibSMI provided MIBs
Group:		Base
Requires:	mibs-dirs

%description -n mibs-libsmi
LibSMI provided MIBs (Management Information Base).

%package -n pibs-libsmi
Summary:	LibSMI provided PIBs
Group:		Base
Requires:	pibs-dirs

%description -n pibs-libsmi
LibSMI provided PIBs (Policy Information Base).

%package devel
Summary:	Header files and development documentation for libsmi
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do libsmi
Summary(ru.UTF-8):	Хедеры для разработки программ с использованием libsmi
Summary(uk.UTF-8):	Хедери для розробки програм з використанням libsmi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for libsmi.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libsmi.

%description devel -l ru.UTF-8
Хедеры для разработки программ с использованием libsmi.

%description devel -l uk.UTF-8
Хедери для розробки програм з використанням libsmi.

%package static
Summary:	Static libsmi libraries
Summary(pl.UTF-8):	Biblioteki statyczne libsmi
Summary(ru.UTF-8):	Статические библиотеки для разработки программ с использованием libsmi
Summary(uk.UTF-8):	Статичні бібліотеки для розробки програм з використанням libsmi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsmi libraries.

%description static -l pl.UTF-8
Biblioteki statyczne libsmi.

%description static -l ru.UTF-8
Статические библиотеки для разработки программ с использованием
libsmi.

%description static -l uk.UTF-8
Статичні бібліотеки для розробки програм з використанням libsmi.

%prep
%setup -q

find '(' -name '*~' -o -name '*.orig' -o -name '*-orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-smi \
	--enable-sming \
	--enable-shared \
	--enable-static \
	--with-mibdir=%{_datadir}/mibs

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/smi.conf

# .index files produced by net-snmp
touch $RPM_BUILD_ROOT%{_datadir}/mibs/{,iana,ietf,irtf,site,tubs}/.index
touch $RPM_BUILD_ROOT%{_datadir}/pibs/{,ietf,site,tubs}/.index

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE COPYING ChangeLog README THANKS TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/smi.conf
%attr(755,root,root) %{_libdir}/libsmi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmi.so.2

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/smi*
%{_mandir}/man1/smi*.1*

%files -n mibs-dirs
%defattr(644,root,root,755)
%dir %{_datadir}/mibs
%dir %{_datadir}/mibs/iana
%dir %{_datadir}/mibs/ietf
%dir %{_datadir}/mibs/irtf
%dir %{_datadir}/mibs/site
%dir %{_datadir}/mibs/tubs

%ghost %{_datadir}/mibs/.index
%ghost %{_datadir}/mibs/iana/.index
%ghost %{_datadir}/mibs/ietf/.index
%ghost %{_datadir}/mibs/irtf/.index
%ghost %{_datadir}/mibs/site/.index
%ghost %{_datadir}/mibs/tubs/.index

%files -n pibs-dirs
%defattr(644,root,root,755)
%dir %{_datadir}/pibs
%dir %{_datadir}/pibs/ietf
%dir %{_datadir}/pibs/site
%dir %{_datadir}/pibs/tubs

%ghost %{_datadir}/pibs/.index
%ghost %{_datadir}/pibs/ietf/.index
%ghost %{_datadir}/pibs/site/.index
%ghost %{_datadir}/pibs/tubs/.index

%files -n mibs-libsmi
%defattr(644,root,root,755)
%{_datadir}/mibs/iana/*
%{_datadir}/mibs/ietf/*
%{_datadir}/mibs/irtf/*
%{_datadir}/mibs/tubs/*

%files -n pibs-libsmi
%defattr(644,root,root,755)
%{_datadir}/pibs/COPS-PR-SPPI*
%{_datadir}/pibs/*-PIB

%files devel
%defattr(644,root,root,755)
%doc doc/draft-irtf-nmrg-smi*.txt
%attr(755,root,root) %{_libdir}/libsmi.so
%{_libdir}/libsmi.la
%{_includedir}/smi.h
%{_aclocaldir}/libsmi.m4
%{_pkgconfigdir}/libsmi.pc
%{_mandir}/man3/libsmi.3*
%{_mandir}/man3/smi_*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libsmi.a
