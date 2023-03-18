curl http://localhost:3000/api/v1/entities/dataSources \
  -H "Content-Type: application/vnd.gooddata.api+json" \
  -H "Accept: application/vnd.gooddata.api+json" \
  -H "Authorization: Bearer YWRtaW46Ym9vdHN0cmFwOmFkbWluMTIz" \
  -X POST \
  -d '{
      "data": {
          "attributes": {
              "name": "SFO-db",
              "url": "jdbc:postgresql://host.docker.internal:8731/sfo",
              "schema": "out__sfo_stats",
              "username":"sfo",
              "password":"sfo",
              "type": "POSTGRESQL"
          },
          "id": "ps-sfodb",
          "type": "dataSource"
      }
  }'

curl http://localhost:3000/api/v1/actions/dataSources/ps-sfodb/scan \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-H "Authorization: Bearer YWRtaW46Ym9vdHN0cmFwOmFkbWluMTIz" \
-X POST \
-d '{"separator": "__", "scanTables": true, "scanViews": false}' > pdm.json

curl http://localhost:3000/api/v1/layout/dataSources/ps-sfodb/physicalModel \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-H "Authorization: Bearer YWRtaW46Ym9vdHN0cmFwOmFkbWluMTIz" \
-X PUT \
-d @pdm.json

rm pdm.json