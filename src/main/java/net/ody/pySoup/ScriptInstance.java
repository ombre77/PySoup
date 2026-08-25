package net.ody.pySoup;

import org.graalvm.polyglot.Context;

import java.io.File;

public final class ScriptInstance {
    private final String name;
    private final File file;
    private final Context context;

    public ScriptInstance(String name, File file, Context context) {
        this.name = name;
        this.file = file;
        this.context = context;
    }

    public String getName() {
        return name;
    }

    public File getFile() {
        return file;
    }

    public Context getContext() {
        return context;
    }
    
    public void close() {
        context.close();
    }
}
