Summary:	Computer chess program
Summary(de):	Computerschachprogramm
Summary(fr):	Jeu d'�checs.
Summary(pl):	Gra w szachy
Summary(tr):	Bilgisayar satran� oyunu
Name:		gnuchess
Version:	4.0.pl80
Release:	4
License:	GPL
Group:		Games
Group(pl):	Gry
Source:		ftp://prep.ai.mit.edu/pub/gnu/gnuchess/%{name}-%{version}.tar.gz
Patch0:		gnuchess-fhs.patch
Patch1:		gnuchess-ncurses.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The gnuchess package contains the GNU chess program.  By default, GNUchess
uses a curses text-based interface.  Alternatively, GNUchess can be used in
conjunction with the xboard user interface and the X Window System for a
graphical chessboard.

%description -l de
Das ber�hmte GNU-Schachprogramm. Es ist textorientiert, kann aber mit
'xboard' verwendet werden, um X-orientiertes Schach zu spielen.

%description -l fr
Le fameux programme de jeu d'�checs de GNU. Il est en mode texte mais peut
�tre utilis� avec xboard pour y jouer sous X.

%description -l pl
Oto s�awny GNU program szachowy. Jest w trybie tekstowym, ale w po��czeniu
z xboard mo�e mie� interfejs w X Window.

%description -l tr
Bu �nl� GNU satran� program�d�r. Metin ekranda �al���r ama xboard program�
ile birlikte kullan�larak X alt�nda da oynanabilir.

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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/gnuchess,%{_mandir}/man6}

cd src
make install prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix}

strip $RPM_BUILD_ROOT%{_bindir}/*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man6/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/gnuchess
%{_mandir}/man6/*
