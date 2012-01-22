%define upstream_name	 Crypt-DSA
%define upstream_version 1.17

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3
Summary:    DSA Signatures and Key Generation
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%upstream_name/
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  perl(Convert::PEM)
BuildRequires:  perl(Crypt::DES_EDE3)
BuildRequires:  perl(Crypt::Random)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:	perl(Data::Buffer) >= 0.01
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Which) >= 0.05
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Math::BigInt) >= 1.78
BuildRequires:	perl(Perl::MinimumVersion) >= 1.20
BuildRequires:	perl(Test::CPAN::Meta) >= 0.12
BuildRequires:	perl(Test::More) >= 0.42
BuildRequires:	perl(Test::MinimumVersion) >= 0.008
BuildRequires:	perl(Test::Pod) >= 1.26
BuildRequires:	openssl
# Crypt::DSA::Keychain calls openssl for DSA parameter generation
Requires:	openssl
# Pull in Math::BigInt::GMP for GMP support for suitably recent versions of Math::BigInt
# else use Math::GMP
%if %(%{__perl} -MMath::BigInt -e 'use Math::BigInt 1.87;' 2>/dev/null && echo 1 || echo 0)
BuildRequires:	perl(Math::BigInt::GMP)
Requires:	perl(Math::BigInt::GMP)
%else
BuildRequires:	perl(Math::GMP)
Requires:	perl(Math::GMP)
%endif
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Crypt::DSA is an implementation of the DSA (Digital Signature Algorithm)
signature verification system. The implementation itself is pure Perl, although
the heavy-duty mathematics underneath are provided by the Math::Pari library.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test AUTOMATED_TESTING=1

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
