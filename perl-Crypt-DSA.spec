%define upstream_name	 Crypt-DSA
%define upstream_version 1.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    DSA Signatures and Key Generation
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%upstream_name/
Source0:	http://www.cpan.org/modules/by-module/Cryp:/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(Convert::PEM)
BuildRequires:  perl(Crypt::DES_EDE3)
BuildRequires:  perl(Crypt::Random)
BuildRequires:  perl(Data::Buffer)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(File::Which)
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Crypt::DSA is an implementation of the DSA (Digital
Signature Algorithm) signature verification system.
The implementation itself is pure Perl, although the
heavy-duty mathematics underneath are provided by the
Math::Pari library.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
