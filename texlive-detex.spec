# revision 23089
# category TLCore
# catalog-ctan /support/detex
# catalog-date 2009-11-09 15:03:08 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-detex
Version:	20091109
Release:	1
Summary:	Strip TeX from a source file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/detex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/detex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/detex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-detex.bin
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Detex is a program to remove TeX constructs from a text file.
It recognizes the \input command. The program assumes it is
dealing with LaTeX input if it sees the string \begin{document}
in the text. In this case, it also recognizes the \include and
\includeonly commands.

#-----------------------------------------------------------------------
%files
%doc %{_mandir}/man1/detex.1*
%doc %{_texmfdir}/doc/man/man1/detex.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
