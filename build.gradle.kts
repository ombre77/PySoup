plugins {
    id("java-library")
    id("xyz.jpenilla.run-paper") version "3.0.2"
}

group = "net.ody.pySoup"
version = "0.1.0"
description = "PySoup"

java {
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(21))
    }
}

repositories {
    mavenCentral()
    maven("https://repo.papermc.io/repository/maven-public/")
}

dependencies {
    // Paper API - provided by the server at runtime, not bundled.
    compileOnly("io.papermc.paper:paper-api:1.21.11-R0.1-SNAPSHOT")

    // GraalVM Polyglot API + GraalPy - compileOnly here because these are
    // NOT bundled into the plugin jar. PySoupLoader resolves them as
    // separate classpath entries at server startup instead (via Paper's
    // PluginLoader/MavenLibraryResolver). Shading these in breaks Truffle's
    // multi-release jar layout, so don't switch this back to
    // implementation(...) or re-add the shadow plugin.
    compileOnly("org.graalvm.polyglot:polyglot:25.0.2")
    compileOnly("org.graalvm.polyglot:python:25.0.2")
    compileOnly("org.graalvm.python:python-embedding:25.0.2")
}

tasks {
    compileJava {
        options.encoding = "UTF-8"
    }

    processResources {
        val props = mapOf("version" to version, "description" to project.description)
        inputs.properties(props)
        filteringCharset = "UTF-8"
        filesMatching("paper-plugin.yml") {
            expand(props)
        }
    }

    runServer {
        // Configure the Minecraft version for the test server.
        minecraftVersion("1.21.11")
        jvmArgs("-Xms2G", "-Xmx2G")
    }
}