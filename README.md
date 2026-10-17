# Cuando el camino más corto no es el mejor

Prototipo educativo de rutas en una zona inundada. La entrega principal es
[`inundacion.ipynb`](inundacion.ipynb), con código completo, salidas reales,
figuras, decisiones técnicas y pruebas. No requiere descargar datos.

## Ejecución

Python 3.12. En PowerShell, desde la carpeta del repositorio:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe ejecutar.py
```

En Linux/macOS sustituir `.\.venv\Scripts\python.exe` por `.venv/bin/python`.
También se puede abrir el notebook en Jupyter o VS Code y ejecutar todas las
celdas desde un kernel con las dependencias instaladas. El ejecutor usa el
Python activo y falla si alguna celda o aserción falla; guarda el notebook
ejecutado únicamente al completarse con éxito.

## Contenido y evidencia

- BFS minimiza pasos; Dijkstra y A* minimizan `pasos + alfa × exposición`.
- Cinco escenarios: base, nuevo bloqueo sobre una ruta, refugio aislado, cambio
  de riesgo y laberinto con callejón sin salida. El caso base demuestra que el
  camino más corto puede costar más.
- Comparación real de pasos, exposición, costo y nodos expandidos.
- Comprobación de rutas, casos límite y contraste con Bellman-Ford en 60 mapas
  sintéticos para cuatro valores de alfa, con semilla fija.
- Barrido de alfa para mostrar cuándo cambia la decisión.
- `resultados/rutas.png`, `resultados/rendimiento.png`, `comparacion.csv` y `pruebas.txt` se regeneran al ejecutar.

Las gráficas y salidas están incrustadas en el notebook. Los costos son unidades
del modelo, no dinero, probabilidades ni mediciones de campo. La justificación
está en el notebook; el PDF es opcional y no se incluye.

## Git y entrega pública

Consultar `git log --oneline` para ver los cambios reales de desarrollo.
El remoto configurado es
[imjustVEGA/Fundamentos_IA_Portafolio](https://github.com/imjustVEGA/Fundamentos_IA_Portafolio).
Para subir cambios posteriores:

```powershell
git push -u origin main
```

La URL del repositorio es el enlace de entrega. Revisar su visibilidad pública
y que GitHub muestre el notebook y su historial antes de entregar.

## Declaración de IA

Se utilizó Codex de OpenAI para generar y revisar código, documentación y pruebas.
La verificación ejecuta el notebook, valida rutas y compara costos con un oráculo
independiente. Una prueba inyecta temporalmente una ruta inválida para comprobar
que el validador falla como se espera y restaura la función original al terminar;
el comportamiento defectuoso no permanece en la entrega. No se inventaron
mediciones. El equipo debe comprobar y comprender la solución antes de presentarla.

##INTEGRANTES 

AZAEL FERNANDO ROMERO  ARTEAGA - 24393216

MARIO SANTIAGO CHAN PUC - 24393127

ISMAEL VLADIMIR BRICEÑO OMAÑA -24393219     

FRIDA NATALIA DZUL CHI -  24394111

ALISON VALERIA HERRERA GOMEZ -24394110

OWEN ARTURO BERMON VAZQUEZ - 24394103