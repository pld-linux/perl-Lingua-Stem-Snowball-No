#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	Snowball-Norwegian
Summary:	Lingua::Stem::Snowball::No - Porter's stemming algorithm for Norwegian
Summary(pl):	Lingua::Stem::Snowball::No - algorytmu Portera okre�laj�cy rdzenie s��w dla j�zyka norweskiego
Name:		perl-Lingua-Stem-Snowball-No
Version:	1.0
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The stem function takes a scalar as a parameter and stems the word
according to Martin Porter's Norwegian stemming algorithm, which can
be found at the Snowball website: http://snowball.tartarus.org/.

%description -l pl
Funkcja okre�laj�ca rdzenie s��w pobiera skalarny parametr i korzysta
z algorytmu dla j�zyka norweskiego autorstwa Martina Portera.
Algorytm ten mo�na znale�� na stronie Snowballa:
http://snowball.tartarus.org/.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install stemmer.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Lingua/Stem/Snowball/*.pm
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_mandir}/man3/*
