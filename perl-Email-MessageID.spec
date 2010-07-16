%define upstream_name    Email-MessageID
%define upstream_version 1.402

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:        Generate world unique message-ids
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Email::Address)

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

Requires:       perl(Email::Address)

%description
Message-ids are optional, but highly recommended, headers that identify a
message uniquely. This software generates a unique message-id.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*
