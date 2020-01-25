#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Regexp
%define		pnam	Common-net-CIDR
Summary:	Regexp::Common::net::CIDR -- provide patterns for CIDR blocks
Name:		perl-Regexp-Common-net-CIDR
Version:	0.03
Release:	1
License:	GPL version 2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Regexp/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	94305bfe4b296da1cc999f8cb89ae504
URL:		http://search.cpan.org/dist/Regexp-Common-net-CIDR/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Patterns for CIDR blocks. Now only next IPv4 formats are supported:

  xxx.xxx/xx
  xxx.xxx.xxx/xx
  xxx.xxx.xxx.xxx/xx

With {-keep} stores address in $1 and number of bits in $2.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{perl_vendorlib}/Regexp/Common/net
%{perl_vendorlib}/Regexp/Common/net/*.pm
%{_mandir}/man3/*
