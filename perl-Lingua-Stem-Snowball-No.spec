#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Lingua
%define		pnam	Snowball-Norwegian
Summary:	Lingua::Stem::Snowball::No - Porter's stemming algorithm for Norwegian
Summary(pl.UTF-8):	Lingua::Stem::Snowball::No - algorytm Portera określający rdzenie słów dla języka norweskiego
Name:		perl-Lingua-Stem-Snowball-No
Version:	1.2
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	24197e600ea4d9b5bb5ca9c175f14676
URL:		http://search.cpan.org/dist/Lingua-Snowball-Norwegian/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The stem function takes a scalar as a parameter and stems the word
according to Martin Porter's Norwegian stemming algorithm, which can
be found at the Snowball website: <http://snowball.tartarus.org/>.

%description -l pl.UTF-8
Funkcja określająca rdzenie słów pobiera skalarny parametr i korzysta
z algorytmu dla języka norweskiego autorstwa Martina Portera. Algorytm
ten można znaleźć na stronie Snowballa:
<http://snowball.tartarus.org/>.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/stemmer-no.pl
%{perl_vendorlib}/Lingua/Stem/Snowball/*.pm
%{_mandir}/man3/*
