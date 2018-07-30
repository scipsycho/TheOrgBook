'''
Enclose property names in double quotes in order to JSON serialize the contents in the API
'''
CUSTOMIZATIONS  = {
          "serializers":
          {
              "Location":
              {
                  "includeFields":[
                        "id",
                        "last_updated",
                        "city",
                        "province"
                  ]
              }
          }
}