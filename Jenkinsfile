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

        def hasBumpCommit = false
        def hasMergeCommit = false

        for (changeSet in currentBuild.changeSets) {
            for (change in changeSet.items) {
                print(change)
                print(change.msg)
                hasBumpCommit = hasBumpCommit || change.msg.startsWith('Bump Confluent') || change.msg.startsWith('Bump Kafka')
                hasMergeCommit = hasMergeCommit || change.msg.startsWith('Merge branch')
            }
        }

        print(hasBumpCommit)
        print(hasMergeCommit)

        if (hasBumpCommit && hasMergeCommit) {
            currentBuild.result = 'ABORTED'
            error('Cancelling build for bump commit merges as they are generally noop but causes build queue spike')
        }
    }
}
