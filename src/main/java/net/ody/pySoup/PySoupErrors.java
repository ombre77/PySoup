package net.ody.pySoup;

import org.graalvm.polyglot.Context;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.SourceSection;
import org.graalvm.polyglot.Value;

import java.util.logging.Logger;

public class PySoupErrors {
    private PySoupErrors() {}

    public static void log(Logger logger, String scriptName, Context context, PolyglotException e) {
        if (e.isHostException()) {
            Throwable host = e.asHostException();
            logger.severe("[" + scriptName + "] Java error in bridge call: "
                    + host.getClass().getSimpleName() + ": " + host.getMessage());
            for (StackTraceElement el : host.getStackTrace()) {
                logger.severe("    at " + el);
                if (el.getClassName().startsWith("net.ody.pySoup")) break;
            }
            return;
        }

        if (e.isGuestException()) {
            logger.severe("[" + scriptName + "] Python error:\n" + formatPythonTraceback(context, e));
            return;
        }

        logger.severe("[" + scriptName + "] Internal engine error: " + e.getMessage());
    }

    private static String formatGuestLocation(PolyglotException e) {
        SourceSection loc = e.getSourceLocation();
        if (loc == null) {
            return null;
        }
        return loc.getSource().getName() + ":" + loc.getStartLine();
    }

    private static String formatPythonTraceback(Context context, PolyglotException e) {
        if (!e.isGuestException()) {
            return e.getMessage();
        }
        Value excInstance = e.getGuestObject();
        if (excInstance == null) {
            return e.getMessage(); // last resort
        }
        try {
            Value traceback = context.eval("python", "import traceback; traceback");
            Value excType = excInstance.getMetaObject();
            Value excTb = excInstance.getMember("__traceback__");

            Value lines = traceback.invokeMember("format_exception", excType, excInstance, excTb);
            StringBuilder sb = new StringBuilder();
            for (long i = 0; i < lines.getArraySize(); i++) {
                sb.append(lines.getArrayElement(i).asString());
            }
            return sb.toString();
        } catch (Exception fmtErr) {
            return e.getMessage() + " (failed to format traceback: " + fmtErr + ")";
        }
    }

    public static String summarize(PolyglotException e) {
        if (e.isHostException()) {
            Throwable host = e.asHostException();
            return host.getClass().getSimpleName() + ": " + host.getMessage();
        }
        if (e.isGuestException()) {
            String msg = e.getMessage();
            return msg != null ? msg : "Python error";
        }
        return e.getMessage();
    }
}
