%define		_decoration 	k3dnomore
Summary:	Kwin decoration - %{_decoration}
Summary(pl):	Dekoracja kwin - %{_decoration}
Name:		kde-decoration-%{_decoration}
Version:	0.6
Release:	1
License:	GPL
Group:		Themes/Gtk
Source0:	%{_decoration}-%{version}.tar.gz
URL:		http://www.kde-look.org/content/show.php?content=4213
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	qt-devel >= 3.0.5
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

%description
%{_decoration} is one of more creative kwin decorations found on kde-look, 
includes configuration module for kcontrol.

%description -l pl
%{_decoration} to jedna z najbardziej kreatywnych dekoracji kwin, jakie
mo�na znale�� na kde-look. Zawiera modu� konfiguracyjny dla kcontrol.

%prep
%setup -q -n %{_decoration}-%{version}

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT


%post
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_datadir}/apps/kwin/*
