#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cmrt
Version  : 1.0.5
Release  : 1
URL      : https://github.com/01org/cmrt/archive/1.0.5.tar.gz
Source0  : https://github.com/01org/cmrt/archive/1.0.5.tar.gz
Summary  : C++ Language example delivered by Development Assistant Tool
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ GPL-3.0+
Requires: cmrt-lib
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libva)

%description
This is sample spec file created on the base of c++ binary packages
It is a part of Development Assistant Tool

%package dev
Summary: dev components for the cmrt package.
Group: Development
Requires: cmrt-lib
Provides: cmrt-devel

%description dev
dev components for the cmrt package.


%package lib
Summary: lib components for the cmrt package.
Group: Libraries

%description lib
lib components for the cmrt package.


%prep
%setup -q -n cmrt-1.0.5

%build
export LANG=C
%autogen --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
