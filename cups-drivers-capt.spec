%define rname capt

Summary:	CAPT driver for Canon LBP-810 and LBP-1120
Name:		cups-drivers-%{rname}
Version:	0.1
Release:	%mkrel 4
License:	GPL
Group:		System/Printing
URL:		http://www.boichat.ch/nicolas/capt/
Source0:	http://www.boichat.ch/nicolas/capt/%{rname}-%{version}.tar.bz2
Requires:	cups
Conflicts:	cups-drivers = 2007
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007

%description
CAPT driver for Canon LBP-810 and LBP-1120

This package contains CUPS drivers (PPD) for the following printers:

 o Canon-LBP-810
 o Canon-LBP-1120

%prep

%setup -q -n %{rname}-%{version}

%build

%make CFLAGS="%{optflags}"

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
