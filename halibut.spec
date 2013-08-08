%define svndate 20100504
%define svnver 8934

Name:		halibut
Summary:	TeX-like software manual tool
Version:	1.0
Release:	%mkrel 2.%{svndate}svn%{svnver}
License:	MIT
Group:		Text tools
URL:		http://www.chiark.greenend.org.uk/~sgtatham/halibut.html
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  svn export -r %{svnver} svn://svn.tartarus.org/sgt/halibut halibut-%{svndate}
#  pushd halibut-%{svndate}
#  svn export -r %{svnver} svn://svn.tartarus.org/sgt/charset
#  popd
#  tar -cjvf halibut-%{svndate}.tar.bz2 halibut-%{svndate}
Source0:	%{name}-%{svndate}.tar.bz2

%description
Halibut is yet another text formatting system, intended primarily for
writing software documentation. It accepts a single source format and
outputs a variety of formats, planned to include text, HTML, Texinfo,
Windows Help, Windows HTMLHelp, PostScript and PDF. It has comprehensive
indexing and cross-referencing support, and generates hyperlinks within
output documents wherever possible.


%package	-n vim-halibut
Summary:	Syntax file for the halibut manual tool
Group:		Editors
Requires:	vim-common
BuildArch:	noarch

%description -n vim-halibut
This package provides vim syntax support for Halibut input files (*.but).


%prep
%setup -q -n %{name}-%{svndate}


%build
sed -i 's/CFLAGS += -g/CFLAGS += /g' Makefile
export CFLAGS="%{optflags}"
make VERSION="%{version}"
%make -C doc


%install
%makeinstall INSTALL="install -Dp"
install -d  html
install -pm 0644 doc/*.html html
install -d %{buildroot}%{_datadir}/vim/syntax
install -pm 0644 misc/halibut.vim %{buildroot}%{_datadir}/vim/syntax


%files
%doc LICENCE html
%{_bindir}/halibut
%{_mandir}/man1/*.1*

%files -n vim-halibut
%{_datadir}/vim/syntax/*.vim
