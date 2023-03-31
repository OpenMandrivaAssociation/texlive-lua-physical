Name:		texlive-lua-physical
Version:	59138
Release:	2
Summary:	Functions and objects for the computation of physical quantities
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lua-physical
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-physical.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-physical.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a pure Lua library, which provides functions and
objects for the computation of physical quantities. The package
provides units of the SI and the imperial system. In order to
display the numbers with measurement uncertainties, the package
is able to perform Gaussian error propagation.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/scripts/lua-physical
%doc %{_texmfdistdir}/doc/lualatex/lua-physical

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
