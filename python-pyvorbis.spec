%include        /usr/lib/rpm/macros.python
%define		module pyvorbis
Summary:	A Python module for the the Ogg/Vorbis library
Summary(pl):	Modu³ pythona do biblioteki Ogg/Vorbis
Name:		python-%{module}
Version:	1.2
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.andrewchatham.com/pyogg/download/%{module}-%{version}.tar.gz
URL:		http://www.andrewchatham.com/pyogg/
BuildRequires:	libvorbis-devel
BuildRequires:	python-devel
BuildRequires:	python-pyogg-devel
BuildRequires:	rpm-pythonprov
Requires:	python-modules
Requires:	python-pyogg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	pyvorbis

%description
pyvorbis is a wrapper for libvorbis, a compressed audio format
library.

%description -l pl
pyvorbis jest wrapperem dla libvorbis - biblioteki obs³uguj±cej d¼wiêk
w formacie skompresowanym.

%package devel
Summary:	pyvorbis headers and example programs
Summary(pl):	Pliki nag³ówkowe i programy przyk³adowe dla modu³u pyvorbis
Group:		Development/Languages/Python
Requires:	%{name} = %{version}
Obsoletes:	pyvorbis-devel

%description devel
pyvorbis is a wrapper for libvorbis, a compressed audio format
library. This package contains the header files and example programs
for pyvorbis module.

%description devel -l pl
pyvorbis jest wrapperem dla libvorbis - biblioteki obs³uguj±cej d¼wiêk
w formacie skompresowanym. Ten pakiet zawiera pliki nag³ówkowe i
programy przyk³adowe dla modu³y pyvorbis.

%prep
%setup -q -n %{module}-%{version}

%build
python config_unix.py \
	---prefix %{_prefix}
python setup.py config
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_incdir}/%{module}
python setup.py install --root $RPM_BUILD_ROOT

install src/*.h $RPM_BUILD_ROOT%{py_incdir}/%{module}
chmod -x test/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{py_sitedir}/ogg/*.so

%files devel
%defattr(644,root,root,755)
%doc test/*
%{py_incdir}/%{module}
