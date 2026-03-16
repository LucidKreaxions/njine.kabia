from rest_framework import serializers
from .models import Order, OrderItem
from apps.menu.models import FoodItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ["food", "quantity"]


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "items", "total_price", "status", "created_at"]
        read_only_fields = ["total_price", "status"]

    
    # order logic
    def create(self, validated_data):

        items_data = validated_data.pop("items")
        user = self.context["request"].user

        order = Order.objects.create(user=user)

        total = 0

        for item in items_data:

            food = item["food"]
            quantity = item["quantity"]

            price = food.price * quantity

            OrderItem.objects.create(
                order=order,
                food=food,
                quantity=quantity,
                price=food.price
            )

            total += price

        order.total_price = total
        order.save()

        return order
