FROM gitpod/workspace-postgres

USER gitpod

RUN wget -O - https://nightly.odoo.com/odoo.key | sudo apt-key add - && \
    echo "deb http://nightly.odoo.com/13.0/nightly/deb/ ./" | sudo tee -a /etc/apt/sources.list.d/odoo.list > /dev/null && \
    sudo apt-get update && \
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -yq odoo xfonts-75dpi xfonts-base && \
    wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.bionic_amd64.deb && \
    sudo dpkg -i wkhtmltox_0.12.5-1.bionic_amd64.deb && \
    sudo DEBIAN_FRONTEND=noninteractive apt-get install -yqf && \
    sudo ln -s /usr/local/bin/wkhtmltopdf /usr/bin && \
    sudo ln -s /usr/local/bin/wkhtmltoimage /usr/bin