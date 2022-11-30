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
  * en plus 
    ```
    echo "shared_preload_libraries = 'timescaledb'" >> /etc/postgresql/14/main/postgresql.conf
    ```
* conf dans /etc/postgresql/14/main/
  * maintenu sous git pour modifs (user notamment)
    * puis 
      ```
      CREATE ROLE rbo WITH LOGIN PASSWORD 'rbo';
      ```
### Notes
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
