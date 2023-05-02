void setBuildStatus(String message, String state, String repo_url) {
  step([
      $class: "GitHubCommitStatusSetter",
      reposSource: [$class: "ManuallyEnteredRepositorySource", url: repo_url],
      contextSource: [$class: "ManuallyEnteredCommitContextSource", context: "ci/jenkins/build-status"],
      errorHandlers: [[$class: "ChangingBuildStatusErrorHandler", result: "UNSTABLE"]],
      statusResultSource: [ $class: "ConditionalStatusResultSource", results: [[$class: "AnyBuildResult", message: message, state: state]] ]
  ]);
}

pipeline {
    agent any

    stages {
        stage('Run cfn-lint linter') {
            steps {
                echo "Running cfn-lint..."
                sh 'cfn-lint $(pwd)/pipeline/webhosting/cloudfront-s3-website.yaml'
                sh 'cfn-lint $(pwd)/pipeline/webhosting/pipeline.yaml'

            }
        }
        stage('Run cfn-nag linter'){
            when { expression { false } }
            steps {
                sh 'docker pull stelligent/cfn_nag:latest'
                sh 'docker run -v $(pwd)/pipeline/webhosting:/templates -t stelligent/cfn_nag /templates/cloudfront-s3-website.yaml'
                sh 'docker run -v $(pwd)/pipeline/webhosting:/templates -t stelligent/cfn_nag /templates/pipeline.yaml'
            }
        } 
        stage('Running FortiDevSec scans...') {
            when { expression { false } }
            steps {
                echo "Running SAST scan..."
                sh 'env | grep -E "JENKINS_HOME|BUILD_ID|GIT_BRANCH|GIT_COMMIT" > /tmp/env'
                sh 'docker pull registry.fortidevsec.forticloud.com/fdevsec_sast:latest'
                sh 'docker run --rm --env-file /tmp/env --mount type=bind,source=$PWD,target=/scan registry.fortidevsec.forticloud.com/fdevsec_sast:latest'
            }
        }
    }
    post {
     success {
        setBuildStatus("Build succeeded", "SUCCESS", "${GIT_URL}");
     }
     failure {
        setBuildStatus("Build failed", "FAILURE", "${GIT_URL}");
     }
  }
}
