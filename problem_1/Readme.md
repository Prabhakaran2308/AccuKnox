# Wisecow Application Deployment

## Docker Deployment

### Prerequisites
- Docker installed on your local machine.
- Kubectl and Minikube on your local machine.

### Steps

1. **Build the Docker Image:**
   ```bash
   docker build -t my-wisecow-image:latest .
   ```

2. **Run the Docker Container:**
   ```bash
   docker run -p 4499:4499 my-wisecow-image
   ```

   This will start the Wisecow application and expose it on port 4499.

3. **Access the Application:**
   Open your web browser and navigate to [http://localhost:4499](http://localhost:4499) to access the Wisecow application.

---

## Kubernetes Deployment

### Prerequisites
- Minikube installed on your local machine.
- Basic knowledge of Kubernetes and `kubectl` commands.

### Steps

1. **Start Minikube Cluster:**
   ```bash
   minikube start
   ```

2. **Build and Push Docker Image to Minikube Registry:**
   ```bash
   eval $(minikube docker-env)
   docker build -t my-wisecow-image:latest .
   docker tag my-wisecow-image:latest $(minikube ip):31040/my-wisecow-image:latest
   docker push $(minikube ip):31040/my-wisecow-image:latest
   ```

3. **Deploy the Application:**
   ```bash
   kubectl apply -f wisecow-deployment.yaml
   ```

4. **Expose the Application as a Service:**
   ```bash
   kubectl expose deployment wisecow-deployment --type=LoadBalancer --port=80
   ```

5. **Access the Application:**
   ```bash
   minikube service wisecow-deployment
   ```

   This will open the Wisecow application in your default web browser.

---
## Output:


Added screenshots for reference.

Successfully containerized the Wisecow application using Docker and orchestrated the application in Kubernetes. For local testing, I utilized port forwarding to map the application to port 80 local. 
 
![image](https://github.com/Prabhakaran2308/AccuKnox/assets/145963770/f47f8fe0-7da6-4073-8455-6fbfb5f09e7d)

![image](https://github.com/Prabhakaran2308/AccuKnox/assets/145963770/01511dba-98b6-4757-a1d7-7026b5c55863)




