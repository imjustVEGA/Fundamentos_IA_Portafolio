"""Ejecuta el notebook completo con un kernel del mismo entorno Python."""
import os
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
os.environ['MPLCONFIGDIR'] = str(ROOT / '.mplconfig')
os.environ['JUPYTER_RUNTIME_DIR'] = str(ROOT / '.jupyter-runtime')

import nbformat
from nbclient import NotebookClient
from jupyter_client.kernelspec import KernelSpecManager

(ROOT / '.build').mkdir(exist_ok=True)
with tempfile.TemporaryDirectory(dir=ROOT / '.build') as temporal:
    kernel = Path(temporal) / 'python-local'
    kernel.mkdir()
    import json
    (kernel / 'kernel.json').write_text(json.dumps({
        'argv': [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'],
        'display_name': 'Python local', 'language': 'python',
    }), encoding='utf-8')
    manager = KernelSpecManager(kernel_dirs=[temporal])
    notebook = nbformat.read(ROOT / 'inundacion.ipynb', as_version=4)
    nbformat.validate(notebook)
    client = NotebookClient(notebook, timeout=180, kernel_name='python-local',
                            resources={'metadata': {'path': str(ROOT)}})
    client.create_kernel_manager()
    client.km.kernel_spec_manager = manager
    client.execute()
    nbformat.write(notebook, ROOT / 'inundacion.ipynb')
    for celda in notebook.cells:
        if celda.cell_type == 'code':
            for salida in celda.outputs:
                if salida.output_type == 'stream':
                    print(salida.text, end='')
print('Notebook ejecutado y guardado sin errores.')
