#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ngx_brotli
Version  : e505dce68acc190cc5a1e780a3b0275e39f160ca
Release  : 33
URL      : https://github.com/google/ngx_brotli/archive/e505dce68acc190cc5a1e780a3b0275e39f160ca.tar.gz
Source0  : https://github.com/google/ngx_brotli/archive/e505dce68acc190cc5a1e780a3b0275e39f160ca.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: ngx_brotli-lib = %{version}-%{release}
BuildRequires : buildreq-nginx
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libbrotlicommon)

%description
# ngx_brotli
Brotli is a generic-purpose lossless compression algorithm that compresses data
using a combination of a modern variant of the LZ77 algorithm, Huffman coding
and 2nd order context modeling, with a compression ratio comparable to the best
currently available general-purpose compression methods. It is similar in speed
with deflate but offers more dense compression.

%package lib
Summary: lib components for the ngx_brotli package.
Group: Libraries

%description lib
lib components for the ngx_brotli package.


%prep
%setup -q -n ngx_brotli-e505dce68acc190cc5a1e780a3b0275e39f160ca
cd %{_builddir}/ngx_brotli-e505dce68acc190cc5a1e780a3b0275e39f160ca

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
nginx-module configure
nginx-module build

%install
nginx-module install %{buildroot}


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/nginx-mainline/ngx_http_brotli_filter_module.so
/usr/lib64/nginx-mainline/ngx_http_brotli_static_module.so
