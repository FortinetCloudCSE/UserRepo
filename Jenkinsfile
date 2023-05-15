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

       stage('Running FortiDevSec scans...') {
            when { expression { false } }
            steps {
                echo "Running SAST scan..."
                sh 'env | grep -E "JENKINS_HOME|BUILD_ID|GIT_BRANCH|GIT_COMMIT" > /tmp/env'
                sh 'docker pull registry.fortidevsec.forticloud.com/fdevsec_sast:latest'
                sh 'docker run --rm --env-file /tmp/env --mount type=bind,source=$PWD,target=/scan registry.fortidevsec.forticloud.com/fdevsec_sast:latest'
            }
        }
        stage('Build docker container and upload to S3') {
            steps {
               echo "Building container..."
               sh '''
                   GIT_HASH=\$(git rev-parse HEAD)
                   REPO_NAME=$(basename -s .git `git config --get remote.origin.url`)
                   PKG_NAME=\${REPO_NAME,,}-\${GIT_HASH:0:5}
                   ./scripts/generate-site.sh /home/jenkins/.ssh/id_rsa /home/jenkins/.ssh/id_rsa.pub \$PKG_NAME
                   tar cvzf \$PKG_NAME.tar.gz \$PKG_NAME
                   aws s3 cp \$(pwd)/\$PKG_NAME.tar.gz s3://test-hugo-site-fortinetcloudcse
               '''
            }
        }
        stage('Assume role and generate pre-signed url') {
            steps {
               echo "Assuming role and generating pre-signed url..."
               sh '''
                   set +x
                   GIT_HASH=\$(git rev-parse HEAD)
                   REPO_NAME=\$(basename -s .git `git config --get remote.origin.url`)
                   PKG_NAME=\${REPO_NAME,,}-\${GIT_HASH:0:5}
                   output=\$(aws sts assume-role --role-arn arn:aws:iam::228122752878:role/get-hugo-app-role --role-session-name jenkins-test)
                   export AWS_SESSION_TOKEN=\$(echo $output | jq -r ."Credentials"."SessionToken")
                   export AWS_ACCESS_KEY_ID=\$(echo $output | jq -r ."Credentials"."AccessKeyId")
                   export AWS_SECRET_ACCESS_KEY=\$(echo $output | jq -r ."Credentials"."SecretAccessKey")
                   PKG_URL=\$(aws s3 presign s3://test-hugo-site-fortinetcloudcse/\$PKG_NAME.tar.gz --expires-in 900)
                   unset AWS_SESSION_TOKEN
                   unset AWS_ACCESS_KEY_ID
                   unset AWS_SECRET_ACCESS_KEY
                   echo $PKG_URL
               '''
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
