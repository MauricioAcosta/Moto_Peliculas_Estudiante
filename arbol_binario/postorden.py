#!/usr/bin/python
# -*- coding: utf-8 -*-
class Nodo():
	def __init__ (self,valor,izq=None,der=None):
		self.valor=valor
		self.izquierda=izq
		self.derecha=der

def postorden(arbol):
	if arbol==None:
		return ""
	else:
		return postorden(arbol.izquierda)+postorden(arbol.derecha)+arbol.valor

def evaluar(arbol):
	if arbol.valor=='+':
		return evaluar(arbol.izquierda)+evaluar(arbol.derecha)
	elif arbol.valor=='-':
		return evaluar(arbol.izquierda)-evaluar(arbol.derecha)
	elif arbol.valor=='*':
		return evaluar(arbol.izquierda)*evaluar(arbol.derecha)
	elif arbol.valor=='/':
		return evaluar(arbol.izquierda)/evaluar(arbol.derecha)
	else:
		return int(arbol.valor)

print (postorden( Nodo('3',Nodo('2'),Nodo('+',Nodo('5', Nodo('8',Nodo('-',Nodo('+',Nodo('A')))))))  ))