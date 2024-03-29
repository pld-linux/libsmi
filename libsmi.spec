Summary:	Structure of Management Information library
Summary(pl.UTF-8):	Biblioteka SMI (Struktur zarządzania informacjami)
Summary(ru.UTF-8):	Библиотека для доступа к информации SMI MIB
Summary(uk.UTF-8):	Бібліотека для доступу до інформації SMI MIB
Name:		libsmi
Version:	0.5.0
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://www.ibr.cs.tu-bs.de/projects/libsmi/download/%{name}-%{version}.tar.gz
# Source0-md5:	4bf47483c06c9f07d1b10fbc74eddf11
Source1:	%{name}-smi.conf
Patch0:		flat-mibdir.patch
Patch1:		%{name}-bison.patch
URL:		http://www.ibr.cs.tu-bs.de/projects/libsmi/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
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

%package progs
Summary:	SMI tools
Summary(pl.UTF-8):	Narzędzia SMI
Group:		Networking
Requires:	%{name} = %{version}-%{release}

%description progs
SMI tools.

%description progs -l pl.UTF-8
Narzędzia SMI.

%package yang
Summary:	SMI data in Yang format
Summary(pl.UTF-8):	Dane SMI w formacie Yang
Group:		Networking
Requires:	%{name} = %{version}-%{release}

%description yang
SMI data in Yang format.

%description yang -l pl.UTF-8
Dane SMI w formacie Yang.

%package -n mibs-dirs
Summary:	Common directories for MIBs
Summary(pl.UTF-8):	Wspólne katalogi dla MIB-ów
Group:		Base

%description -n mibs-dirs
Common directories for MIBs (Management Information Base).

%description -n mibs-dirs -l pl.UTF-8
Wspólne katalogi dla danych MIB (Management Information Base).

%package -n pibs-dirs
Summary:	Common directories for PIBs
Summary(pl.UTF-8):	Wspólne katalogi dla PIB-ów
Group:		Base

%description -n pibs-dirs
Common directories for PIBs (Policy Information Base).

%description -n pibs-dirs -l pl.UTF-8
Wspólne katalogi dla danych PIB (Policy Information Base).

%package -n mibs-libsmi
Summary:	LibSMI provided MIBs
Summary(pl.UTF-8):	MIB-y dostarczane przez LibSMI
Group:		Base
Requires:	mibs-dirs

%description -n mibs-libsmi
LibSMI provided MIBs (Management Information Base).

%description -n mibs-libsmi -l pl.UTF-8
Dane MIB (Management Information Base) dostarczane przez LibSMI.

%package -n pibs-libsmi
Summary:	LibSMI provided PIBs
Summary(pl.UTF-8):	PIB-y dostarczane przez LibSMI
Group:		Base
Requires:	pibs-dirs

%description -n pibs-libsmi
LibSMI provided PIBs (Policy Information Base).

%description -n pibs-libsmi -l pl.UTF-8
Dane PIB (Policy Information Base) dostarczane przez LibSMI.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

find '(' -name '*~' -o -name '*.orig' -o -name '*-orig' ')' -print0 | xargs -0 -r -l512 rm -f

# force rebuild
touch lib/scanner-sming.l

# packaged by mibs-net-snmp
while read mib; do
	%{__rm} mibs/*/$mib
done <<'EOF'
AGENTX-MIB
DISMAN-EVENT-MIB
DISMAN-SCHEDULE-MIB
DISMAN-SCRIPT-MIB
EtherLike-MIB
HCNUM-TC
HOST-RESOURCES-MIB
HOST-RESOURCES-TYPES
IANA-ADDRESS-FAMILY-NUMBERS-MIB
IANAifType-MIB
IANA-LANGUAGE-MIB
IANA-RTPROTO-MIB
IF-INVERTED-STACK-MIB
IF-MIB
INET-ADDRESS-MIB
IP-FORWARD-MIB
IP-MIB
IPV6-ICMP-MIB
IPV6-MIB
IPV6-TC
IPV6-TCP-MIB
IPV6-UDP-MIB
MTA-MIB
NETWORK-SERVICES-MIB
NOTIFICATION-LOG-MIB
RFC1155-SMI
RFC1213-MIB
RFC-1215
RMON-MIB
SCTP-MIB
SNMP-COMMUNITY-MIB
SNMP-FRAMEWORK-MIB
SNMP-MPD-MIB
SNMP-NOTIFICATION-MIB
SNMP-PROXY-MIB
SNMP-TARGET-MIB
SNMP-USER-BASED-SM-MIB
SNMP-USM-AES-MIB
SNMP-USM-DH-OBJECTS-MIB
SNMPv2-CONF
SNMPv2-MIB
SNMPv2-SMI
SNMPv2-TC
SNMPv2-TM
SNMP-VIEW-BASED-ACM-MIB
TCP-MIB
TRANSPORT-ADDRESS-MIB
UDP-MIB
EOF

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
	--with-mibdir=%{_datadir}/mibs \
	--with-pibdir=%{_datadir}/pibs \
	--with-smipath=%{_datadir}/mibs:%{_datadir}/pibs:%{_datadir}/yang/ietf:%{_datadir}/yang/iana:%{_datadir}/yang/site

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/smi.conf

# .index files produced by net-snmp
touch $RPM_BUILD_ROOT%{_datadir}/mibs/.index
touch $RPM_BUILD_ROOT%{_datadir}/pibs/.index

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post	-n mibs-dirs -p <lua>
posix.utime("%{_datadir}/mibs");

%post	-n pibs-dirs -p <lua>
posix.utime("%{_datadir}/pibs");

%files
%defattr(644,root,root,755)
%doc ANNOUNCE COPYING ChangeLog README THANKS TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/smi.conf
%attr(755,root,root) %{_libdir}/libsmi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmi.so.2

%files devel
%defattr(644,root,root,755)
%doc doc/draft-irtf-nmrg-smi*.txt
%attr(755,root,root) %{_libdir}/libsmi.so
%{_libdir}/libsmi.la
%{_includedir}/smi.h
%{_includedir}/yang.h
%{_aclocaldir}/libsmi.m4
%{_pkgconfigdir}/libsmi.pc
%{_mandir}/man3/libsmi.3*
%{_mandir}/man3/smi_*.3*
%{_mandir}/man3/yang_node.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libsmi.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/smi*
%{_mandir}/man1/smi*.1*

%files yang
%defattr(644,root,root,755)
%{_datadir}/yang

%files -n mibs-dirs
%defattr(644,root,root,755)
%dir %{_datadir}/mibs
%ghost %{_datadir}/mibs/.index

%files -n pibs-dirs
%defattr(644,root,root,755)
%dir %{_datadir}/pibs
%ghost %{_datadir}/pibs/.index

%files -n mibs-libsmi
%defattr(644,root,root,755)
%{_datadir}/mibs/*

%files -n pibs-libsmi
%defattr(644,root,root,755)
%{_datadir}/pibs/*
