Summary:	SCIM IMEngine for m17n-lib
Summary(pl.UTF-8):	Silnik IM SCIM dla biblioteki m17n-lib
Name:		scim-m17n
Version:	0.2.3
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/scim/%{name}-%{version}.tar.gz
# Source0-md5:	179a009b262e0aa0aba786f37e4345ed
Patch1:		%{name}-no-M17N-prefix.patch
URL:		http://www.scim-im.org/projects/imengines
BuildRequires:	libstdc++-devel
BuildRequires:	m17n-lib-devel >= 1.2.0
BuildRequires:	scim-devel >= 1.4.4
Requires:	scim >= 1.4.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
scim-m17n provides a SCIM IMEngine for m17n-lib, which allows input of
many languages using the input table maps from m17n-db.

%description -l pl.UTF-8
scim-m17n udostępnia silnik IM SCIM dla bibloteki m17n-lib,
umożliwiającej wprowadzanie znaków z wielu języków przy użyciu map
tablic wejściowych z bazy m17n-db.

%prep
%setup -q
%patch -P1 -p1

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README THANKS
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/m17n.so
%{_datadir}/scim/icons/scim-m17n.png
