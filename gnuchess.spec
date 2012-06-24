Summary:	Computer chess program
Summary(de):	Computerschachprogramm
Summary(es):	Juego de ajedrez de la GNU
Summary(fr):	Jeu d'�checs
Summary(pl):	Gra w szachy
Summary(pt_BR):	Jogo de xadrez da GNU
Summary(ru):	��������� ��������� GNU
Summary(tr):	Bilgisayar satran� oyunu
Summary(uk):	������ �������� GNU
Name:		gnuchess
Version:	5.07
Release:	3
License:	GPL
Group:		Applications/Games
Source0:	ftp://ftp.gnu.org/gnu/chess/%{name}-%{version}.tar.gz
# Source0-md5:	259da00aa559e5624c65279484fccaf7
Source1:	xchess.png
Source2:	%{name}.desktop
URL:		http://www.gnu.org/software/chess/chess.html
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gnuchess package contains the GNU chess program. By default,
GNUchess uses a curses text-based interface. Alternatively, GNUchess
can be used in conjunction with the xboard user interface and the X
Window System for a graphical chessboard.

%description -l de
Das ber�hmte GNU-Schachprogramm. Es ist textorientiert, kann aber mit
'xboard' verwendet werden, um X-orientiertes Schach zu spielen.

%description -l es
Este es el famoso programa de ajedrez de GNU. Est� basado en texto,
pero puede ser usado en conjunci�n con xboard para jugar ajedrez
basado en X.

%description -l fr
Le fameux programme de jeu d'�checs de GNU. Il est en mode texte mais
peut �tre utilis� avec xboard pour y jouer sous X.

%description -l pl
Oto s�awny GNU program szachowy. Jest w trybie tekstowym, ale w
po��czeniu z xboard mo�e mie� interfejs w X Window.

%description -l pt_BR
Este � o famoso programa de xadrez da GNU. � baseado em texto, mas
pode ser usado em conjun��o com xboard para jogar xadrez baseado em X.

%description -l ru
����� gnuchess �������� ��������� ��������� GNU. �� ��������� GNUchess
���������� ��������� ��������� �� ������ curses. ������������� ���
����� �������������� � ��������� � xboard, �������������� �����������
��������� ��� X Window System.

%description -l tr
Bu �nl� GNU satran� program�d�r. Metin ekranda �al���r ama xboard
program� ile birlikte kullan�larak X alt�nda da oynanabilir.

%description -l uk
����� gnuchess ͦ����� ������ �������� GNU. �� ���������� GNUchess
����������դ ��������� ��������� �� ����צ curses. ������������� ����
���� ����������������� � ��Ҧ � ��������� xboard, ��� ��������դ
���Ʀ���� ��������� Ц� X Window System.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/gnuchess,%{_mandir}/man6} \
       $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install src/gnuchess $RPM_BUILD_ROOT%{_bindir}
install src/gnuchessx $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/gnuchess
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/*
