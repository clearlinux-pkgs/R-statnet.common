#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-statnet.common
Version  : 4.5.0
Release  : 44
URL      : https://cran.r-project.org/src/contrib/statnet.common_4.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/statnet.common_4.5.0.tar.gz
Summary  : Common R Scripts and Utilities Used by the Statnet Project
Group    : Development/Tools
License  : GPL-3.0
Requires: R-statnet.common-lib = %{version}-%{release}
Requires: R-coda
BuildRequires : R-coda
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-statnet.common package.
Group: Libraries

%description lib
lib components for the R-statnet.common package.


%prep
%setup -q -c -n statnet.common
cd %{_builddir}/statnet.common

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641132103

%install
export SOURCE_DATE_EPOCH=1641132103
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library statnet.common
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library statnet.common
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library statnet.common
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc statnet.common || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/statnet.common/CITATION
/usr/lib64/R/library/statnet.common/DESCRIPTION
/usr/lib64/R/library/statnet.common/INDEX
/usr/lib64/R/library/statnet.common/LICENSE
/usr/lib64/R/library/statnet.common/Meta/Rd.rds
/usr/lib64/R/library/statnet.common/Meta/features.rds
/usr/lib64/R/library/statnet.common/Meta/hsearch.rds
/usr/lib64/R/library/statnet.common/Meta/links.rds
/usr/lib64/R/library/statnet.common/Meta/nsInfo.rds
/usr/lib64/R/library/statnet.common/Meta/package.rds
/usr/lib64/R/library/statnet.common/NAMESPACE
/usr/lib64/R/library/statnet.common/NEWS
/usr/lib64/R/library/statnet.common/NEWS.md
/usr/lib64/R/library/statnet.common/R/statnet.common
/usr/lib64/R/library/statnet.common/R/statnet.common.rdb
/usr/lib64/R/library/statnet.common/R/statnet.common.rdx
/usr/lib64/R/library/statnet.common/help/AnIndex
/usr/lib64/R/library/statnet.common/help/aliases.rds
/usr/lib64/R/library/statnet.common/help/paths.rds
/usr/lib64/R/library/statnet.common/help/statnet.common.rdb
/usr/lib64/R/library/statnet.common/help/statnet.common.rdx
/usr/lib64/R/library/statnet.common/html/00Index.html
/usr/lib64/R/library/statnet.common/html/R.css
/usr/lib64/R/library/statnet.common/templates/snctrl.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/statnet.common/libs/statnet.common.so
/usr/lib64/R/library/statnet.common/libs/statnet.common.so.avx2
/usr/lib64/R/library/statnet.common/libs/statnet.common.so.avx512
