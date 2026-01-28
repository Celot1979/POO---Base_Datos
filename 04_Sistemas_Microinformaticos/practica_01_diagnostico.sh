#!/bin/bash

# Script de Diagnóstico Rápido para IFCD0112
# Muestra información básica de CPU, Memoria y Disco

echo "========================================"
echo "    INFORME DE ESTADO DEL SISTEMA"
echo "========================================"
echo "Fecha: $(date)"
echo ""

# 1. Información del Procesador
echo "--- PROCESADOR (CPU) ---"
grep "model name" /proc/cpuinfo | head -n 1
echo ""

# 2. Información de Memoria RAM
echo "--- MEMORIA RAM (MB) ---"
free -h | grep "Mem"
echo ""

# 3. Espacio en Disco
echo "--- ESPACIO EN DISCO (Raíz /) ---"
df -h / | grep "/"
echo ""

echo "========================================"
echo "Diagnóstico finalizado."
echo "========================================"
