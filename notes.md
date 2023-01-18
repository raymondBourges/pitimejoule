## Promscale
* doc https://docs.timescale.com/promscale/latest/

### Notes
* docker-compose inspiré de https://github.com/timescale/promscale/blob/master/docker-compose/docker-compose.yaml et de https://docs.timescale.com/install/latest/installation-docker/ pour la partie timescaledb
* Le docker compose contient notamment :
  * Promscale
  * Prometheus
  * Grafana
  * node exporteur (avec une conf pour lire les informations sur la machine hôte)

## Prometheus
* doc https://prometheus.io/docs/introduction/overview/
* conf dans prometheus.yml
* data dans /var/lib/prometheu
* accès via http://localhost:9090/
* notes
  * https://prometheus.io/docs/concepts/jobs_instances/ --> The up time series is useful for instance availability monitoring

## Grafana
* doc https://grafana.com/docs/grafana/latest/
* conf dans grafana.ini
* data dans /var/lib/grafana
* accès via http://localhost:3000
* Complément de configuration via l'IHM de grafana
  * Ajout d'une datasource de type prometheus mais branchée sur Promscale via http://promscale:9201

## pgadmin
* Installation via :
    ```
    sudo apt install pgadmin4-desktop
    sudo update-alternatives --install /usr/local/bin/pgadmin pgadmin /usr/pgadmin4/bin/pgadmin4 0
    ```
## FastAPI
* doc https://fastapi.tiangolo.com/fr/
* run 
```
export ETCD_HOST=localhost
export ETCD_PORT=2379
cd fastapi
uvicorn app.main:app --port 8001 --reload
```

## Etcd
* doc https://etcd.io/docs/
* récupération de ~/.local/bin/etcdctl et etcdutl depuis zip dans https://github.com/etcd-io/etcd/releases/
