# Devops_Lab

## Exercise 1: Hello Pod

### Aim
To run an Nginx application using Kubernetes and access it through a browser.

### Commands Used

```bash
minikube start
kubectl run hello-k8s --image=nginx --port=80
kubectl get pods
kubectl expose pod hello-k8s --type=NodePort --port=80
minikube service hello-k8s

learned how to start a Kubernetes cluster using Minikube, run an Nginx Pod, check its status, expose it as a service, and access it through a browser.

# Exercise 2: Deploy Flask App on Minikube

## Aim
To deploy a Flask app on Kubernetes using Minikube.

## Steps
- Created `app.py` Flask application.
- Created a Dockerfile and built the `flask-app` image.
- Created `flask-deployment.yaml`.
- Deployed the Flask app using Kubernetes.
- Checked the Deployment and Pod status.
- Checked Flask logs.
- Created a NodePort Service.
- Accessed the Flask app using the Minikube Service URL.

## Output
`Hello from Flask on Kubernetes!`

## What I Learned
I learned how to build a Docker image, deploy a Flask app on Kubernetes, create a Service, and access the app using Minikube.

# Exercise 3 - Scaling Flask App using ReplicaSet

## What I did

1. Started Minikube with one node.
2. Created a Flask application.
3. Created a Dockerfile and built the Flask image.
4. Created a ReplicaSet with 3 replicas.
5. Created a Service for the Flask application.
6. Scaled the ReplicaSet from 3 Pods to 5 Pods.
7. Deleted one Pod and observed that Kubernetes automatically created a replacement Pod.
8. Checked the Pod distribution using `kubectl get pods -o wide`.

## What I understood

A ReplicaSet maintains the required number of Pods.

Initially, there were 3 Pods. I scaled the ReplicaSet to 5 Pods, so Kubernetes created 2 more Pods.

When I deleted one Pod, Kubernetes automatically created another Pod to maintain 5 Pods.

Since I used one Minikube node, all 5 Pods were running on the same node.

## Screenshots

- Minikube started
- Nodes checked
- Docker image built
- YAML applied
- Pods running
- ReplicaSet checked
- ReplicaSet scaled to 5
- Five Pods verified
- Pod self-healing verified
- Pod distribution checked

# Exercise 6: Real-Time Delivery Monitoring

## Objective
Build a real-time delivery monitoring system using Python, Prometheus, and Grafana.

## Technologies Used
- Python
- Prometheus
- Grafana
- Docker
- prometheus-client

## Project Structure

```text
Exercise-6/
├── delivery_monitoring/
│   ├── delivery_monitoring/
│   │   └── delivery_metrics.py
│   ├── prometheus.yml
│   └── alert_rules.yml
├── screenshots/
│   ├── 01-python-setup.png
│   ├── 02-python-app.png
│   ├── 03-prometheus-targets.png
│   ├── 04-grafana-running.png
│   ├── 05-grafana-prometheus-datasource.png
│   ├── 06-grafana-live-metrics.png
│   └── 07-grafana-dashboard.png
└── README.md
```

## Metrics Monitored
1. Total deliveries
2. Pending deliveries
3. Deliveries on the way
4. Average delivery time

## Configuration
- Python metrics endpoint: `http://localhost:8000/metrics`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3000`
- Prometheus scrape interval: 5 seconds

## Alert Rules
- HighPendingDeliveries: triggers when pending deliveries exceed 10 for 15 seconds.
- HighAverageDeliveryTime: triggers when average delivery time exceeds 30 seconds for 15 seconds.

## Verification
- Python metrics endpoint responds successfully.
- Prometheus `delivery_service` target reports UP.
- Grafana and Prometheus Docker containers are running.
- Four Grafana dashboard panels have been created.
- Seven screenshots have been saved in the screenshots folder.

## Screenshots
Refer to the `screenshots/` directory for evidence of the setup, metrics, Prometheus target status, and Grafana dashboard.

## Result
The Python delivery metrics application is exposing metrics successfully, Prometheus is scraping the delivery service, and Grafana is configured to visualize delivery performance.