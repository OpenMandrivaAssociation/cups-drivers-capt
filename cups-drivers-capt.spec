%define rname capt

Summary:	CAPT driver for Canon LBP-810 and LBP-1120
Name:		cups-drivers-%{rname}
Version:	0.1
Release:	20
License:	GPLv2
Group:		System/Printing
Url:		http://www.boichat.ch/nicolas/capt/
Source0:	http://www.boichat.ch/nicolas/capt/%{rname}-%{version}.tar.gz
Patch0:		capt-0.1-LDFLAGS.diff
Requires:	cups

%description
CAPT driver for Canon LBP-810 and LBP-1120

This package contains CUPS drivers (PPD) for the following printers:

 o Canon-LBP-810
 o Canon-LBP-1120

%prep
%setup -qn %{rname}-%{version}
%patch0 -p0

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

# Correct PPD files to pass "cupstestppd"
sed -i -e "s/DefaultNoReset/DefaultAlwaysReset/g" ppd/*.ppd

# Do not generate a log file with fixed name, security problem!
sed -i -e "s:/tmp/capt.log:/dev/null:g" ppd/*.ppd

# Create PPD file for LBP-1120
cp ppd/Canon-LBP-810-capt.ppd ppd/Canon-LBP-1120-capt.ppd
sed -i -e "s:LBP-810:LBP-1120:g" ppd/Canon-LBP-1120-capt.ppd
sed -i -e "s:lbp810:lbp1120:g" ppd/Canon-LBP-1120-capt.ppd

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/cups/model/capt

install -m0755 capt %{buildroot}%{_bindir}/
install -m0755 capt-* %{buildroot}%{_bindir}/
install -m0644 ppd/*.ppd %{buildroot}%{_datadir}/cups/model/capt/

%files
%doc COPYING NEWS README SPECS THANKS TODO
%{_bindir}/capt*
%dir %{_datadir}/cups/model/capt
%{_datadir}/cups/model/capt/Canon-LBP-810-capt.ppd*
%{_datadir}/cups/model/capt/Canon-LBP-1120-capt.ppd*

