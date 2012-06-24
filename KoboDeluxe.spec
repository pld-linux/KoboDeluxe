# $Revision: 1.2 $, $Dat: 2003/08/04 19:06:42 $
Summary:	A third person scrolling 2D shooter
Summary(pl):	Prosta strzelanka 2D
Name:		KoboDeluxe
Version:	0.4
%define	_pre	pre8
Release:	0.%{_pre}.1
Epoch:		1
License:	GPL, partially LGPL
Group:		Aplications/Games
Source0:	http://olofson.net/kobodl/download/%{name}-%{version}%{_pre}.tar.gz
# Source0-md5:	215fba14e30755940833dc1abb322bd6
Patch0:		kobousr2var.patch
URL:		http://olofson.net/kobodl/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kobo Deluxe is a 3'rd person scrolling 2D shooter with a simple and
responsive control system - which you'll need to tackle the tons of
enemy ships that shoot at you, chase you, circle around you shooting,
or even launch other ships at you, while you're trying to destroy the
labyrinth shaped bases.  There are 50 action packed levels with
smoothly increasing difficulty, and different combinations of enemies
that require different tactics to be dealt with successfully.


%description -l pl
Kobo Deluxe jest gr� 2D typu 3'rd person perspective z prostym
systemem sterowania. W grze tej twoim zadaniem jest pokonanie masy
atakuj�cych ci� nieprzyjacielskich statk�w, kt�re do ciebie strzelaj�,
otaczaj� ci� czy wr�cz nasy�aj� na ciebie inne statki, kiedy ty
starasz si� zniszczy� bazy w kszta�cie labiryntu. Czekana ciebie 50
etap�w pe�nych wartkiej akcji, ze stopniowo zwi�kszaj�cym si� stopniem
trudno�ci i r�nymi typami nieprzyjaci� do kt�rych pokonania
potrzebujesz r�nych taktyk.


%prep
%setup -q -n %{name}-%{version}%{_pre}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog COPYING COPYING.LIB README README.jp README.sfont README.xkobo README.xkobo.jp TODO
%attr(2755,root,games) %{_bindir}/kobodl
%dir /var/games/kobo-deluxe
%dir %attr(775,root,games) /var/games/kobo-deluxe/scores
%{_prefix}/share/games/kobo-deluxe
