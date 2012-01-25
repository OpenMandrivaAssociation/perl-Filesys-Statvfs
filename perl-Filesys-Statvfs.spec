%define	upstream_name	 Filesys-Statvfs
%define	upstream_version 0.82

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Interface between Perl and the statvfs() system call
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Filesys/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Obsoletes: perl-Filesys-Statvfs_Statfs_Df <= 0.79
Provides:  perl-Filesys-Statvfs_Statfs_Df = %{version}-%{release}

%description
Filesys::Statvfs provides an interface between
Perl and the statvfs() system call.

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
%{_mandir}/*/*
%{perl_vendorlib}/*/Filesys
%{perl_vendorlib}/*/auto/Filesys
