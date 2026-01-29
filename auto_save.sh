#!/bin/bash

# Configuración
INTERVALO=1200 # 20 minutos en segundos (20 * 60)

echo "🤖 AGENTE REPOSITORIO: Modo Automático Activado"
echo "==============================================="
echo "Reglas:"
echo "1. Pull al arrancar."
echo "2. Push cada 20 minutos si hay cambios."
echo "-----------------------------------------------"

# 1. Pull Inicial (Paso 0 del protocolo)
echo "⬇️  [INICIO] Sincronizando con GitHub (git pull)..."
git pull origin main

if [ $? -eq 0 ]; then
    echo "✅ Sincronización completada."
else
    echo "⚠️  Hubo un problema con el pull. Revisa conflictos."
fi

# 2. Bucle infinito
while true; do
    echo "⏳ Esperando 20 minutos para el siguiente escaneo..."
    sleep $INTERVALO

    # Comprueba si hay cambios pendientes (staged, unstaged o untracked)
    if [[ `git status --porcelain` ]]; then
        echo "📝 [DETECTADO] Hay cambios en el proyecto."
        echo "⬆️  Subiendo cambios..."
        
        # Flujo de guardado
        git add .
        git commit -m "auto: guardado periódico (cada 20 min)"
        git push origin main
        
        if [ $? -eq 0 ]; then
            echo "✅ [ÉXITO] Cambios guardados en la nube."
        else
            echo "❌ [ERROR] No se pudo subir. Revisa tu conexión."
        fi
    else
        echo "zzZ... [SIN CAMBIOS] El proyecto está limpio. Seguimos vigilando."
    fi
done
