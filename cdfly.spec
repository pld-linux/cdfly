Summary:	CdFly is a crossplatform CD collection manager
Summary(hu.UTF-8):	CdFly egy többplatformos CD gyűjteménykezelő
Name:		cdfly
Version:	0.3
Release:	0.1
License:	check first
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/cdfly/%{name}-%{version}.zip
# Source0-md5:	d460a16d8d2563f419c7d81a176acfec
URL:		http://cdfly.sourceforge.net
BuildRequires:	QtCore-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	QtSql-sqlite3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CdFly is a crossplatform CD collection manager.

%description -l hu.UTF-8
CdFly egy többplatformos CD gyűjteménykezelő.

%prep
%setup -q -n %{name}

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install cdfly $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
