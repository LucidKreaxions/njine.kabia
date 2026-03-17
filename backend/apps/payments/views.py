from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
import uuid

from .models import Payment
from .serializers import PaymentSerializer

# Create your views here.
# list user payments
class PaymentCreateView(generics.CreateAPIView):

    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        transaction_id = str(uuid.uuid4())

        serializer.save(
            user=self.request.user,
            transaction_id=transaction_id,
            status="completed"
        )

# payment detail
class PaymentDetailView(generics.RetrieveAPIView):

    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)


class PaymentDetailView(generics.RetrieveAPIView):

    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)

class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
