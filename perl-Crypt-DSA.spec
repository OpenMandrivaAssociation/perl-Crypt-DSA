%define upstream_name	 Crypt-DSA
%define upstream_version 1.17

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	DSA Signatures and Key Generation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%upstream_name/
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz
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
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Crypt::DSA is an implementation of the DSA (Digital Signature Algorithm)
signature verification system. The implementation itself is pure Perl, although
the heavy-duty mathematics underneath are provided by the Math::Pari library.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sat Jun 25 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.170.0-1mdv2011.0
+ Revision: 687046
- new version

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.160.0-2
+ Revision: 676614
- sync with perl-Crypt-DSA-1.16-6.fc15.src.rpm
- rebuild

* Mon Sep 14 2009 Jérôme Quelin <jquelin@mandriva.org> 1.160.0-1mdv2010.0
+ Revision: 439607
- adding missing buildrequires:
- update to 1.16

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.0
+ Revision: 406925
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.14-5mdv2009.0
+ Revision: 256260
- rebuild

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-3mdv2008.1
+ Revision: 138076
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jun 07 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-2mdv2007.0
- fix source URL

* Tue May 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2007.0
- New release 0.14
- spec cleanup
- fix directory ownership

* Tue Jun 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.13-1mdk
- 0.13. Slow to test, but works.

* Tue Jun 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.12-4mdk
- spec cleanup (not ready for 0.13 yet)

* Wed Feb 09 2005 Sylvie Terjan <erinmargault@mandrake.org> 0.12-3mdk
- rebuild for new perl

* Tue Nov 11 2003 Michael Scherer <scherer.michael@free.fr> 0.12-2mdk
- BuildRequires ( perl-Crypt-Random, perl-Digest-SHA1 )

* Thu Nov 06 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 0.12-1mdk
- New package

