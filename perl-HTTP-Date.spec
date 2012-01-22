%define upstream_name    HTTP-Date
%define upstream_version 6.00

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    5

Summary:    Date conversion for HTTP date formats
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Time::Local)
Conflicts:	perl-libwww-perl < 6
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides functions that deal the date formats used by the HTTP
protocol (and then some more). Only the first two functions, time2str() and
str2time(), are exported by default.

* time2str( [$time] )

  The time2str() function converts a machine time (seconds since epoch) to
  a string. If the function is called without an argument or with an
  undefined argument, it will use the current time.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*
