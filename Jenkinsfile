pipeline {
    agent any
    stages {
        stage('pull code') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/${branch}']], extensions: [], userRemoteConfigs: [[credentialsId: 'dd15805e-7fb9-44fc-bf1c-6c4bfea878ce', url: 'git@192.168.195.130:root/testool.git']]])
            }
        }
        stage('build project') {
            steps {
                sh 'pytest'
            }
        }
    }
    post {
        always {
            script {
                allure includeProperties: false, jdk: 'jdk1.8', report: 'allure-report', results: [[path: 'report']]
            }
            emailext(
                subject: '构建通知：${PROJECT_NAME} - Build # ${BUILD_NUMBER} - ${BUILD_STATUS}!',
                body: '${FILE,path="templates/email.html"}',
                to: '1695735420@qq.com'
            )
        }
    }
}
