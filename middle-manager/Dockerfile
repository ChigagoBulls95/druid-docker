FROM banno/druid-base:latest

MAINTAINER Zach Cox zach.cox@banno.com

ENTRYPOINT exec java $(/common-druid.sh) -Ddruid.indexer.fork.property.druid.computation.buffer.size=268435456 -Ddruid.indexer.runner.javaOpts="-server -Xmx$JAVA_PEON_MAX_HEAP -Xms$JAVA_PEON_MIN_HEAP -XX:MaxDirectMemorySize=$JAVA_PEON_MAX_DIRECT_MEMORY" -cp "/usr/local/druid/config/_common:/usr/local/druid/lib/*" io.druid.cli.Main server middleManager
