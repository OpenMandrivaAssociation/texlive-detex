# revision 33736
# category TLCore
# catalog-ctan /support/detex
# catalog-date 2012-05-07 22:13:48 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-detex
Version:	20120507
Release:	9
Summary:	Strip TeX from a source file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/detex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/detex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/detex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-detex.bin

%description
Detex is a program to remove TeX constructs from a text file.
It recognizes the \input command. The program assumes it is
dealing with LaTeX input if it sees the string \begin{document}
in the text. In this case, it also recognizes the \include and
\includeonly commands.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/detex.1*
%doc %{_texmfdistdir}/doc/man/man1/detex.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
