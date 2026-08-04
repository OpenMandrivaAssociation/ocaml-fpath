%undefine _debugsource_packages
Name:		ocaml-fpath
Version:	0.7.3
Release:	2
Summary:	File system paths for OCaml
License:	ISC
URL:		https://erratique.ch/software/fpath
Source0:	fpath-0.7.3.tbz
BuildRequires:	ocaml >= 4.08
BuildRequires:	ocaml-compiler
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-ocamlbuild
BuildRequires:	ocaml-topkg-devel
BuildRequires:	ocaml-astring-devel

%description
File system paths for OCaml

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{EVRD}

%description devel
Development files for %{name}.

%prep
%autosetup -n fpath-0.7.3

%build
ocaml pkg/pkg.ml build --dev-pkg false

%install
%ocaml_install

%files -f .ofiles
%doc README* CHANGES*
%license LICENSE*

%files devel -f .ofiles-devel
