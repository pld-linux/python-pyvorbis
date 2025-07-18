%define		module	pyvorbis
Summary:	A Python module for the the Ogg/Vorbis library
Summary(pl.UTF-8):	Moduł Pythona do biblioteki Ogg/Vorbis
Name:		python-%{module}
Version:	1.4
Release:	9
License:	GPL
Group:		Libraries/Python
Source0:	http://ekyo.nerim.net/software/pyogg/%{module}-%{version}.tar.gz
# Source0-md5:	b4921e792c0a74f75b9d3057df10ee7c
Patch0:		pyvorbis-double_free.patch
URL:		http://ekyo.nerim.net/software/pyogg/
BuildRequires:	libvorbis-devel
BuildRequires:	python-devel
BuildRequires:	python-pyogg-devel
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-pyogg
Obsoletes:	pyvorbis
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyvorbis is a wrapper for libvorbis, a compressed audio format
library.

%description -l pl.UTF-8
pyvorbis jest wrapperem dla libvorbis - biblioteki obsługującej dźwięk
w formacie skompresowanym.

%package devel
Summary:	pyvorbis headers and example programs
Summary(pl.UTF-8):	Pliki nagłówkowe modułu pyvorbis
Group:		Development/Languages/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}
%pyrequires_eq	python-devel
Requires:	libvorbis-devel
Obsoletes:	pyvorbis-devel

%description devel
pyvorbis is a wrapper for libvorbis, a compressed audio format
library. This package contains the header files and example programs
for pyvorbis module.

%description devel -l pl.UTF-8
pyvorbis jest wrapperem dla libvorbis - biblioteki obsługującej dźwięk
w formacie skompresowanym. Ten pakiet zawiera pliki nagłówkowe i
programy przykładowe dla moduły pyvorbis.

%prep
%setup -q -n %{module}-%{version}
%patch -P0 -p1

%build
%{__python} config_unix.py \
	---prefix %{_prefix}
%{__python} setup.py config
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_incdir}/%{module}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_install

install src/*.h $RPM_BUILD_ROOT%{py_incdir}/%{module}
chmod -x test/*
install test/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{py_sitedir}/ogg/vorbis.so
%if "%{py_ver}" >= "2.5"
%{py_sitedir}/pyvorbis-%{version}-py*.egg-info
%endif
%{_examplesdir}/%{name}-%{version}

%files devel
%defattr(644,root,root,755)
%{py_incdir}/%{module}
