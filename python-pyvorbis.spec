%include        /usr/lib/rpm/macros.python
%define		module pyvorbis
Name:		python-%{module}
Version:	1.2
Release:	1
Summary:	A Python module for the the Ogg/Vorbis library
Summary(pl):	Modu³ pythona do biblioteki Ogg/Vorbis
Group:		Libraries/Python
License:	GPL
URL:		http://www.andrewchatham.com/pyogg/
Source0:	http://www.andrewchatham.com/pyogg/download/%{module}-%{version}.tar.gz
Requires:	python-modules
Requires:	libvorbis
Requires:	python-pyogg
BuildRequires:	python-devel
BuildRequires:	libvorbis-devel
BuildRequires:	python-pyogg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	pyvorbis

%description
pyvorbis is a wrapper for libvorbis, a compressed audio format
library.

%description -l pl
pyvorbis jest wrapperem dla biblioteki libvorbis, formatu
skompresowanego.

%package devel
Summary:	pyvorbis header and example programs
Group:		Development/Languages/Python
Requires:	%{name} = %{version}
Obsolete:	pyvorbis-devel

%description devel
pyvorbis is a wrapper for libvorbis, a compressed audio format
library.

Install python-pyvorbis-devel if you need the API documentation and
example programs.

%description devel -l pl
pyvorbis jest wrapperem dla biblioteki libvorbis, formatu
skompresowanego.

Zainstaluj tê paczkê je¶li potrzebujesz dokumentacjê API oraz
przyk³adowe programy.

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
%dir %{py_sitedir}/ogg
%attr(755,root,root) %{py_sitedir}/ogg/*.so
%doc AUTHORS ChangeLog README NEWS

%files devel
%defattr(644,root,root,755)
%{py_incdir}/%{module}
%doc test/*
