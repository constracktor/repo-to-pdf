#/bin/bash
# $1: Path to repository to convert to PDF

# Install wkhtmltox
WKHTMLTOX_DIR=wkhtmltox
if [[ ! -d $WKHTMLTOX_DIR ]]; then
    (
	FILENAME="wkhtmltox_0.12.6.1-2.jammy_amd64.deb"
	DOWNLOAD_URL=https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/$FILENAME
        mkdir -p $WKHTMLTOX_DIR
	cd $WKHTMLTOX_DIR
        wget $DOWNLOAD_URL
	ar -vx $FILENAME
	tar xf data.tar.xz
	rm -r $(ls -A | grep -v usr)
    )
fi

# Create Python environment
PYTHON_ENV_DIR=.venv
if [[ ! -d $PYTHON_ENV_DIR ]]; then
    (
	python3 -m venv $PYTHON_ENV_DIR
	source $PYTHON_ENV_DIR/bin/activate
        pip3 install -r requirements.txt
    )
fi

# Add wkhtmltox to path
export PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd )/wkhtmltox/usr/local/bin":$PATH
# Acitvate Python environment
source $PYTHON_ENV_DIR/bin/activate
# Convert repository to pdf file
python3 generate_pdf.py $1
# Merge created PDF with existing PDF files
python3 merge_pdf.py $1
