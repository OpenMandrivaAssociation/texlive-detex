%global tl_name detex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Strip TeX from a source file
Group:		Publishing
URL:		https://www.ctan.org/pkg/detex
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/detex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/detex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(detex.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Detex is a program to remove TeX constructs from a text file. It
recognizes the \input command. The program assumes it is dealing with
LaTeX input if it sees the string \begin{document} in the text. In this
case, it also recognizes the \include and \includeonly commands. The
author now considers this program to be "retired" and Piotr Kubowicz's
OpenDetex as its successor.

