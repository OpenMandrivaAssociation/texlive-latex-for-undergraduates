Name:		texlive-latex-for-undergraduates
Version:	64647
Release:	1
Summary:	A tutorial aimed at introducing undergraduate students to LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/latex-for-undergraduates
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-for-undergraduates.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-for-undergraduates.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A tutorial aimed at introducing undergraduate students to
LaTeX, including an introduction to LaTeX Workshop in Visual
Studio Code and an example package of user-defined LaTeX
commands.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/latex-for-undergraduates

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
