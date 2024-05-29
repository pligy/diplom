FROM postgres:14

RUN apt-get update \
    && apt-get install --no-install-recommends --yes \
        postgresql-14-postgis-3 postgresql-14-postgis-3-scripts postgresql-contrib \
    && rm -rf /var/lib/apt/lists/*