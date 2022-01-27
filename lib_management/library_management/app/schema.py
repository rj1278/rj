from rest_framework.schemas.openapi import AutoSchema

class CustomSchema(AutoSchema):
    def get_operation(self, path, method):
        op = super().get_operation(path, method)
        op['parameters'].append({
            "name": "email",
            "in": "query",
            "required": True,
            "description": "Admin user email only allowed",
            'schema': {'type': 'string'}
        }
        )
        return op

class IdCustomSchema(AutoSchema):
    def get_operation(self, path, method):
        op = super().get_operation(path, method)
        op['parameters'].append({
            "name": "email",
            "in": "query",
            "required": True,
            "description": "Admin user email only allowed",
            'schema': {'type': 'string'}
        })
        op['parameters'].append({
            "name": "id",
            "in": "query",
            "required": True,
            "description": "Give book id for delete operation",
            'schema': {'type': 'integer'}
        }
        )
        return op



    #      @action(methods=['post'],detail=False,schema=AutoSchema(tags=['BOOK']),serializer_class=BookSerializer)
    # def update_(self,request):
    #     data=validate(request.query_params.get("email"))
    #     if data:
    #         serializer=self.serializer_class(instance=data['id'],data=request.data,partial=True)
    #         if serializer.is_valid():
    #             serializer.save()
    #         return Response({'status':status.HTTP_200_OK})
    #     return Response({'status':status.HTTP_401_UNAUTHORIZED})