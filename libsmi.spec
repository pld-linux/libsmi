Summary:	Structure of Management Information library
Summary(pl):	Biblioteka SMI (Struktur zarz�dzania informacjami)
Name:		libsmi
Version:	0.3.1
Release:	2
License:	distributable (see COPYING)
Group:		Libraries
Source0:	ftp://ftp.ibr.cs.tu-bs.de/pub/local/libsmi/%{name}-%{version}.tar.gz
Source1:	%{name}-smi.conf
Patch0:		%{name}-sysconfdir.patch
URL:		http://www.ibr.cs.tu-bs.de/projects/libsmi/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr

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
libsmi jest bibliotek� pozwalaj�c� aplikacjom zarz�dzania sieci� na
dost�p do informacji o modu�ach MIB poprzez dobrze zdefiniowane API,
ukrywaj�ce brzydkie szczeg�y szukania i parsowania modu��w MIB
SMIv1/v2.

%package progs
Summary:	SMI tools
Summary(pl):	Narz�dzia SMI
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description progs
SMI tools.

%description progs -l pl
Narz�dzia SMI.

%package devel
Summary:	Header files and development documentation for libsmi
Summary(pl):	Pliki nag��wkowe i dokumentacja do libsmi
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libsmi.

%description devel -l pl
Pliki nag��wkowe i dokumentacja do libsmi.

%package static
Summary:	Static libsmi libraries
Summary(pl):	Biblioteki statyczne libsmi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libsmi libraries.

%description static -l pl
Biblioteki statyczne libsmi.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/smi.conf

gzip -9nf ChangeLog README THANKS TODO \
	doc/draft-irtf-nmrg-sming-*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%{_sysconfdir}/smi.conf
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/mibs

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/draft-irtf-nmrg-sming-*.txt.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
