Summary:	Computer chess program
Summary(de):	Computerschachprogramm
Summary(fr):	Jeu d'échecs
Summary(pl):	Gra w szachy
Summary(tr):	Bilgisayar satranç oyunu
Name:		gnuchess
Version:	4.0.pl80
Release:	6
License:	GPL
Group:		Games
Group(pl):	Gry
Source0:	ftp://prep.ai.mit.edu/pub/gnu/gnuchess/%{name}-%{version}.tar.gz
Source1:	xchess.png
Source2:	gnuchess.desktop
Patch0:		gnuchess-fhs.patch
Patch1:		gnuchess-ncurses.patch
Icon:		xchess.xpm
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	chessprogram

%description
The gnuchess package contains the GNU chess program. By default,
GNUchess uses a curses text-based interface. Alternatively, GNUchess
can be used in conjunction with the xboard user interface and the X
Window System for a graphical chessboard.

%description -l de
Das berühmte GNU-Schachprogramm. Es ist textorientiert, kann aber mit
'xboard' verwendet werden, um X-orientiertes Schach zu spielen.

%description -l fr
Le fameux programme de jeu d'échecs de GNU. Il est en mode texte mais
peut être utilisé avec xboard pour y jouer sous X.

%description -l pl
Oto s³awny GNU program szachowy. Jest w trybie tekstowym, ale w
po³±czeniu z xboard mo¿e mieæ interfejs w X Window.

%description -l tr
Bu ünlü GNU satranç programýdýr. Metin ekranda çalýþýr ama xboard
programý ile birlikte kullanýlarak X altýnda da oynanabilir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cd src
rm -f config.status config.cache
LDFLAGS="-s"; export LDFLAGS
%configure
%{__make} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/gnuchess,%{_mandir}/man6} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Games,/usr/X11R6/share/pixmaps}

cd src
%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix}

install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/pixmaps
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Games

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man6/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Games/*
/usr/X11R6/share/pixmaps/*
%{_datadir}/games/gnuchess
%{_mandir}/man6/*
