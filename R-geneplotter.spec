%global packname  geneplotter
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.32.1
Release:          1
Summary:          Graphics related functions for Bioconductor
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-Biobase R-annotate R-lattice 
Requires:         R-annotate R-AnnotationDbi R-Biobase R-graphics R-grDevices R-grid R-methods R-RColorBrewer R-stats R-utils 
Requires:         R-Biobase R-Rgraphviz R-annotate R-fibroEset R-hgu95av2.db R-hu6800.db R-hgu133a.db 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-Biobase R-annotate R-lattice
BuildRequires:    R-annotate R-AnnotationDbi R-Biobase R-graphics R-grDevices R-grid R-methods R-RColorBrewer R-stats R-utils 
BuildRequires:    R-Biobase R-Rgraphviz R-annotate R-fibroEset R-hgu95av2.db R-hu6800.db R-hgu133a.db 
BuildRequires:    x11-server-xvfb

%description
Some basic functions for plotting genetic data

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Fails in build system
%if 0
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
