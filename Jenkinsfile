peline {
    
   checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/praveenramaraj/assesments.git']]])
   
    stages {
        stage('input1') {
            steps {
                echo 'Executing ip_print with input1'
                sh 'python3 ip_print/ip_print.py --json input1.json'
            }
        }
        stage('input2') {
            steps {
                echo 'Executing ip_print with input2'
                sh 'python3 ip_print/ip_print.py --json input2.json'
            }
        }
    }
}1
