%define	upstream_name	 Filesys-Statvfs
%define	upstream_version 0.82

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Interface between Perl and the statvfs() system call
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Filesys/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel

Obsoletes:	perl-Filesys-Statvfs_Statfs_Df <= 0.79
Provides:	perl-Filesys-Statvfs_Statfs_Df = %{version}-%{release}

%description
Filesys::Statvfs provides an interface between
Perl and the statvfs() system call.

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
%{_mandir}/*/*
%{perl_vendorlib}/*/Filesys
%{perl_vendorlib}/*/auto/Filesys

%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.820.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.820.0-3mdv2011.0
+ Revision: 555271
- rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.820.0-2mdv2010.1
+ Revision: 504722
- renaming spec file to match pkg name

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.820.0-1mdv2010.0
+ Revision: 395155
- renamed package to match its new upstream name
- update to 0.82
- using %%perl_convert_version
- fixed license field
- renamed to perl-Filesys-Statvfs since upstream package has been
  splitted in 2, will introduce perl-Filesys-Df later on

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.79-5mdv2009.0
+ Revision: 257027
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.79-3mdv2008.1
+ Revision: 151382
- rebuild for perl-5.10.0

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 0.79-2mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

