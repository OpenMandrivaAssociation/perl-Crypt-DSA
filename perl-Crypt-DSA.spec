%define modname	Crypt-DSA
%define modver	1.17

Summary:	DSA Signatures and Key Generation
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%modname/
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Convert::PEM)
BuildRequires:	perl(Crypt::DES_EDE3)
BuildRequires:	perl(Crypt::Random)
BuildRequires:	perl(Digest::SHA1)
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

%description
Crypt::DSA is an implementation of the DSA (Digital Signature Algorithm)
signature verification system. The implementation itself is pure Perl, although
the heavy-duty mathematics underneath are provided by the Math::Pari library.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test AUTOMATED_TESTING=1

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Crypt
%{_mandir}/man3/*

