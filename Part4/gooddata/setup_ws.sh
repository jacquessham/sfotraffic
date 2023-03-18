curl http://localhost:3000/api/v1/entities/workspaces \
  -H "Content-Type: application/vnd.gooddata.api+json" \
  -H "Accept: application/vnd.gooddata.api+json" \
  -H "Authorization: Bearer YWRtaW46Ym9vdHN0cmFwOmFkbWluMTIz" \
  -X POST \
  -d '{
      "data": {
          "attributes": {
              "name": "SFO Statistics"
          },
          "id": "sfo-stats",
          "type": "workspace"
      }
  }'

curl http://localhost:3000/api/v1/layout/workspaces/sfo-stats \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer YWRtaW46Ym9vdHN0cmFwOmFkbWluMTIz" \
  -X PUT \
  -d @sfo-stats_ldm.json