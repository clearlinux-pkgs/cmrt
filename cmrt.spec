#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cmrt
Version  : 1.0.6
Release  : 11
URL      : https://github.com/intel/cmrt/archive/1.0.6.tar.gz
Source0  : https://github.com/intel/cmrt/archive/1.0.6.tar.gz
Summary  : C++ Language example delivered by Development Assistant Tool
Group    : Development/Tools
License  : Distributable GPL-2.0 GPL-2.0+ GPL-3.0+ MIT
Requires: cmrt-lib = %{version}-%{release}
Requires: cmrt-license = %{version}-%{release}
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libva)

%description
This is sample spec file created on the base of c++ binary packages
It is a part of Development Assistant Tool

%package dev
Summary: dev components for the cmrt package.
Group: Development
Requires: cmrt-lib = %{version}-%{release}
Provides: cmrt-devel = %{version}-%{release}

%description dev
dev components for the cmrt package.


%package lib
Summary: lib components for the cmrt package.
Group: Libraries
Requires: cmrt-license = %{version}-%{release}

%description lib
lib components for the cmrt package.


%package license
Summary: license components for the cmrt package.
Group: Default

%description license
license components for the cmrt package.


%prep
%setup -q -n cmrt-1.0.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545590638
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1545590638
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cmrt
cp COPYING %{buildroot}/usr/share/package-licenses/cmrt/COPYING
cp LICENSE %{buildroot}/usr/share/package-licenses/cmrt/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libcmrt.so
/usr/lib64/pkgconfig/libcmrt.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcmrt.so.1
/usr/lib64/libcmrt.so.1.1001.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cmrt/COPYING
/usr/share/package-licenses/cmrt/LICENSE
