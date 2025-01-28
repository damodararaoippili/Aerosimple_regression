pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'C:\\Users\\damod\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install pytest-html allure-pytest selenium webdriver-manager'
            }
        }
        stage('Run Pytest') {
            steps {
                sh 'C:\\Users\\damod\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pytest --html=report.html --alluredir=allure-results'
            }
        }
        stage('Generate Allure Report') {
            steps {
                sh 'allure serve allure-results'
            }
        }
    }
}



