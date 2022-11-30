## Prometheus
* doc https://prometheus.io/docs/introduction/overview/
* conf dans /etc/prometheus/prometheus.yml
* data dans /var/lib/prometheus/metrics2/
* accès via http://localhost:9090/classic/graph

## Grafana
* doc https://grafana.com/docs/grafana/latest/
* conf dans /etc/grafana/grafana.ini
* data dans /var/lib/grafana
* accès via http://localhost:3000

## Promscale
* doc https://docs.timescale.com/promscale/latest/
* start via

### Notes
* docker-compose inspiré de https://github.com/timescale/promscale/blob/master/docker-compose/docker-compose.yaml et de https://docs.timescale.com/install/latest/installation-docker/ pour la partie timescaledb
* connexion de secours via 
  ```
  sudo su postgres -c 'psql'
  ```

## pgadmin
* doc sudo apt install pgadmin4-desktop
  * en plus 
    ```
    sudo update-alternatives --install /usr/local/bin/pgadmin pgadmin /usr/pgadmin4/bin/pgadmin4 0
    ```
* 
