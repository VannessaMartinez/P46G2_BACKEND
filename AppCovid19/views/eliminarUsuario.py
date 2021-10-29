from django.conf                                      import settings
from rest_framework                                   import generics, status
from rest_framework.response                          import Response
from AppCovid19.serializers.userSerializer            import UserSerializer
from AppCovid19.models.user                           import User

class EliminarUsuario(generics.DestroyAPIView):
    serializer_class   = UserSerializer
    #permission_classes = (IsAuthenticated,)
    

    def delete(self, request, *args, **kwargs):

        try:

            usuario = queryset = User.objects.filter(username=request.data['usuario']).exists()
            if usuario:
                User.objects.filter(username=request.data['usuario']).delete()
                return Response("Usuario eliminado", status=status.HTTP_200_OK)     

            return Response("El usuario no existe", status=status.HTTP_404_NOT_FOUND) 
        except Exception as e:
            return Response('Error en el json', status=status.HTTP_400_BAD_REQUEST)