FROM banno/druid-base:latest

MAINTAINER Zach Cox zach.cox@banno.com

ENTRYPOINT exec java $(/common-druid.sh) -Ddruid.indexer.fork.property.druid.computation.buffer.size=268435456 -cp "/usr/local/druid/config/_common:/usr/local/druid/lib/*" io.druid.cli.Main server middleManager
