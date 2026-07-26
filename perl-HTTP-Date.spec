%define modname	HTTP-Date
Summary:	Date conversion for HTTP date formats
Name:		perl-%{modname}
Version:	6.02
Release:	12
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/HTTP/HTTP-Date-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test)
BuildRequires:	perl(Time::Local)
BuildRequires:	perl-devel
Conflicts:	perl-libwww-perl < 6

%description
This module provides functions that deal the date formats used by the HTTP
protocol (and then some more). Only the first two functions, time2str() and
str2time(), are exported by default.

* time2str( [$time] )

  The time2str() function converts a machine time (seconds since epoch) to
  a string. If the function is called without an argument or with an
  undefined argument, it will use the current time.

%prep
%setup -qn %{modname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{perl_vendorlib}/*
%{_mandir}/man3/*


