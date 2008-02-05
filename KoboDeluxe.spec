# $Revision: 1.13 $, $Dat: 2003/08/04 19:06:42 $
Summary:	A third person scrolling 2D shooter
Summary(pl.UTF-8):	Prosta strzelanka 2D
Name:		KoboDeluxe
Version:	0.5.1
Release:	1
Epoch:		1
License:	GPL, partially LGPL
Group:		X11/Applications/Games
#Source0Download: http://olofson.net/kobodl/download.html
Source0:	http://olofson.net/kobodl/download/%{name}-%{version}.tar.bz2
# Source0-md5:	cb5dcdaf07ccad18a921058138dedc4a
Patch0:		kobousr2var.patch
URL:		http://olofson.net/kobodl/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kobo Deluxe is a 3'rd person scrolling 2D shooter with a simple and
responsive control system - which you'll need to tackle the tons of
enemy ships that shoot at you, chase you, circle around you shooting,
or even launch other ships at you, while you're trying to destroy the
labyrinth shaped bases.  There are 50 action packed levels with
smoothly increasing difficulty, and different combinations of enemies
that require different tactics to be dealt with successfully.

%description -l pl.UTF-8
Kobo Deluxe jest grą 2D typu 3'rd person perspective z prostym
systemem sterowania. W grze tej twoim zadaniem jest pokonanie masy
atakujących cię nieprzyjacielskich statków, które do ciebie strzelają,
otaczają cię czy wręcz nasyłają na ciebie inne statki, kiedy ty
starasz się zniszczyć bazy w kształcie labiryntu. Czekana ciebie 50
etapów pełnych wartkiej akcji, ze stopniowo zwiększającym się stopniem
trudności i różnymi typami nieprzyjaciół do których pokonania
potrzebujesz różnych taktyk.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--datadir=%{_datadir}/games/kobo-deluxe
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog COPYING.LIB README README.jp README.sfont README.xkobo README.xkobo.jp TODO
%attr(2755,root,games) %{_bindir}/kobodl
%{_prefix}/share/games/kobo-deluxe
%dir /var/games/kobo-deluxe
%dir %attr(775,root,games) /var/games/kobo-deluxe/scores
%{_mandir}/man6/kobodl.6*
