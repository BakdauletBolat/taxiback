from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from apps.message.models import Message
from apps.message.serializers import MessageSerializer
from apps.order.views import StandardResultsSetPagination


class ListUserMessageView(ListAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('created_at')