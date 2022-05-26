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
            script{// 集成allure，目录需要和保存的results保持一致，注意此处目录为job工作目录之后的目录，Jenkins会自动将根目录与path进行拼接
                    allure includeProperties: false, jdk: '', report: 'allure-report', results: [[path: 'report']]
                }
            emailext(
                subject: '构建通知：${PROJECT_NAME} - Build # ${BUILD_NUMBER} - ${BUILD_STATUS}!',
                body: '${FILE,path="email.html"}',
                to: '1695735420@qq.com'
            )
        }
    }
}
