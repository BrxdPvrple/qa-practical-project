pipeline {
    agent any
    stages{
        stage('Run Unit Tests') {
            steps{
                sh "bash scripts/tests.sh"
            }
        } 
        stage ('Build & Push Images') {
            environment {
                DOCKER_UNAME = credentials('docker_uname')
                DOCKER_PWORD = credentials('docker_pword')
            }
            steps {
                sh "bash scripts/docker.sh"        
            }
        }
        stage ("Run Ansible") {
            steps{
                sh "scp -i ~/.ssh/id_rsa docker-compose.yaml docker-swarm:/home/jenkins/docker-compose.yaml"
                sh "ansible-playbook -v -i Ansible/inventory.yaml Ansible/playbook.yaml"
            }
        }
    }
}

