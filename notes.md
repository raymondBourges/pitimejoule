## Prometheus
* doc https://prometheus.io/docs/introduction/overview/
* conf dans prometheus.yml
* data dans /var/lib/prometheus
* accès via http://localhost:9090/
* notes
  * https://prometheus.io/docs/concepts/jobs_instances/ --> The up time series is useful for instance availability monitoring

## Grafana
* doc https://grafana.com/docs/grafana/latest/
* conf dans grafana.ini
* data dans /var/lib/grafana
* accès via http://localhost:3000
* Complément de configuration via l'IHM de grafana
  * Ajout d'une datasource de type prometheus mais branchée sur Promscale via http://prometheus:9090

