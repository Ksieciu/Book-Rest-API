from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import url_has_allowed_host_and_scheme


def books_list_redirect_view(request, *args, **kwargs):
    return redirect('/api/books/')
