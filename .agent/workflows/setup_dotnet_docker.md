---
description: Configurar y ejecutar entorno de desarrollo .NET usando Docker
---

# Configuración de Entorno .NET (Dockerizado)

Este workflow permite levantar un entorno de desarrollo .NET 8.0 efímero y aislado, sin instalar nada en el host.

## Prerrequisitos
- Docker instalado y corriendo.

## Pasos

1. **Descargar la imagen oficial**
   Asegura tener la última versión del SDK.
   ```bash
   docker pull mcr.microsoft.com/dotnet/sdk:8.0
   ```

2. **Iniciar el Contenedor**
   Ejecuta un contenedor interactivo que se borra al salir (`--rm`).
   Montamos el directorio actual (`$PWD`) en `/app` para poder editar el código desde el host y ejecutarlo dentro.
   ```bash
   // turbo
   docker run -it --rm -v "$(pwd):/app" -w /app mcr.microsoft.com/dotnet/sdk:8.0 /bin/bash
   ```

3. **Verificación (Dentro del contenedor)**
   Una vez dentro, verifica la versión:
   ```bash
   dotnet --version
   ```
