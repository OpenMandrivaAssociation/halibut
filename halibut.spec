%define svndate 20100504
%define svnver 8934

%define _disable_lto 1

Name:		halibut
Summary:	TeX-like software manual tool
Version:	1.3
Release:	2
License:	MIT
Group:		Text tools
URL:		https://www.chiark.greenend.org.uk/~sgtatham/halibut.html
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  svn export -r %{svnver} svn://svn.tartarus.org/sgt/halibut halibut-%{svndate}
#  pushd halibut-%{svndate}
#  svn export -r %{svnver} svn://svn.tartarus.org/sgt/charset
#  popd
#  tar -cjvf halibut-%{svndate}.tar.bz2 halibut-%{svndate}
#Source0:	%{name}-%{svndate}.tar.bz2
# No need now to use git. Tarball available
Source0:    https://www.chiark.greenend.org.uk/~sgtatham/halibut/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:    halibut.vim
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
%setup -q

%build
%cmake

%make_build 

%install
cd build
%make_install 
cd doc 
%make_install
mkdir -p %{buildroot}/%{_datadir}/vim/vimfiles/syntax
cp %{SOURCE1} %{buildroot}/%{_datadir}/vim/vimfiles/syntax/

%files
%doc LICENCE 
%{_infodir}/%{name}*
%{_docdir}/halibut/*.html
%{_bindir}/halibut
%{_mandir}/man1/*.1*

%files -n vim-halibut
%{_datadir}/vim/vimfiles/syntax/*.vim
