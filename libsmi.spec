Summary:	Structure of Management Information library
Name:		libsmi
Version:	0.1.7
Release:	1
Copyright:	distributable (see COPYING file)
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://ftp.ibr.cs.tu-bs.de/pub/local/libsmi/%{name}-%{version}.tar.gz
URL:		http://www.ibr.cs.tu-bs.de/projects/libsmi/
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr

%description
Libsmi is a C library that allows network management applications to access
MIB module information through a well defined API that hides the nasty
details of locating and parsing SMIv1/v2 MIB modules.

Libsmi supports exact and iterative retrieval functions for all major SMIv1
and SMIv2 constructs (except the AGENT-CAPABILITIES statement).

The layered concept of libsmi allows to add further methods to retrieve MIB
information from persistent repositories. In fact, besides the SMIv1/v2 MIB
file parser an additional parser for `SMIng' is included. Both parsers are
built on flex/bison grammar specifications.

SMIng is a research project concerned with the definition of a MIB module
language that is semantically fully compatible with SMIv2 but avoids many
problems of the ASN.1 based SMI versions.

Included with the library, there are three tools that make use of libsmi:
Smiquery allows simple queries of single MIB module items.  Smilint allows
to increase the verbosity of the parser(s), so that MIB modules can be
checked for syntax and semantic errors. Finally, smidump can be used to dump
MIB modules. Currently, SMIng and SMIv2 are supported as output formats, so
that SMIv2 <-> SMIng conversions are possible.

%package devel
Summary:	Header files and development documentation for libsmi
Summary(pl):	Pliki nag³ówkowe i dokumentacja do libsmi
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libsmi.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do libsmi.

%package static
Summary:	Static libsmi libraries
Summary(pl):	Biblioteki statyczne libsmi
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libsmi libraries.

%description -l pl static
Biblioteki statyczne libsmi.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-smi \
	--enable-sming \
	--enable-shared \
	--enable-static \
	--with-mibdir=%{_datadir}/mibs

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT/%{_mandir}/man?/* \
	COPYING ChangeLog README THANKS TODO \
	doc/{SMI.ps,draft-irtf-nmrg-sming-00.txt}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/mibs
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc *.gz doc/{SMI.ps,draft-irtf-nmrg-sming-00.txt}.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a

%changelog
