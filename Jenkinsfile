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
                sh "scp -o StrictHostKeyChecking=no -i ~/.ssh/ansible_id_rsa docker-compose.yaml swarm-manager:/home/jenkins/docker-compose.yaml"
                sh "ansible-playbook -v -i ansible/inventory.yaml ansible/playbook.yaml"
            }
        }
    }
}

