node('docker-test') {
    stage('Checkout') {
        checkout([
            $class: 'GitSCM',
            branches: scm.branches,
            doGenerateSubmoduleConfigurations: scm.doGenerateSubmoduleConfigurations,
            extensions: [[$class: 'CloneOption', noTags: false, shallow: false, depth: 0, reference: '']],
            userRemoteConfigs: scm.userRemoteConfigs,
        ])
    }


    stage('test') {
        print(currentBuild.changeSets)
        print(currentBuild.changeSets.getClass())

        for (change in currentBuild.changeSets) {
            print(change)
            print(change.getClass())
        }
    }
}
