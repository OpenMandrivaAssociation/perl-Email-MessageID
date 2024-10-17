%define upstream_name    Email-MessageID
%define upstream_version 1.405

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Generate world unique message-ids

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Email::Address)

BuildArch:	noarch

Requires:	perl(Email::Address)

%description
Message-ids are optional, but highly recommended, headers that identify a
message uniquely. This software generates a unique message-id.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


