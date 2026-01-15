package com.jsonviewertool;

public class JsonUtils {

    public static boolean isValidJson(String json) {
        if (json == null || json.isEmpty()) return false;
        json = json.trim();
        return (json.startsWith("{") && json.endsWith("}"))
            || (json.startsWith("[") && json.endsWith("]"));
    }
}
