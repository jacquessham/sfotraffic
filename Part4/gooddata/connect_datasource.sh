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
              "schema": "OUT__SFO_STATS",
              "username":"sfo",
              "password":"sfo",
              "type": "POSTGRESQL"
          },
          "id": "ps-sfodb",
          "type": "dataSource"
      }
  }'