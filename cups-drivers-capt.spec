%define rname capt

Summary:	CAPT driver for Canon LBP-810 and LBP-1120
Name:		cups-drivers-%{rname}
Version:	0.1
Release:	%mkrel 11
License:	GPL
Group:		System/Printing
URL:		http://www.boichat.ch/nicolas/capt/
Source0:	http://www.boichat.ch/nicolas/capt/%{rname}-%{version}.tar.bz2
Patch0:		capt-0.1-LDFLAGS.diff
Requires:	cups
Conflicts:	cups-drivers = 2007
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
CAPT driver for Canon LBP-810 and LBP-1120

This package contains CUPS drivers (PPD) for the following printers:

 o Canon-LBP-810
 o Canon-LBP-1120

%prep

%setup -q -n %{rname}-%{version}
%patch0 -p0

%build

%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

# Correct PPD files to pass "cupstestppd"
perl -p -i -e "s/DefaultNoReset/DefaultAlwaysReset/g" ppd/*.ppd

# Do not generate a log file with fixed name, security problem!
perl -p -i -e "s:/tmp/capt.log:/dev/null:g" ppd/*.ppd

# Create PPD file for LBP-1120
cp ppd/Canon-LBP-810-capt.ppd ppd/Canon-LBP-1120-capt.ppd
perl -p -i -e "s:LBP-810:LBP-1120:g" ppd/Canon-LBP-1120-capt.ppd
perl -p -i -e "s:lbp810:lbp1120:g" ppd/Canon-LBP-1120-capt.ppd

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/cups/model/capt

install -m0755 capt %{buildroot}%{_bindir}/
install -m0755 capt-* %{buildroot}%{_bindir}/
install -m0644 ppd/*.ppd %{buildroot}%{_datadir}/cups/model/capt/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc COPYING NEWS README SPECS THANKS TODO
%attr(0755,root,root) %{_bindir}/capt*
%attr(0755,root,root) %dir %{_datadir}/cups/model/capt
%attr(0644,root,root) %{_datadir}/cups/model/capt/Canon-LBP-810-capt.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/capt/Canon-LBP-1120-capt.ppd*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-11mdv2011.0
+ Revision: 663434
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-10mdv2011.0
+ Revision: 603866
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-9mdv2010.1
+ Revision: 518838
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.1-8mdv2010.0
+ Revision: 413282
- rebuild

* Tue Dec 23 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1-7mdv2009.1
+ Revision: 318056
- use %%ldflags

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.1-6mdv2009.0
+ Revision: 220524
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.1-5mdv2008.1
+ Revision: 149144
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1-4mdv2008.0
+ Revision: 75323
- fix deps (pixel)

* Sun Aug 19 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1-3mdv2008.0
+ Revision: 66562
- rebuild
- use the new System/Printing RPM GROUP

* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1-1mdv2008.0
+ Revision: 62495
- Import cups-drivers-capt



* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1-1mdv2008.0
- initial Mandriva package
