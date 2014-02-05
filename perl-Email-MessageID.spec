%define upstream_name    Email-MessageID
%define upstream_version 1.404

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Generate world unique message-ids
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Email/Email-MessageID-%{upstream_version}.tar.gz

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

%changelog
* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 1.402.0-1mdv2011.0
+ Revision: 553964
- update to 1.402

* Wed May 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.401.0-2mdv2010.0
+ Revision: 378110
- fix dependencies

* Wed Feb 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.401.0-1mdv2010.0
+ Revision: 337635
- new version
- standardized version

* Thu Dec 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.400-1mdv2009.1
+ Revision: 315965
- new version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.351-3mdv2009.0
+ Revision: 268464
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.351-2mdv2009.0
+ Revision: 210954
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri May 04 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.351-1mdv2008.0
+ Revision: 22445
- New version


* Mon Jul 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.35-1mdv2007.0
- new version

* Mon Mar 06 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.31-1mdk
- first mdk release


