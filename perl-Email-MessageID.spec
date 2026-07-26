%define upstream_name    Email-MessageID
Name:		perl-%{upstream_name}
Version:	1.408
Release:	2

Summary:	Generate world unique message-ids

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/rjbs/Email-MessageID
Source0:	https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-MessageID-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Email::Address)

BuildArch:	noarch

Requires:	perl(Email::Address)

%description
Message-ids are optional, but highly recommended, headers that identify a
message uniquely. This software generates a unique message-id.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*


