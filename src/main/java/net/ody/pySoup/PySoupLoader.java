package net.ody.pySoup;

import io.papermc.paper.plugin.loader.PluginClasspathBuilder;
import io.papermc.paper.plugin.loader.PluginLoader;
import io.papermc.paper.plugin.loader.library.impl.MavenLibraryResolver;
import org.eclipse.aether.artifact.DefaultArtifact;
import org.eclipse.aether.repository.RemoteRepository;
import org.eclipse.aether.graph.Dependency;

public class PySoupLoader implements PluginLoader {

    @Override
    public void classloader(PluginClasspathBuilder classpathBuilder) {
        MavenLibraryResolver resolver = new MavenLibraryResolver();

        resolver.addRepository(new RemoteRepository.Builder(
                "central", "default", MavenLibraryResolver.MAVEN_CENTRAL_DEFAULT_MIRROR
        ).build());

        resolver.addDependency(new Dependency(
                new DefaultArtifact("org.graalvm.polyglot:polyglot:25.0.2"), null));

        resolver.addDependency(new Dependency(
                new DefaultArtifact("org.graalvm.polyglot:python:pom:25.0.2"), null));
        resolver.addDependency(new Dependency(
                new DefaultArtifact("org.graalvm.python:python-embedding:25.0.2"), null));

        classpathBuilder.addLibrary(resolver);
    }
}