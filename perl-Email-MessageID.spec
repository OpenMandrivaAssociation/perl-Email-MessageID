%define module  Email-MessageID
%define name    perl-%{module}
%define version 1.351
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Generate world unique message-ids
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl-Email-Address
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Message-ids are optional, but highly recommended, headers that identify a
message uniquely. This software generates a unique message-id.

%prep
%setup -q -n %{module}-%{version} 

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

