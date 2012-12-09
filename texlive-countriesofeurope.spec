# revision 26042
# category Package
# catalog-ctan /fonts/countriesofeurope
# catalog-date 2012-04-19 16:32:32 +0200
# catalog-license lppl
# catalog-version 0.21
Name:		texlive-countriesofeurope
Version:	0.21
Release:	2
Summary:	A font with the images of the countries of Europe
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/countriesofeurope
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/countriesofeurope.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/countriesofeurope.doc.tar.xz
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
%{_texmfdistdir}/dvips/countriesofeurope/config.CountriesOfEurope
%{_texmfdistdir}/fonts/afm/public/countriesofeurope/CountriesOfEurope.afm
%{_texmfdistdir}/fonts/enc/dvips/countriesofeurope/CountriesOfEurope.enc
%{_texmfdistdir}/fonts/map/dvips/countriesofeurope/CountriesOfEurope.map
%{_texmfdistdir}/fonts/tfm/public/countriesofeurope/CountriesOfEurope.tfm
%{_texmfdistdir}/fonts/type1/public/countriesofeurope/CountriesOfEurope.pfb
%{_texmfdistdir}/tex/latex/countriesofeurope/CountriesOfEurope.sty
%doc %{_texmfdistdir}/doc/fonts/countriesofeurope/CountriesOfEurope.pdf
%doc %{_texmfdistdir}/doc/fonts/countriesofeurope/CountriesOfEurope.tex
%doc %{_texmfdistdir}/doc/fonts/countriesofeurope/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.21-2
+ Revision: 813464
- Update to latest release.
- Import texlive-countriesofeurope
- Import texlive-countriesofeurope

