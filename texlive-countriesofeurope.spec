%global tl_name countriesofeurope
%global tl_revision 79618
%global tl_version 0.23

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	A font with the images of the countries of Europe
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/countriesofeurope
License:	ofl lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/countriesofeurope.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/countriesofeurope.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The bundle provides a font "CountriesOfEurope" (in Adobe Type 1 format)
and the necessary metrics, together with LaTeX macros for its use. The
font provides glyphs with a filled outline of the shape of each country;
each glyph is at the same cartographic scale.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from countriesofeurope:
Map countriesofeurope.map
TL_DROPIN_EOF
