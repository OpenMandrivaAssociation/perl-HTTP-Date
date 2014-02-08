%define upstream_name    HTTP-Date
%define upstream_version 6.00

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    8

Summary:    Date conversion for HTTP date formats
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Time::Local)
BuildRequires: perl-devel
Conflicts:	perl-libwww-perl < 6
BuildArch: noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-5
+ Revision: 765356
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-4
+ Revision: 763864
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-3
+ Revision: 763071
- rebuild

* Thu May 05 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 6.0.0-2
+ Revision: 669498
- add conflicts on older perl-libwww-perl version to fix upgrades

* Tue May 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.0.0-1
+ Revision: 664976
- import perl-HTTP-Date

