pipeline {
    agent any
    stages{
        stage('Run Unit Tests') {
            steps{
                sh "bash unittests.sh"
            }
        } 
        stage ('Build & Push Images') {
            environment {
                DOCKER_UNAME = credentials('docker_uname')
                DOCKER_PWORD = credentials('docker_pword')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
                sh "docker-compose push"          
            }
        }
        stage ("Run Ansible") {
            steps{
                sh "scp -i ~/.ssh/id_rsa docker-compose.yaml docker-swarm:/home/clril/docker-compose.yaml"
                sh "ansible-playbook -v -i Ansible/inventory.yaml Ansible/playbook.yaml"
            }
        }
    }
}