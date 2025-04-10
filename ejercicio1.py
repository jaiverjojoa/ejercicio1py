{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HKox6gBy1WeB"
      },
      "outputs": [],
      "source": [
        "# Taller Práctico: Python Básico y Manipulación de Strings\n",
        "# Duración estimada: 2 horas\n",
        "# Basado en los temas 1 y 3\n",
        "\n",
        "# ================================\n",
        "# Parte 1: Variables en Python\n",
        "# ================================\n",
        "\n",
        "# Ejercicio 1:\n",
        "# Declara tres variables: una con un número entero, una con un texto y una con un decimal.\n",
        "# Imprímelas en pantalla.\n",
        "\n",
        "\n",
        "\n",
        "# Ejercicio 2:\n",
        "# Intenta crear variables con los siguientes nombres. ¿Cuáles son válidas y cuáles no? Justifica.\n",
        "# 1variable, nombre_completo, NombreCompleto, nombre-completo, edad, def, _pais\n",
        "\n",
        "\n",
        "\n",
        "# Ejercicio 3:\n",
        "# Crea una variable que guarde tu nombre, otra tu apellido y otra tu edad.\n",
        "# Luego, imprime una frase como: \"Hola, me llamo Juan Pérez y tengo 25 años.\"\n",
        "\n",
        "\n",
        "\n",
        "# Ejercicio 4:\n",
        "# Usa la función type() para verificar el tipo de cada variable que creaste.\n",
        "\n",
        "\n",
        "\n",
        "# ================================\n",
        "# Parte 2: Strings en Python\n",
        "# ================================\n",
        "\n",
        "# Ejercicio 5:\n",
        "# Declara un string con tu nombre completo. Usa slicing para extraer tu primer nombre y tu apellido.\n",
        "\n",
        "\n",
        "\n",
        "# Ejercicio 6:\n",
        "# Usa los métodos de string para:\n",
        "# - Convertir tu nombre a mayúsculas\n",
        "# - Reemplazar letras con otras\n",
        "# - Eliminar espacios al inicio y al final\n",
        "\n",
        "\n",
        "\n",
        "# Ejercicio 7:\n",
        "# Crea una variable con un correo electrónico. Verifica si contiene el símbolo '@'.\n",
        "\n",
        "\n",
        "\n",
        "# Ejercicio 8:\n",
        "# Usa format() y f-strings para mostrar mensajes personalizados.\n",
        "# Ejemplo: \"Hola {nombre}, tu edad es {edad}\"\n",
        "\n",
        "\n",
        "\n",
        "# Ejercicio 9:\n",
        "# Usa .count(), .find() y .replace() en un string largo para:\n",
        "# - Contar cuántas veces aparece una letra\n",
        "# - Encontrar la posición de una palabra\n",
        "# - Reemplazar palabras por otras\n",
        "\n",
        "\n",
        "\n",
        "# ================================\n",
        "# Parte 3: Mini-proyecto guiado\n",
        "# ================================\n",
        "\n",
        "# Objetivo: Crear un sistema básico de registro de usuario\n",
        "# Paso 1: Solicita al usuario que ingrese su nombre, apellido, edad y correo.\n",
        "\n",
        "nombre = input(\"Ingresa tu nombre: \")\n",
        "apellido = input(\"Ingresa tu apellido: \")\n",
        "edad = input(\"Ingresa tu edad: \")\n",
        "correo = input(\"Ingresa tu correo electrónico: \")\n",
        "\n",
        "# Paso 2: Muestra un resumen con el siguiente formato:\n",
        "# \"Perfil registrado:\\nNombre completo: Juan Pérez\\nEdad: 25\\nEmail: juanp@example.com\"\n",
        "\n",
        "\n",
        "\n",
        "# Paso 3: (Desafío extra)\n",
        "# Genera un nombre de usuario automático con la primera letra del nombre + apellido + últimos 2 dígitos de la edad\n",
        "# Ejemplo: Juan Pérez, 25 años -> jperez25\n",
        "\n",
        "\n",
        "\n",
        "# Paso 4: (Desafío por puntos =))\n",
        "# Detecta si el correo no tiene \"@\" y muestra un mensaje de error si falta.\n",
        "\n",
        "\n",
        "\n",
        "# Paso 5:\n",
        "# Usa un literal multilinea (triple comillas) para mostrar un resumen decorado del usuario, tipo:\n",
        "# \"\"\"\n",
        "# === PERFIL ===\n",
        "# Nombre completo: Juan Pérez\n",
        "# Edad: 25\n",
        "# Email: juan@example.com\n",
        "# \"\"\"\n",
        "\n",
        "\n",
        "\n",
        "# Paso 6:\n",
        "# Importa el módulo datetime y muestra el año actual junto al mensaje:\n",
        "# \"Registro completado en el año 2025\"\n",
        "\n",
        "import datetime\n",
        "\n",
        "\n",
        "\n",
        "# Paso 7:\n",
        "# Pide al usuario un número y aumenta ese valor en 5. Muestra el resultado final.\n",
        "# Asegúrate de convertir la entrada a entero con int().\n",
        "\n",
        "\n",
        "\n",
        "# ================================\n",
        "# Parte 4: Extra Challenge\n",
        "# ================================\n",
        "\n",
        "# Escribe un programa que pida al usuario su nombre completo y devuelva:\n",
        "# - Cuántos caracteres tiene (sin contar espacios)\n",
        "# - Cuántas veces aparece la letra \"a\"\n",
        "# - Cuántas palabras tiene el nombre\n",
        "\n",
        "\n",
        "\n",
        "# ================================\n",
        "# Fin del taller\n",
        "# ================================\n",
        "# ¡Buen trabajo! Guarda este archivo con tus respuestas completadas."
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n"
      ],
      "metadata": {
        "id": "J7jVANs52fN-"
      }
    }
  ]
}