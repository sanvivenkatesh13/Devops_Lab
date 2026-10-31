# Microservice Deployment with Configuration and Service Discovery

## Objective
To deploy interconnected Flask microservices using Docker and Kubernetes and demonstrate service discovery, configuration management and scaling.

## Technologies Used
- Python
- Flask
- Docker
- Kubernetes
- Minikube
- YAML

## Microservices

### 1. Shipment API
Provides shipment information such as customer name, source, destination and shipment status.

### 2. Tracking API
Fetches shipment details from the Shipment API and provides tracking information.

## Key Concepts
- Docker containerization
- Kubernetes Deployments and Services
- Service discovery using Kubernetes DNS
- Environment variables
- Microservice communication
- Scaling replicas
- Troubleshooting

## Kubernetes Deployment

Apply configurations:

```bash
kubectl apply -f kubernetes/shipment.yaml
kubectl apply -f kubernetes/tracking.yaml