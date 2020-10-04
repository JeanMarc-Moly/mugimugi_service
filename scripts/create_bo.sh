find ./resources/xml/schema/ -type f -name '*.xsd' | xargs -i -t ./.python_env/bin/xsdata \
    --package mugimugi.bo \
    --output pydata \
    {}