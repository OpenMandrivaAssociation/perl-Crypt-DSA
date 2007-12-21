%define module	Crypt-DSA
%define name	perl-%{module}
%define version 0.14
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:        DSA Signatures and Key Generation
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%module/
Source:		http://www.cpan.org/modules/by-module/Cryp:/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(Convert::PEM)
BuildRequires:  perl(Data::Buffer)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(Crypt::Random)
BuildRequires:  perl(Crypt::DES_EDE3)
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Crypt::DSA is an implementation of the DSA (Digital
Signature Algorithm) signature verification system.
The implementation itself is pure Perl, although the
heavy-duty mathematics underneath are provided by the
Math::Pari library.

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
%doc README
%{perl_vendorlib}/Crypt
%{_mandir}/*/*

