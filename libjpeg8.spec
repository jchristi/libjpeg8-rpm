

Summary: A library for manipulating JPEG image format files
Name: libjpeg8
Version: 8d
Release: 3.1
License: IJG
Group: System Environment/Libraries
URL: http://www.ijg.org/
Source0: http://www.ijg.org/files/jpegsrc.v8d.tar.gz
BuildRequires: autoconf libtool
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The libjpeg8 package contains a JPEG library needed for Eagle eCAD 
software package

%package devel
Summary: Development tools for programs which will use the libjpeg library
Group: Development/Libraries
Requires: libjpeg8 = %{version}-%{release}
Conflicts: libjpeg-devel

%description devel
The libjpeg-devel package includes the header files and documentation
necessary for developing programs which will manipulate JPEG files using
the libjpeg library.

If you are going to develop programs which will manipulate JPEG images,
you should install libjpeg-devel.  You'll also need to have the libjpeg
package installed.

%prep
%setup -q -n jpeg-8d


autoconf

%build
%configure --enable-shared --disable-static

make libdir=%{_libdir} %{?_smp_mflags}

LD_LIBRARY_PATH=$PWD:$LD_LIBRARY_PATH make test

%install
rm -rf $RPM_BUILD_ROOT

export QA_RPATHS=$0x0001

%makeinstall

# remove unwanted stuff, .so file is needed
rm -rf $RPM_BUILD_ROOT%{_mandir}
rm $RPM_BUILD_ROOT%{_bindir}/*
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README
%{_libdir}/libjpeg.so.*

%files devel
%defattr(-,root,root)
%doc libjpeg.txt coderules.txt structure.txt wizard.txt example.c
%{_libdir}/*.so
/usr/include/*.h

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Jul 3 2012 Wojciech Kazubski <wk@ire.pw.edu.pl> - 8d-1
- new package based on libjpeg version 6
