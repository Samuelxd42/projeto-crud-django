from django.shortcuts import render, HttpResponse


def hello(request, nome, idade):
    return HttpResponse('<h1> Hello World {} Você tem {} </h1>'.format(nome, idade))


def soma(request, n1, n2):
    soma = n1 + n2
    return HttpResponse('<h1> Soma => {} {} a soma = {}</h1>'.format(n1, n2, soma))


def sub(request, n1, n2):
    subtracao = n1 - n2
    return HttpResponse('<h1> Subtracao => {} {} a subtracao = {}</h1>'.format(n1, n2, subtracao))


def div(request, n1, n2):
    divisao = n1 / n2
    return HttpResponse('<h1>Divisao=> {} {} divisao = {}</h1>'.format(n1, n2, divisao))


def mult(request, n1, n2):
    multiplicao = n1 * n2
    return HttpResponse('<h1>Multiplicao=> {} {} divisao = {}</h1>'.format(n1, n2, multiplicao))
