Summary:	Computer chess program
Summary(de):	Computerschachprogramm
Summary(fr):	Jeu d'échecs.
Summary(pl):	Gra w szachy
Summary(tr):	Bilgisayar satranç oyunu
Name:		gnuchess
Version:	4.0.pl80
Release:	1
Copyright:	GPL
Group:		Games
Source:		ftp://prep.ai.mit.edu/pub/gnu/gnuchess/%{name}-%{version}.tar.gz
Patch0:		gnuchess-fhs.patch
Patch1:		gnuchess-ncurses.patch
BuildRequires:	ncurses-devel
BuildRoot:	/tmp/%{name}-%{version}-root

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
LDFLAGS="-s"; export LDFLAGS
%configure
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/gnuchess,%{_mandir}/man6}

cd src
make install prefix=$RPM_BUILD_ROOT%{_prefix} \
	exec_prefix=$RPM_BUILD_ROOT%{_prefix}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man6/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/gnuchess
%{_mandir}/man6/*
