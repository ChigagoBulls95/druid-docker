FROM banno/druid-base:latest

MAINTAINER Zach Cox zach.cox@banno.com

ADD runtime.properties /usr/local/druid/config/overlord/

ENTRYPOINT exec java $DRUID_COMMON_JAVA_OPTIONS -Xmx1g $(/common-druid.sh) -Ddruid.processing.buffer.sizeBytes=104857600 -Ddruid.indexer.runner.type=$RUNNER_TYPE -cp "/usr/local/druid/config/_common:/usr/local/druid/config/overlord:/usr/local/druid/lib/*" io.druid.cli.Main server overlord
