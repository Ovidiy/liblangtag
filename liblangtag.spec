#
# Conditional build:
%bcond_without	static_libs	# static library build
%bcond_without	introspection	# GObject interface
%bcond_without	tests		# "make check" call
#
Summary:	An interface library to access tags for identifying languages
Summary(pl.UTF-8):	Biblioteka interfejsu dostępu do znaczników identyfikujących języki
Name:		liblangtag
Version:	0.5.2
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://bitbucket.org/tagoh/liblangtag/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	34de44f61c5ba308796c14a5b4ca572c
URL:		http://tagoh.bitbucket.org/liblangtag/
%{?with_tests:BuildRequires:	check-devel >= 0.9.4}
%{?with_introspection:BuildRequires:	glib2-devel >= 2.0}
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libxml2-devel >= 2.1.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
liblangtag is an interface library to access tags for identifying
languages.

Features:
- several subtag registry database supports:
  - language
  - extlang
  - script
  - region
  - variant
  - extension
  - grandfathered
  - redundant
- handling of the language tags
  - parser
  - matching
  - canonicalizing

%description -l pl.UTF-8
liblangtag to biblioteka interfejsu dostępu do znaczników
identyfikujących języki.

Możliwości:
- baza danych rejestru podznaczników obsługująca:
  - język
  - extlang
  - pismo
  - region
  - wariant
  - rozszerzenie
  - dziedziczenie
  - nadmiarowość
- obsługa znaczników języków:
  - analiza
  - dopasowywanie
  - sprowadzanie do postaci kanonicznej

%package devel
Summary:	Development files for liblangtag
Summary(pl.UTF-8):	Pliki programistyczne biblioteki liblangtag
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0

%description devel
This package contains the header files for developing applications
that use liblangtag.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
wykorzystujących bibliotekę liblangtag.

%package static
Summary:	Static liblangtag library
Summary(pl.UTF-8):	Statyczna biblioteka liblangtag
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liblangtag library.

%description static -l pl.UTF-8
Statyczna biblioteka liblangtag.

%package gobject
Summary:	GObject based interface to liblangtag
Summary(pl.UTF-8):	Interfejs GObject do biblioteki liblangtag
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gobject
GObject based interface to liblangtag.

%description gobject -l pl.UTF-8
Interfejs GObject do biblioteki liblangtag.

%package gobject-devel
Summary:	Header files for liblangtag-gobject library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki liblangtag-gobject
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gobject = %{version}-%{release}
Requires:	glib2-devel >= 2.0

%description gobject-devel
Header files for liblangtag-gobject library.

%description gobject-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki liblangtag-gobject.

%package gobject-static
Summary:	Static liblangtag-gobject library
Summary(pl.UTF-8):	Statyczna biblioteka liblangtag-gobject
Group:		Development/Libraries
Requires:	%{name}-gobject-devel = %{version}-%{release}

%description gobject-static
Static liblangtag-gobject library.

%description gobject-static -l pl.UTF-8
Statyczna biblioteka liblangtag-gobject.

%prep
%setup -q

%build
%configure \
	%{!?with_introspection:--disable-introspection} \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	%{!?with_tests:--disable-test} \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la
%{?with_static_libs:%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/*.a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gobject -p /sbin/ldconfig
%postun	gobject -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/liblangtag.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblangtag.so.1
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/liblangtag-ext-ldml-t.so
%attr(755,root,root) %{_libdir}/%{name}/liblangtag-ext-ldml-u.so
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root)  %{_libdir}/liblangtag.so
%dir %{_includedir}/liblangtag
%{_includedir}/liblangtag/langtag.h
%{_includedir}/liblangtag/lt-database.h
%{_includedir}/liblangtag/lt-error.h
%{_includedir}/liblangtag/lt-ext-module.h
%{_includedir}/liblangtag/lt-ext-module-data.h
%{_includedir}/liblangtag/lt-extension.h
%{_includedir}/liblangtag/lt-extlang-db.h
%{_includedir}/liblangtag/lt-extlang.h
%{_includedir}/liblangtag/lt-grandfathered.h
%{_includedir}/liblangtag/lt-grandfathered-db.h
%{_includedir}/liblangtag/lt-iter.h
%{_includedir}/liblangtag/lt-lang.h
%{_includedir}/liblangtag/lt-lang-db.h
%{_includedir}/liblangtag/lt-list.h
%{_includedir}/liblangtag/lt-macros.h
%{_includedir}/liblangtag/lt-redundant.h
%{_includedir}/liblangtag/lt-redundant-db.h
%{_includedir}/liblangtag/lt-region.h
%{_includedir}/liblangtag/lt-region-db.h
%{_includedir}/liblangtag/lt-script.h
%{_includedir}/liblangtag/lt-script-db.h
%{_includedir}/liblangtag/lt-string.h
%{_includedir}/liblangtag/lt-tag.h
%{_includedir}/liblangtag/lt-variant.h
%{_includedir}/liblangtag/lt-variant-db.h
%{_pkgconfigdir}/liblangtag.pc
%{_gtkdocdir}/liblangtag

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/liblangtag.a
%endif

%if %{with introspection}
%files gobject
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblangtag-gobject.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblangtag-gobject.so.0
%{_libdir}/girepository-1.0/LangTag-0.5.typelib

%files gobject-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblangtag-gobject.so
%{_includedir}/liblangtag/lt-gobject.h
%{_datadir}/gir-1.0/LangTag-0.5.gir
%{_pkgconfigdir}/liblangtag-gobject.pc

%if %{with static_libs}
%files gobject-static
%defattr(644,root,root,755)
%{_libdir}/liblangtag-gobject.a
%endif
%endif
