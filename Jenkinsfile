pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                bat 'C:\\Users\\damod\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install pytest-html allure-pytest selenium webdriver-manager'
            }
        }
        stage('Run Pytest') {
            steps {
                bat 'C:\\Users\\damod\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pytest --html=report.html --alluredir=allure-results'
            }
        }
        stage('Generate Allure Report') {
            steps {
                bat 'allure serve allure-results'
            }
        }
    }
}
