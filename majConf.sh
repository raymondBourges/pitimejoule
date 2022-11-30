cp etc/prometheus/prometheus.yml /etc/prometheus/.
cp etc/grafana/grafana.ini /etc/grafana/.
systemctl restart prometheus.service
systemctl restart grafana-server.service