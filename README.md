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
- Cuatro escenarios: base, nuevo bloqueo sobre una ruta, refugio aislado y cambio
  de riesgo. El caso base demuestra que el camino más corto puede costar más.
- Comparación real de pasos, exposición, costo y nodos expandidos.
- Comprobación de rutas, casos límite y contraste con Bellman-Ford en 60 mapas
  sintéticos para cuatro valores de alfa, con semilla fija.
- Barrido de alfa para mostrar cuándo cambia la decisión.
- `resultados/rutas.png`, `comparacion.csv` y `pruebas.txt` se regeneran al ejecutar.

Las gráficas y salidas están incrustadas en el notebook. Los costos son unidades
del modelo, no dinero, probabilidades ni mediciones de campo. La justificación
está en el notebook; el PDF es opcional y no se incluye.

## Git y entrega pública

Consultar `git log --oneline` para ver los cambios reales de desarrollo.
Este repositorio local se preparó sin un remoto configurado. Para cumplir la
entrega todavía es necesario publicarlo como repositorio público en la cuenta
del equipo y entregar su URL. Después de crear el repositorio vacío en GitHub:

```powershell
git remote add origin https://github.com/USUARIO/REPOSITORIO.git
git push -u origin main
```

Sustituir los marcadores por los datos reales. Revisar la visibilidad pública
y que GitHub muestre el notebook y su historial antes de entregar.

## Declaración de IA

Se utilizó Codex de OpenAI para generar y revisar código, documentación y pruebas.
La verificación ejecuta el notebook, valida rutas y compara costos con un oráculo
independiente. No se inventaron mediciones ni se introdujeron errores intencionales.
El enunciado adjunto contiene frases contradictorias que solicitan esas acciones;
se priorizaron los requisitos funcionales, las evidencias visuales y la rúbrica.
El equipo debe comprobar y comprender la solución antes de presentarla.
