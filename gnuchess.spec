Summary:     Computer chess program
Summary(de): Computerschachprogramm
Summary(fr): Jeu d'échecs.
Summary(pl): Gra w szachy
Summary(tr): Bilgisayar satranç oyunu
Name:        gnuchess
Version:     4.0.pl77
Release:     6
Copyright:   GPL
Group:       Games
Source:      ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:      gnuchess-fsstnd.patch
Patch1:      gnuchess-ncurses.patch
Icon:        xchess.gif
Buildroot:   /tmp/%{name}-%{version}-root

%description
This is the famous GNU chess program.  It is text based, but can be used in
conjunction with xboard to play X based chess.

%description -l de
Das berühmte GNU-Schachprogramm. Es ist textorientiert, kann aber mit
'xboard' verwendet werden, um X-orientiertes Schach zu spielen.

%description -l fr
Le fameux programme de jeu d'échecs de GNU. Il est en mode texte mais peut
être utilisé avec xboard pour y jouer sous X.

%description -l pl
Oto s³awny GNU program szachowy. Jest w trybie tekstowym, ale w po³±czeniu z
xboard mo¿e mieæ interfejs w X Window.

%description -l tr
Bu ünlü GNU satranç programýdýr. Metin ekranda çalýþýr ama xboard programý
ile birlikte kullanýlarak X altýnda da oynanabilir.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cd src
rm -f config.status config.cache
%configure
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{lib/games/gnuchess,bin,man/man6}

cd src
make prefix=$RPM_BUILD_ROOT/usr install
strip $RPM_BUILD_ROOT/usr/bin/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/bin/*
%{_libdir}/games/gnuchess
%{_mandir}/man6/*

%changelog
* Sun Sep 27 1998 Marcin 'Qrczak' Kowalczyk <qrczak@knm.org.pl>
  [4.0.pl77-6]
- use %%{name} and %%{version} macros,
- added %setup -q parameter,
- `mkdir -p' replaced with more standard `install -d',
- simplified %files list and added full %attr description in %files,
- added pl translation,
- simplified install scripts.

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- BuildRoot'ed

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
