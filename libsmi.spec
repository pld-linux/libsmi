Summary:	Structure of Management Information library
Summary(pl):	Biblioteka SMI (Struktur zarz╠dzania informacjami)
Summary(ru):	Библиотека для доступа к информации SMI MIB
Summary(uk):	Б╕бл╕отека для доступу до ╕нформац╕╖ SMI MIB
Name:		libsmi
Version:	0.4.3
Release:	1
License:	BSD
Group:		Libraries
Source0:	ftp://ftp.ibr.cs.tu-bs.de/pub/local/libsmi/%{name}-%{version}.tar.gz
# Source0-md5:	aca6bbeaff025d38c58f26ecbd70b604
Source1:	%{name}-smi.conf
Patch0:		%{name}-sysconfdir.patch
Patch1:		%{name}-am18.patch
URL:		http://www.ibr.cs.tu-bs.de/projects/libsmi/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libsmi is a C library that allows network management applications to
access MIB module information through a well defined API that hides
the nasty details of locating and parsing SMIv1/v2 MIB modules.

Libsmi supports exact and iterative retrieval functions for all major
SMIv1 and SMIv2 constructs (except the AGENT-CAPABILITIES statement).

The layered concept of libsmi allows to add further methods to
retrieve MIB information from persistent repositories. In fact,
besides the SMIv1/v2 MIB file parser an additional parser for `SMIng'
is included. Both parsers are built on flex/bison grammar
specifications.

SMIng is a research project concerned with the definition of a MIB
module language that is semantically fully compatible with SMIv2 but
avoids many problems of the ASN.1 based SMI versions.

Included with the library, there are three tools that make use of
libsmi: Smiquery allows simple queries of single MIB module items.
Smilint allows to increase the verbosity of the parser(s), so that MIB
modules can be checked for syntax and semantic errors. Finally,
smidump can be used to dump MIB modules. Currently, SMIng and SMIv2
are supported as output formats, so that SMIv2 <-> SMIng conversions
are possible.

%description -l pl
libsmi jest bibliotek╠ pozwalaj╠c╠ aplikacjom zarz╠dzania sieci╠ na
dostЙp do informacji o moduЁach MIB poprzez dobrze zdefiniowane API,
ukrywaj╠ce brzydkie szczegСЁy szukania i parsowania moduЁСw MIB
SMIv1/v2.

%description -l ru
Libsmi - это C библиотека, дающая программам управления сетью доступ к
информационным модулям MIB посредством хорошо определенного API,
который прячет неприятные детали поиска и разбора модулей SMIv1/v2
MIB.

%description -l uk
Libsmi - це C б╕бл╕отека, що нада╓ програмам управл╕ння мережею доступ
до ╕нформац╕йних модул╕в MIB через добре визначений API, що прихову╓
непри╓мн╕ детал╕ пошуку та розбору модул╕в SMIv1/v2 MIB.

%package progs
Summary:	SMI tools
Summary(pl):	NarzЙdzia SMI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description progs
SMI tools.

%description progs -l pl
NarzЙdzia SMI.

%package devel
Summary:	Header files and development documentation for libsmi
Summary(pl):	Pliki nagЁСwkowe i dokumentacja do libsmi
Summary(ru):	Хедеры для разработки программ с использованием libsmi
Summary(uk):	Хедери для розробки програм з використанням libsmi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for libsmi.

%description devel -l pl
Pliki nagЁСwkowe i dokumentacja do libsmi.

%description devel -l ru
Хедеры для разработки программ с использованием libsmi.

%description devel -l uk
Хедери для розробки програм з використанням libsmi.

%package static
Summary:	Static libsmi libraries
Summary(pl):	Biblioteki statyczne libsmi
Group:		Development/Libraries
Summary(ru):	Статические библиотеки для разработки программ с использованием libsmi
Summary(uk):	Статичн╕ б╕бл╕отеки для розробки програм з використанням libsmi
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsmi libraries.

%description static -l pl
Biblioteki statyczne libsmi.

%description static -l ru
Статические библиотеки для разработки программ с использованием
libsmi.

%description static -l uk
Статичн╕ б╕бл╕отеки для розробки програм з використанням libsmi.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/smi.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE COPYING ChangeLog README THANKS TODO
%{_sysconfdir}/smi.conf
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/mibs
%{_datadir}/pibs

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc doc/draft-irtf-nmrg-smi*.txt
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
