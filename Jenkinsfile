pipeline {
    agent any

    stages {
        stage('pull code') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/${branch}']], extensions: [], userRemoteConfigs: [[credentialsId: 'dd15805e-7fb9-44fc-bf1c-6c4bfea878ce', url: 'git@192.168.195.130:zhouchen_group/web_demo.git']]])
            }
        }
        stage('check code') {
            steps {
                // 引入sonarqube scanner工具
                script {
                    scannerHome = tool 'sonar-scanner'
                }
                // 引入sonarqube服务器环境
                withSonarQubeEnv('sonarqube') {
                    sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
        stage('build project') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('public project') {
            steps {
                deploy adapters: [tomcat8(credentialsId: '9738b87b-da98-41f5-a333-9d156d6c5a67', path: '', url: 'http://192.168.195.132:8080/')], contextPath: null, war: 'target/*.war'
            }
        }
    }
    post {
        always {
            emailext(
                subject: '构建通知：${PROJECT_NAME} - Build # ${BUILD_NUMBER} - ${BUILD_STATUS}!',
                body: '${FILE,path="email.html"}',
                to: '1695735420@qq.com'
            )
        }
    }
}
