pipeline {
    agent {
        label 'docker-ssh-slave'
    }
    stages {
        stage('Print neš') {
            steps {
                println currentBuild.projectName
                println currentBuild.number
            }
        }
    }
}

