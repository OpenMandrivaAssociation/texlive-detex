# revision 26689
# category TLCore
# catalog-ctan /support/detex
# catalog-date 2012-05-07 22:13:48 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-detex
Version:	20120507
Release:	1
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
%doc %{_texmfdir}/doc/man/man1/detex.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120507-1
+ Revision: 812217
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20091109-2
+ Revision: 750887
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20091109-1
+ Revision: 718217
- texlive-detex
- texlive-detex
- texlive-detex
- texlive-detex

