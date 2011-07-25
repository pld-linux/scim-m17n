Summary:	SCIM IMEngine for m17n-lib
Name:		scim-m17n
Version:	0.2.3
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/scim/%{name}-%{version}.tar.gz
# Source0-md5:	179a009b262e0aa0aba786f37e4345ed
Patch1:		%{name}-no-M17N-prefix.patch
URL:		http://www.scim-im.org/projects/imengines
BuildRequires:	m17n-lib-devel
BuildRequires:	scim-devel
Requires:	scim >= 1.4.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
scim-m17n provides a SCIM IMEngine for m17n-lib, which allows input of
many languages using the input table maps from m17n-db.

%prep
%setup -q
%patch1 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README THANKS
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/m17n.so
%{_datadir}/scim/icons/*
