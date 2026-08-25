# hello-platform

Aplicacion FastAPI de ejemplo para un flujo de despliegue con Docker y
Kubernetes. El servicio responde con informacion de la aplicacion y expone un
endpoint de salud para los probes del cluster.

## Funcionalidad

- `GET /` devuelve el nombre, la version y el mensaje de la aplicacion.
- `GET /health` devuelve `{ "status": "ok" }` para readiness y liveness.
- La API se ejecuta con Uvicorn en `0.0.0.0:8000`.
- La imagen se construye desde Python 3.12 slim.
- Kubernetes despliega 2 replicas en el namespace `hello-dev`.
- El Service `hello-platform` expone el puerto `80` y lo dirige al puerto `8000` de los pods.

## Requisitos

- Python 3.12+
- Docker
- `kubectl` y un cluster Kubernetes disponible para el despliegue

## Ejecucion local

Instala las dependencias y arranca la API:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Prueba los endpoints:

```bash
curl http://localhost:8000/
curl http://localhost:8000/health
```

La documentacion interactiva de FastAPI queda disponible en
`http://localhost:8000/docs`.

## Docker

Construye y ejecuta la imagen:

```bash
docker build -t hello-platform:1.0.0 .
docker run --rm -p 8000:8000 hello-platform:1.0.0
```

## Kubernetes

Aplica los manifiestos incluidos:

```bash
kubectl create namespace hello-dev
kubectl apply -f k8s/ -n hello-dev
kubectl get pods,service -n hello-dev
```

Para acceder al Service desde la maquina local:

```bash
kubectl port-forward service/hello-platform 8080:80 -n hello-dev
curl http://localhost:8080/
curl http://localhost:8080/health
```

El Deployment usa la imagen `hello-platform:1.0.0` con
`imagePullPolicy: IfNotPresent`; en un cluster local, carga la imagen en el
runtime del cluster antes de aplicar el manifiesto si no esta disponible en un
registry.

## Estructura

```text
app/                 Codigo de la API FastAPI
tests/               Pruebas de la aplicacion
k8s/deployment.yaml  Deployment, replicas, recursos y probes
k8s/service.yaml     Service interno tipo ClusterIP
Dockerfile           Imagen de produccion
requirements.txt     Dependencias Python
```

El repositorio contiene los manifiestos preparados para un flujo GitOps. La
configuracion concreta de CI/CD y la Application de Argo CD deben definirse en
la plataforma o repositorio de infraestructura que consuma estos manifiestos.
