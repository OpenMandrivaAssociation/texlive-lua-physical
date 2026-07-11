%global tl_name lua-physical
%global tl_revision 59138

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.5
Release:	%{tl_revision}.1
Summary:	Functions and objects for the computation of physical quantities
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/lua-physical
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-physical.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lua-physical.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a pure Lua library, which provides functions and objects for the
computation of physical quantities. The package provides units of the SI
and the imperial system. In order to display the numbers with
measurement uncertainties, the package is able to perform Gaussian error
propagation.

