%define		_decoration 	k3dnomore
Summary:	Kwin decoration - %{_decoration}
Summary(pl):	Dekoracja kwin - %{_decoration}
Name:		kde-decoration-%{_decoration}
Version:	0.7
Release:	1
License:	GPL
Group:		Themes
Source0:	%{_decoration}-%{version}.tar.gz
# Source0-md5:	bd46e58a3e9d3b4d6c4f309d0feb539e
URL:		http://www.kde-look.org/content/show.php?content=4213
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	rpmbuild(macros) >= 1.129
BuildConflicts:	kdebase-devel >= 9:3.2.0
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
k3dnomore is one of more creative kwin decorations found on kde-look,
includes configuration module for kcontrol.

%description -l pl
k3dnomore to jedna z najbardziej kreatywnych dekoracji kwin, jakie
mo¿na znale¼æ na kde-look. Zawiera modu³ konfiguracyjny dla kcontrol.

%prep
%setup -q -n %{_decoration}-%{version}

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_datadir}/apps/kwin/*
