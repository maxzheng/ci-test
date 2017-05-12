pipeline {
    agent { docker 'maxzheng/tox' }
    stages {
        stage('build') {
            steps {
                sh 'tox'
            }
        }
    }
}
