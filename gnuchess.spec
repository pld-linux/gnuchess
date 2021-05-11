Summary:	Computer chess program
Summary(de.UTF-8):	Computerschachprogramm
Summary(es.UTF-8):	Juego de ajedrez de la GNU
Summary(fr.UTF-8):	Jeu d'échecs
Summary(pl.UTF-8):	Gra w szachy
Summary(pt_BR.UTF-8):	Jogo de xadrez da GNU
Summary(ru.UTF-8):	Шахматная программа GNU
Summary(tr.UTF-8):	Bilgisayar satranç oyunu
Summary(uk.UTF-8):	Шахова програма GNU
Name:		gnuchess
Version:	6.2.8
Release:	1
License:	GPL v3+
Group:		Applications/Games
Source0:	https://ftp.gnu.org/gnu/chess/%{name}-%{version}.tar.gz
# Source0-md5:	f66e10f6596915fbc9695b6e1d622e5c
Source1:	xchess.png
Source2:	%{name}.desktop
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/chess/chess.html
BuildRequires:	flex
BuildRequires:	gettext-tools >= 0.18.3
BuildRequires:	help2man
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
BuildRequires:	texinfo
Provides:	chess_backend
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gnuchess package contains the GNU chess program. By default,
GNUchess uses a curses text-based interface. Alternatively, GNUchess
can be used in conjunction with the xboard user interface and the X
Window System for a graphical chessboard.

%description -l de.UTF-8
Das berühmte GNU-Schachprogramm. Es ist textorientiert, kann aber mit
'xboard' verwendet werden, um X-orientiertes Schach zu spielen.

%description -l es.UTF-8
Este es el famoso programa de ajedrez de GNU. Está basado en texto,
pero puede ser usado en conjunción con xboard para jugar ajedrez
basado en X.

%description -l fr.UTF-8
Le fameux programme de jeu d'échecs de GNU. Il est en mode texte mais
peut être utilisé avec xboard pour y jouer sous X.

%description -l pl.UTF-8
Oto sławny GNU program szachowy. Domyślnie ma interfejs tekstowy
(curses), ale w połączeniu z xboard może mieć graficzny interfejs
X Window.

%description -l pt_BR.UTF-8
Este é o famoso programa de xadrez da GNU. É baseado em texto, mas
pode ser usado em conjunção com xboard para jogar xadrez baseado em X.

%description -l ru.UTF-8
Пакет gnuchess содержит шахматную программу GNU. По умолчанию GNUchess
использует текстовый интерфейс на основе curses. Альтернативно она
может использоваться в сочетании с xboard, обеспечивающим графический
интерфейс под X Window System.

%description -l tr.UTF-8
Bu ünlü GNU satranç programıdır. Metin ekranda çalışır ama xboard
programı ile birlikte kullanılarak X altında da oynanabilir.

%description -l uk.UTF-8
Пакет gnuchess містить шахову програму GNU. За умовчанням GNUchess
використовує текстовий інтерфейс на основі curses. Альтернативно вона
може використовуватись у парі з програмою xboard, яка забезпечує
графічний інтерфейс під X Window System.

%package -n xboard-gnuchess
Summary:	GNU Chess engine integration for Xboard
Summary(pl.UTF-8):	Integracja silnika szachowego GNU Chess z Xboard
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}
Requires:	xboard >= 4.6.0

%description -n xboard-gnuchess
GNU Chess engine integration for Xboard.

%description -n xboard-gnuchess -l pl.UTF-8
Integracja silnika szachowego GNU Chess z Xboard.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gnuchess
%attr(755,root,root) %{_bindir}/gnuchessu
%{_datadir}/gnuchess
%{_desktopdir}/gnuchess.desktop
%{_pixmapsdir}/xchess.png
%{_mandir}/man1/gnuchess.1*
%{_infodir}/gnuchess.info*

%files -n xboard-gnuchess
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnuchessx
%{_datadir}/games/plugins/logos/gnuchess.png
%{_datadir}/games/plugins/xboard/gnuchess.eng
