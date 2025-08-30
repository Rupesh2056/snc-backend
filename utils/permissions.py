from django.shortcuts import redirect
from django.urls import reverse_lazy

class AccessMixin:
     def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated :
        
            return super().dispatch(request, *args, **kwargs)
        return redirect(reverse_lazy("user_login"))