mkdir -p /pitimejoule/prometheus/data
mkdir -p /pitimejoule/grafana/lib
mkdir -p /pitimejoule/grafana/log

chown -R 65534:65534 /pitimejoule/prometheus 
chown -R 472:472 /pitimejoule/grafana

chmod -R g+rw /pitimejoule/prometheus 
chmod -R g+rw /pitimejoule/grafana
