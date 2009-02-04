%define module  Email-MessageID
%define name    perl-%{module}
%define up_version 1.401
%define version %perl_convert_version %{up_version}
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Generate world unique message-ids
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{up_version}.tar.gz
BuildRequires:  perl(Email::Address)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Message-ids are optional, but highly recommended, headers that identify a
message uniquely. This software generates a unique message-id.

%prep
%setup -q -n %{module}-%{up_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

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

