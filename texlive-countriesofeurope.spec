Name:		texlive-countriesofeurope
Version:	54512
Release:	2
Summary:	A font with the images of the countries of Europe
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/countriesofeurope
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/countriesofeurope.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/countriesofeurope.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides a font "CountriesOfEurope" (in Adobe Type 1
format) and the necessary metrics, together with LaTeX macros
for its use. The font provides glyphs with a filled outline of
the shape of each country; each glyph is at the same
cartographic scale.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/countriesofeurope
%{_texmfdistdir}/fonts/enc/dvips/countriesofeurope
%{_texmfdistdir}/fonts/map/dvips/countriesofeurope
%{_texmfdistdir}/fonts/tfm/public/countriesofeurope
%{_texmfdistdir}/fonts/type1/public/countriesofeurope
%{_texmfdistdir}/fonts/opentype/public/countriesofeurope
%{_texmfdistdir}/tex/latex/countriesofeurope
%doc %{_texmfdistdir}/doc/fonts/countriesofeurope

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
