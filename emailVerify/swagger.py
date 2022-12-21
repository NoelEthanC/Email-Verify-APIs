from drf_yasg.generators import OpenAPISchemaGenerator 

class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def __init__(self):
            print("in init")
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        print('this is schema',schema)
        return schema   
    